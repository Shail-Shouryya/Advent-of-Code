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
	printLineDivide()
	part1Solution := solvePartOne(allNumbers)
	printLineDivide()
	fmt.Println("Solution to day 1 part 1: ", part1Solution)

	printLineDivide()
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
	fmt.Println(textentries)
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
		} else {
			fmt.Println(err)
		}
	}
	fmt.Println(intEntries)
	return intEntries
}

func solvePartOne(allNumbers []int) int {
	first, second := findPairSumTo2020(allNumbers)
	product := first * second
	fmt.Println(fmt.Sprintf("The two numbers that sum to 2020 are: %d, %d", first, second))
	fmt.Println(fmt.Sprintf("The product of these two numbers is:  %d", product))
	return product
}
func findPairSumTo2020(allNumbers []int) (int, int) {
	// Declare AND initialize a map that takes an
	// integer as a key and an integer as the value
	// to its key - similar to a dictionary in Python,
	// a hash in Ruby, and a HashMap in Java.
	// It's important to initialize the map since
	// just declaring a map but NOT initializing it
	// (e.g. var pairs map[int]int) will result in
	// this compile time error:
	// panic: assignment to entry in nil map
	pairs := make(map[int]int)
	// fmt.Println(pairs)

	// https://stackoverflow.com/questions/2050391/how-to-check-if-a-map-contains-a-key-in-go
	for _, number := range allNumbers {
		value, ok := pairs[number]
		if ok {
			return number, value
		}
		pairs[2020-number] = number
	}
	return 0, -1
}
