package main

import (
	"fmt"
	"strconv"
)

// check if id repeats pattern at least twice
func isInvalidIDPart2Day2(num int) bool {
	numStr := strconv.Itoa(num)
	length := len(numStr)

	// try all possible pattern lengths to half string length
	for patternLen := 1; patternLen <= length/2; patternLen++ {
		// only check if length divides evenly 
		if length%patternLen != 0 {
			continue
		}

		// extract potential pattern
		pattern := numStr[:patternLen]

		// build expected pattern
		repeats := length / patternLen
		expected := ""
		for i := 0; i < repeats; i++ {
			expected += pattern
		}

		// if expected string matches, invalid
		if expected == numStr && repeats >= 2 {
			return true
		}
	}

	return false
}

// return sum
func findInvalidIDsInRangePart2Day2(start int, end int) int64 {
	var sum int64 = 0

	for num := start; num <= end; num++ {
		if isInvalidIDPart2Day2(num) {
			sum += int64(num)
		}
	}

	return sum
}

// test with example input
func testWithExamplePart2Day2() {
	exampleInput := "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

	ranges := parseRangesDay2(exampleInput)
	var totalSum int64 = 0

	for _, r := range ranges {
		sum := findInvalidIDsInRangePart2Day2(r[0], r[1])
		totalSum += sum
	}

	fmt.Printf("example result (part 2): %d (expected 4174379265)\n", totalSum)
}

// process range, return sum of invalid ids
func processRangesPart2Day2(inputStr string) int64 {
	ranges := parseRangesDay2(inputStr)
	var totalSum int64 = 0

	for _, r := range ranges {
		sum := findInvalidIDsInRangePart2Day2(r[0], r[1])
		totalSum += sum
	}

	return totalSum
}
