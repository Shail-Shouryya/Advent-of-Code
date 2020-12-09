'''
--- Day 1: Report Repair ---
After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.

The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

To save your vacation, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?

Your puzzle answer was __________.

--- Part Two ---
The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?
Your puzzle answer was __________.
'''

def main():
    text        = read_puzzle_input('puzzle_day_1.txt')
    all_numbers = convert_puzzle_text_to_list(text)
    part_1_solution = solve_part_one(all_numbers)
    print('*' * 80)
    part_2_solution = solve_part_two(all_numbers)
    print('*' * 80)
    print(f'Solution to part 1: {part_1_solution}')
    print(f'Solution to part 2: {part_2_solution}')




def read_puzzle_input(filename) :
    with open(filename, 'r', encoding='utf-8') as puzzle_input:
        return puzzle_input.read()


def convert_puzzle_text_to_list(text):
    return [int(number) for number in text.split()]


def solve_part_one(all_numbers):
    first, second = find_pair_sum_to_2020(all_numbers)
    product = first * second
    print(f'The two numbers that sum to 2020 are: {first}, {second}')
    print(f'The product of these two numbers is:  {product}')
    return product


def find_pair_sum_to_2020(all_numbers):
    pairs = {}
    for number in all_numbers:
        if number in pairs:
            return number, pairs[number]
        else:
            pairs[2020 - number] = number




def solve_part_two(all_numbers):
    first, second, third = find_triplet_sum_to_2020(all_numbers)
    product = first * second * third
    print(f'The three numbers that sum to 2020 are: {first}, {second}, {third}')
    print(f'The product of these three numbers is:  {product}')
    return product


def find_triplet_sum_to_2020(all_numbers):
    all_numbers.sort()
    first = 0
    last  = len(all_numbers) - 1
    not_found = True
    # print(max(all_numbers))
    current_triplet_sum = 0
    while all_numbers[last]  > 2020: last  -= 1
    while all_numbers[first] < 0:    first  += 1
    mover = first + 1           # initialize mover as first + 1 to start while loop below
    while not_found:
        # print(current_triplet_sum)
        lowest  = first
        highest = last
        while lowest < mover < highest:
            # print(lowest, highest, current_triplet_sum)
            mover = first + (highest - lowest)//2
            current_triplet_sum = all_numbers[first] + all_numbers[mover] + all_numbers[last]
            if   current_triplet_sum < 2020:  highest = mover - 1
            elif current_triplet_sum > 2020:  lowest = mover  + 1
            else:
                return all_numbers[first], all_numbers[mover], all_numbers[last]
        if current_triplet_sum < 2020: first += 1
        else:                          last  -= 1




if __name__ == '__main__':
    main()
