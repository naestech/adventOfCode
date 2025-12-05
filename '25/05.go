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
type IngredientRange struct {
	start, end int64
}

// parse range from "start-end" format
func parseRange(line string) IngredientRange {
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

	return IngredientRange{start: start, end: end}
}

// merge overlapping ranges into single sorted array
func mergeRanges(ranges []IngredientRange) []IngredientRange {
	if len(ranges) == 0 {
		return ranges
	}

	// sort by start value
	sort.Slice(ranges, func(i, j int) bool {
		return ranges[i].start < ranges[j].start
	})

	// merge overlapping ranges
	var merged []IngredientRange
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

// check if ingredient id is fresh 
func isFresh(id int64, ranges []IngredientRange) bool {
	// binary search for efficiency
	left, right := 0, len(ranges)-1

	for left <= right {
		mid := (left + right) / 2

		if id >= ranges[mid].start && id <= ranges[mid].end {
			return true
		}

		if id < ranges[mid].start {
			right = mid - 1
		} else {
			left = mid + 1
		}
	}

	return false
}

// count fresh ingredients from available list
func countFreshIngredientsDay5(ranges []IngredientRange, ingredients []int64) int {
	fresh := 0

	for _, id := range ingredients {
		if isFresh(id, ranges) {
			fresh++
		}
	}

	return fresh
}

// read puzzle input from .md file
func readPuzzleInputDay5(filename string) ([]IngredientRange, []int64, error) {
	file, err := os.Open(filename)
	if err != nil {
		return nil, nil, err
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var ranges []IngredientRange
	var ingredients []int64
	foundHeader := false
	blankLineFound := false

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

		// blank line separates ranges from ingredients
		if line == "" {
			blankLineFound = true
			continue
		}

		// parse ranges before blank line
		if !blankLineFound {
			ranges = append(ranges, parseRange(line))
		} else {
			// parse ingredient ids after blank line
			id, err := strconv.ParseInt(line, 10, 64)
			if err != nil {
				log.Fatal(err)
			}
			ingredients = append(ingredients, id)
		}
	}

	if err := scanner.Err(); err != nil {
		return nil, nil, err
	}

	return ranges, ingredients, nil
}

// test with provided example
func testWithExampleDay5() {
	exampleRanges := []IngredientRange{
		{3, 5},
		{10, 14},
		{16, 20},
		{12, 18},
	}

	exampleIngredients := []int64{1, 5, 8, 11, 17, 32}

	// merge ranges
	merged := mergeRanges(exampleRanges)

	fresh := countFreshIngredientsDay5(merged, exampleIngredients)
	fmt.Printf("example result: %d (expected 3)\n", fresh)
}

func main() {
	// part one
	testWithExampleDay5()

	fmt.Println()

	// read puzzle input
	ranges, ingredients, err := readPuzzleInputDay5("'25/05.md")
	if err != nil {
		log.Fatal(err)
	}

	// merge overlapping ranges
	merged := mergeRanges(ranges)

	fmt.Printf("read %d ranges (merged to %d), %d ingredients\n", len(ranges), len(merged), len(ingredients))

	fresh := countFreshIngredientsDay5(merged, ingredients)

	fmt.Printf("fresh ingredients (part one): %d\n", fresh)
}
