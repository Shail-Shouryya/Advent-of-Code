package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

// --- Day 1: Report Repair ---
// After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.
//
// The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.
//
// To save your vacation, you need to get all fifty stars by December 25th.
//
// Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!
//
// Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.
//
// Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.
//
// For example, suppose your expense report contained the following:
//
// 1721
// 979
// 366
// 299
// 675
// 1456
// In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.
//
// Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?
//
// Your puzzle answer was __________.
//
// --- Part Two ---
// The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.
//
// Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.
//
// In your expense report, what is the product of the three entries that sum to 2020?
// Your puzzle answer was __________.

func solveDay1() {
	text := readPuzzleInput("puzzle_day_1.txt")
	allNumbers := convertPuzzleTextToSlice(text)
	fmt.Println(allNumbers)
}

func readPuzzleInput(fileName string) string {
	// f is a slice of type bytes
	// error is of type error
	f, error := ioutil.ReadFile(fileName)
	if error != nil {
		fmt.Println("ERROR! The exact error was ", error)
	}
	// convert the slice of bytes to its string representation
	// without this step, we get a slice of bytes
	// representing its corresponding character's
	// Unicode code point
	text := string(f)
	fmt.Println(text)
	return text
}

func convertPuzzleTextToSlice(text string) []int {
	textentries := strings.Split(text, "\n")
	var intEntries []int
	for _, entry := range textentries {
		number, err := strconv.Atoi(entry)
		// If there is an error converting the text
		// to an integer (could happen if text is a
		// text character, an empty space, or an
		// empty line), we don't add it to our slice.
		// If the string conversion goes fine, we
		// add the converted character (number variable)
		// to our slice of integers, intEntries.
		// NOTE Atoi is short for "ASCII to integer"
		if err == nil {
			intEntries = append(intEntries, number)
		}
	}
	return intEntries
}
