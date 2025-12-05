package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

// find max joltage by trying all pairs of positions
func findMaxJoltageDay3(bank string) int {
	maxJoltage := 0
	length := len(bank)

	// try all pairs of positions (i < j)
	for i := 0; i < length; i++ {
		for j := i + 1; j < length; j++ {
			// form number using digits at positions i and j
			digit1 := int(bank[i] - '0')
			digit2 := int(bank[j] - '0')
			joltage := digit1*10 + digit2

			if joltage > maxJoltage {
				maxJoltage = joltage
			}
		}
	}

	return maxJoltage
}

// process all battery banks, sum max joltage
func calculateTotalJoltageDay3(banks []string) int {
	totalJoltage := 0

	for _, bank := range banks {
		maxJoltage := findMaxJoltageDay3(bank)
		totalJoltage += maxJoltage
	}

	return totalJoltage
}

// read puzzle input from .md file
func readPuzzleInputDay3(filename string) ([]string, error) {
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

// test with provided example
func testWithExampleDay3() {
	exampleBanks := []string{
		"987654321111111",
		"811111111111119",
		"234234234234278",
		"818181911112111",
	}

	totalJoltage := calculateTotalJoltageDay3(exampleBanks)
	fmt.Printf("example result: %d (expected 357)\n", totalJoltage)
}

func main() {
	// part one
	testWithExampleDay3()

	fmt.Println()

	// read puzzle input
	banks, err := readPuzzleInputDay3("'25/03.md")
	if err != nil {
		log.Fatal(err)
	}

	fmt.Printf("read %d battery banks from puzzle input\n", len(banks))

	totalJoltage := calculateTotalJoltageDay3(banks)

	fmt.Printf("total output joltage (part one): %d\n", totalJoltage)
}
