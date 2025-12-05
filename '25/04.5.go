package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

// count @ symbols in 8 adjacent cells
func countAdjacentRollsDay4Part2(grid [][]byte, row, col int) int {
	count := 0
	rows := len(grid)
	cols := len(grid[0])

	// 8 adjacent positions 
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

// find all accessible rolls in current grid state
func findAccessibleDay4Part2(grid [][]byte) []struct {
	row, col int
} {
	var accessible []struct {
		row, col int
	}

	rows := len(grid)

	for r := 0; r < rows; r++ {
		for c := 0; c < len(grid[r]); c++ {
			// only check cells with paper rolls
			if grid[r][c] == '@' {
				// count adjacent rolls
				adjacent := countAdjacentRollsDay4Part2(grid, r, c)

				// accessible if fewer than 4 adjacent
				if adjacent < 4 {
					accessible = append(accessible, struct {
						row, col int
					}{r, c})
				}
			}
		}
	}

	return accessible
}

// remove accessible rolls until none remain
func findTotalRemovableDay4Part2(grid [][]byte) int {
	totalRemoved := 0

	// keep removing until no more accessible rolls
	for {
		// find all accessible rolls
		accessible := findAccessibleDay4Part2(grid)

		// if none accessible, we're done
		if len(accessible) == 0 {
			break
		}

		// remove all accessible rolls
		for _, pos := range accessible {
			grid[pos.row][pos.col] = '.'
		}

		// add to total
		totalRemoved += len(accessible)
	}

	return totalRemoved
}

// read puzzle input from .md file
func readPuzzleInputDay4Part2(filename string) ([]string, error) {
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

// test with provided example for part two
func testWithExampleDay4Part2() {
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

	// convert to mutable grid
	mutableGrid := make([][]byte, len(exampleGrid))
	for i, row := range exampleGrid {
		mutableGrid[i] = []byte(row)
	}

	totalRemoved := findTotalRemovableDay4Part2(mutableGrid)
	fmt.Printf("example result: %d (expected 43)\n", totalRemoved)
}

func main() {
	// part two
	testWithExampleDay4Part2()

	fmt.Println()

	// read puzzle input
	grid, err := readPuzzleInputDay4Part2("'25/04.md")
	if err != nil {
		log.Fatal(err)
	}

	// convert to mutable grid
	mutableGrid := make([][]byte, len(grid))
	for i, row := range grid {
		mutableGrid[i] = []byte(row)
	}

	fmt.Printf("read grid of size %d x %d\n", len(mutableGrid), len(mutableGrid[0]))

	totalRemoved := findTotalRemovableDay4Part2(mutableGrid)

	fmt.Printf("total removable paper rolls (part two): %d\n", totalRemoved)
}
