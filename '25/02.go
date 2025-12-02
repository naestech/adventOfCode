package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

// check if pattern repeats twice
func isInvalidIDDay2(num int) bool {
	numStr := strconv.Itoa(num)
	length := len(numStr)

	// only even-length numbers 
	if length%2 != 0 {
		return false
	}

	// split into halves, compare
	halfLen := length / 2
	left := numStr[:halfLen]
	right := numStr[halfLen:]

	return left == right
}

// find all invalid ids, return sum
func findInvalidIDsInRangeDay2(start int, end int) int64 {
	var sum int64 = 0

	for num := start; num <= end; num++ {
		if isInvalidIDDay2(num) {
			sum += int64(num)
		}
	}

	return sum
}

// parse separated ranges from input
func parseRangesDay2(line string) [][2]int {
	var ranges [][2]int

	rangeStrs := strings.Split(line, ",")

	for _, rangeStr := range rangeStrs {
		// split dash
		parts := strings.Split(rangeStr, "-")

		if len(parts) != 2 {
			continue
		}

		start, err := strconv.Atoi(parts[0])
		if err != nil {
			log.Fatal(err)
		}

		end, err := strconv.Atoi(parts[1])
		if err != nil {
			log.Fatal(err)
		}

		ranges = append(ranges, [2]int{start, end})
	}

	return ranges
}

// read input 
func readPuzzleInputDay2(filename string) (string, error) {
	file, err := os.Open(filename)
	if err != nil {
		return "", err
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	foundPuzzleInput := false

	for scanner.Scan() {
		line := scanner.Text()

		// locate input section
		if strings.Contains(line, "--- IDs: Puzzle input ---") {
			foundPuzzleInput = true
			continue
		}

		if foundPuzzleInput && line != "" {
			return line, nil
		}
	}

	if err := scanner.Err(); err != nil {
		return "", err
	}

	return "", nil
}

// test with example 
func testWithExampleDay2() {
	exampleInput := "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

	ranges := parseRangesDay2(exampleInput)
	var totalSum int64 = 0

	for _, r := range ranges {
		sum := findInvalidIDsInRangeDay2(r[0], r[1])
		totalSum += sum
	}

	fmt.Printf("example result: %d (expected 1227775554)\n", totalSum)
}

func main() {
	// part one
	testWithExampleDay2()

	fmt.Println()

	// read puzzle input
	input, err := readPuzzleInputDay2("02.md")
	if err != nil {
		log.Fatal(err)
	}

	ranges := parseRangesDay2(input)

	fmt.Printf("found %d ranges\n", len(ranges))

	// process ranges, sum invalid ids
	var totalSum int64 = 0

	for _, r := range ranges {
		sum := findInvalidIDsInRangeDay2(r[0], r[1])
		totalSum += sum
	}

	fmt.Printf("sum of all invalid IDs (part one): %d\n", totalSum)

	fmt.Println()

	// part two
	testWithExamplePart2Day2()

	fmt.Println()

	// process all ranges, sum invalid ids
	totalSum = processRangesPart2Day2(input)

	fmt.Printf("sum of all invalid IDs (part two): %d\n", totalSum)
}
