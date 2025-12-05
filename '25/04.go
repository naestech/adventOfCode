package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

// count @ symbols in 8 adjacent cells
func countAdjacentRolls(grid []string, row, col int) int {
	count := 0
	rows := len(grid)
	cols := len(grid[0])

	// 8 adjacent positions (all directions)
	for dr := -1; dr <= 1; dr++ {
		for dc := -1; dc <= 1; dc++ {
			// skip the center cell
			if dr == 0 && dc == 0 {
				continue
			}

			nr, nc := row+dr, col+dc

			// check bounds
			if nr >= 0 && nr < rows && nc >= 0 && nc < cols {
				if grid[nr][nc] == '@' {
					count++
				}
			}
		}
	}

	return count
}

// find rolls accessible by forklifts 
func findAccessibleRollsDay4(grid []string) int {
	accessible := 0
	rows := len(grid)

	for r := 0; r < rows; r++ {
		for c := 0; c < len(grid[r]); c++ {
			// only check cells with paper rolls
			if grid[r][c] == '@' {
				// count adjacent rolls
				adjacent := countAdjacentRolls(grid, r, c)

				// accessible if fewer than 4 adjacent
				if adjacent < 4 {
					accessible++
				}
			}
		}
	}

	return accessible
}

// read puzzle input from .md file
func readPuzzleInputDay4(filename string) ([]string, error) {
	file, err := os.Open(filename)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var grid []string
	foundPuzzleInput := false

	for scanner.Scan() {
		line := scanner.Text()

		// locate puzzle input section 
		if strings.Contains(line, "--- Puzzle input:") {
			foundPuzzleInput = true
			continue
		}

		if foundPuzzleInput && line != "" {
			grid = append(grid, line)
		}
	}

	if err := scanner.Err(); err != nil {
		return nil, err
	}

	return grid, nil
}

// test with provided example
func testWithExampleDay4() {
	exampleGrid := []string{
		"..@@.@@@@.",
		"@@@.@.@.@@",
		"@@@@@.@.@@",
		"@.@@@@..@.",
		"@@.@@@@.@@",
		".@@@@@@@.@",
		".@.@.@.@@@",
		"@.@@@.@@@@",
		".@@@@@@@@.",
		"@.@.@@@.@.",
	}

	accessible := findAccessibleRollsDay4(exampleGrid)
	fmt.Printf("example result: %d (expected 13)\n", accessible)
}

func main() {
	// part one
	testWithExampleDay4()

	fmt.Println()

	// read puzzle input
	grid, err := readPuzzleInputDay4("'25/04.md")
	if err != nil {
		log.Fatal(err)
	}

	fmt.Printf("read grid of size %d x %d\n", len(grid), len(grid[0]))

	accessible := findAccessibleRollsDay4(grid)

	fmt.Printf("accessible paper rolls (part one): %d\n", accessible)
}
