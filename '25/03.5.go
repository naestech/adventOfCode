package main

import (
	"bufio"
	"fmt"
	"log"
	"math/big"
	"os"
	"strings"
)

// find max 12-digit joltage 
func findMaxJoltageDay3Part2(bank string) string {
	length := len(bank)
	toSkip := length - 12

	// use monotonic stack
	var stack []byte

	for i := 0; i < length; i++ {
		digit := bank[i]

		// while can skip and top of stack is smaller, remove 
		for toSkip > 0 && len(stack) > 0 && stack[len(stack)-1] < digit {
			stack = stack[:len(stack)-1]
			toSkip--
		}

		stack = append(stack, digit)
	}

	// if skips left, skip from the end
	for toSkip > 0 {
		stack = stack[:len(stack)-1]
		toSkip--
	}

	// return first 12 digits as string
	return string(stack[:12])
}

// process all battery banks, sum max 12-digit joltage
func calculateTotalJoltageDay3Part2(banks []string) string {
	totalJoltage := new(big.Int)

	for _, bank := range banks {
		// find max 12-digit joltage for this bank
		maxJoltageStr := findMaxJoltageDay3Part2(bank)
		joltageInt := new(big.Int)
		joltageInt.SetString(maxJoltageStr, 10)

		// add to total
		totalJoltage.Add(totalJoltage, joltageInt)
	}

	return totalJoltage.String()
}

// read puzzle input from .md file
func readPuzzleInputDay3Part2(filename string) ([]string, error) {
	file, err := os.Open(filename)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var banks []string
	foundPuzzleInput := false

	for scanner.Scan() {
		line := scanner.Text()

		// locate puzzle input section 
		if strings.Contains(line, "--- Puzzle input:") {
			foundPuzzleInput = true
			continue
		}

		if foundPuzzleInput && line != "" {
			banks = append(banks, line)
		}
	}

	if err := scanner.Err(); err != nil {
		return nil, err
	}

	return banks, nil
}

// test with provided example for part two
func testWithExampleDay3Part2() {
	exampleBanks := []string{
		"987654321111111",
		"811111111111119",
		"234234234234278",
		"818181911112111",
	}

	totalJoltage := calculateTotalJoltageDay3Part2(exampleBanks)
	fmt.Printf("example result: %s (expected 3121910778619)\n", totalJoltage)
}

func main() {
	// part two
	testWithExampleDay3Part2()

	fmt.Println()

	// read puzzle input
	banks, err := readPuzzleInputDay3Part2("'25/03.md")
	if err != nil {
		log.Fatal(err)
	}

	fmt.Printf("read %d battery banks from puzzle input\n", len(banks))

	totalJoltage := calculateTotalJoltageDay3Part2(banks)

	fmt.Printf("total output joltage (part two): %s\n", totalJoltage)
}
