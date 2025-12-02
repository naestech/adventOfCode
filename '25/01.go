package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

// single dial rotation with direction and distance
type rotation struct {
	direction byte // 'L' or 'R'
	distance  int
}

// extract direction and distance from input strings
func parseRotation(line string) rotation {
	// determine direction
	direction := line[0]

	// determine distance
	distanceStr := line[1:]
	distance, err := strconv.Atoi(distanceStr)
	if err != nil {
		log.Fatal(err)
	}

	return rotation{direction: direction, distance: distance}
}

// open 01.md
func readInput(filename string) ([]string, error) {
	file, err := os.Open(filename)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var rotations []string
	foundPuzzleInput := false

	for scanner.Scan() {
		line := scanner.Text()

		// locate, extract puzzle input
		if strings.Contains(line, "--- Attached document") {
			foundPuzzleInput = true
			continue
		}

		if foundPuzzleInput && line != "" {
			rotations = append(rotations, line)
		}
	}

	if err := scanner.Err(); err != nil {
		return nil, err
	}

	return rotations, nil
}

// update position based on rotation
func rotateDialPosition(currentPosition int, rot rotation) int {
	if rot.direction == 'R' {
		// right rotation: add distance, wrap around with modulo
		return (currentPosition + rot.distance) % 100
	} else {
		// left rotation: subtract distance
		return ((currentPosition-rot.distance)%100 + 100) % 100
	}
}

// returns times dial lands on 0
func processRotations(rotationStrings []string) int {
	currentPosition := 50 
	zeroCount := 0

	for _, rotationStr := range rotationStrings {
		// get direction and distance
		rot := parseRotation(rotationStr)

		currentPosition = rotateDialPosition(currentPosition, rot)

		// check if we landed on 0
		if currentPosition == 0 {
			zeroCount++
		}
	}

	return zeroCount
}

// run solution with example 
func testWithExample() {
	exampleRotations := []string{
		"L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82",
	}

	zeroCount := processRotations(exampleRotations)
	fmt.Printf("example result: %d (expected 3)\n", zeroCount)
}

func main() {
	// part one
	testWithExample()

	fmt.Println()

	rotations, err := readInput("'25/01.md")
	if err != nil {
		log.Fatal(err)
	}

	fmt.Printf("read %d rotations from puzzle input\n", len(rotations))

	zeroCount := processRotations(rotations)

	fmt.Printf("password (part one): %d\n", zeroCount)

	fmt.Println()

	// part two
	testWithExamplePart2()

	fmt.Println()

	zeroCountPart2 := processRotationsPart2(rotations)

	fmt.Printf("password (part two): %d\n", zeroCountPart2)
}
