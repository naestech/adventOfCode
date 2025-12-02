package main

import "fmt"

func rotateDialPositionPart2(currentPosition int, rot rotation) (int, int) {
	zeroCount := 0

	for step := 0; step < rot.distance; step++ {
		if rot.direction == 'R' {
			// right: increase position 
			currentPosition = (currentPosition + 1) % 100
		} else {
			// left: decrease position 
			currentPosition = ((currentPosition-1)%100 + 100) % 100
		}

		// count zeros hit during rotation
		if currentPosition == 0 {
			zeroCount++
		}
	}

	return currentPosition, zeroCount
}

// returns 0 passes including steps
func processRotationsPart2(rotationStrings []string) int {
	currentPosition := 50
	totalZeroCount := 0

	for _, rotationStr := range rotationStrings {
		// get direction and distance
		rot := parseRotation(rotationStr)

		newPosition, zerosInThisRotation := rotateDialPositionPart2(currentPosition, rot)

		currentPosition = newPosition

		// total zeros
		totalZeroCount += zerosInThisRotation
	}

	return totalZeroCount
}

// test part two with example input
func testWithExamplePart2() {
	exampleRotations := []string{
		"L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82",
	}

	zeroCount := processRotationsPart2(exampleRotations)
	fmt.Printf("example test (part two): %d (expected 6)\n", zeroCount)
}
