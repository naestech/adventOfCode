package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
	"strconv"
	"strings"
)

// range of fresh ingredient ids
type IngredientRangeDay5Part2 struct {
	start, end int64
}

// parse range from "start-end" format
func parseRangeDay5Part2(line string) IngredientRangeDay5Part2 {
	parts := strings.Split(line, "-")
	if len(parts) != 2 {
		log.Fatal("invalid range format:", line)
	}

	start, err := strconv.ParseInt(parts[0], 10, 64)
	if err != nil {
		log.Fatal(err)
	}

	end, err := strconv.ParseInt(parts[1], 10, 64)
	if err != nil {
		log.Fatal(err)
	}

	return IngredientRangeDay5Part2{start: start, end: end}
}

// merge overlapping ranges into single sorted array
func mergeRangesDay5Part2(ranges []IngredientRangeDay5Part2) []IngredientRangeDay5Part2 {
	if len(ranges) == 0 {
		return ranges
	}

	// sort by start value
	sort.Slice(ranges, func(i, j int) bool {
		return ranges[i].start < ranges[j].start
	})

	// merge overlapping ranges
	var merged []IngredientRangeDay5Part2
	current := ranges[0]

	for i := 1; i < len(ranges); i++ {
		// if next range overlaps or touches current, merge them
		if ranges[i].start <= current.end+1 {
			// extend current range
			if ranges[i].end > current.end {
				current.end = ranges[i].end
			}
		} else {
			// no overlap, add current to merged and start new
			merged = append(merged, current)
			current = ranges[i]
		}
	}

	// add final range
	merged = append(merged, current)

	return merged
}

// count total fresh ingredient ids in all merged ranges
func countTotalFreshDay5Part2(ranges []IngredientRangeDay5Part2) int64 {
	var total int64 = 0

	// sum sizes of all non-overlapping ranges
	for _, r := range ranges {
		total += r.end - r.start + 1
	}

	return total
}

// read ranges from puzzle input
func readRangesDay5Part2(filename string) ([]IngredientRangeDay5Part2, error) {
	file, err := os.Open(filename)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var ranges []IngredientRangeDay5Part2
	foundHeader := false

	for scanner.Scan() {
		line := scanner.Text()

		// locate puzzle input header
		if strings.Contains(line, "--- Puzzle input:") {
			foundHeader = true
			continue
		}

		// haven't found header yet, keep skipping
		if !foundHeader {
			continue
		}

		// blank line separates ranges from ingredients (stop before it)
		if line == "" {
			break
		}

		// parse ranges only
		ranges = append(ranges, parseRangeDay5Part2(line))
	}

	if err := scanner.Err(); err != nil {
		return nil, err
	}

	return ranges, nil
}

// test with provided example
func testWithExampleDay5Part2() {
	exampleRanges := []IngredientRangeDay5Part2{
		{3, 5},
		{10, 14},
		{16, 20},
		{12, 18},
	}

	// merge ranges
	merged := mergeRangesDay5Part2(exampleRanges)

	total := countTotalFreshDay5Part2(merged)
	fmt.Printf("example result: %d (expected 14)\n", total)
}

func main() {
	// part two
	testWithExampleDay5Part2()

	fmt.Println()

	// read puzzle input 
	ranges, err := readRangesDay5Part2("'25/05.md")
	if err != nil {
		log.Fatal(err)
	}

	// merge overlapping ranges
	merged := mergeRangesDay5Part2(ranges)

	fmt.Printf("read %d ranges (merged to %d)\n", len(ranges), len(merged))

	total := countTotalFreshDay5Part2(merged)

	fmt.Printf("total fresh ingredient ids (part two): %d\n", total)
}
