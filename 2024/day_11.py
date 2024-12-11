'''
--- Day 11: Plutonian Pebbles ---
The ancient civilization on Pluto was known for its ability to manipulate spacetime, and while the Historians explore their infinite corridors, you've noticed a strange set of physics-defying stones.

At first glance, they seem like normal stones: they're arranged in a perfectly straight line, and each stone has a number engraved on it.

The strange part is that every time you blink, the stones change.

Sometimes, the number engraved on a stone changes. Other times, a stone might split in two, causing all the other stones to shift over a bit to make room in their perfectly straight line.

As you observe them for a while, you find that the stones have a consistent behavior. Every time you blink, the stones each simultaneously change according to the first applicable rule in this list:

If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
No matter how the stones change, their order is preserved, and they stay on their perfectly straight line.

How will the stones evolve if you keep blinking at them? You take a note of the number engraved on each stone in the line (your puzzle input).

If you have an arrangement of five stones engraved with the numbers 0 1 10 99 999 and you blink once, the stones transform as follows:

The first stone, 0, becomes a stone marked 1.
The second stone, 1, is multiplied by 2024 to become 2024.
The third stone, 10, is split into a stone marked 1 followed by a stone marked 0.
The fourth stone, 99, is split into two stones marked 9.
The fifth stone, 999, is replaced by a stone marked 2021976.
So, after blinking once, your five stones would become an arrangement of seven stones engraved with the numbers 1 2024 1 0 9 9 2021976.

Here is a longer example:

Initial arrangement:
125 17

After 1 blink:
253000 1 7

After 2 blinks:
253 0 2024 14168

After 3 blinks:
512072 1 20 24 28676032

After 4 blinks:
512 72 2024 2 0 2 4 2867 6032

After 5 blinks:
1036288 7 2 20 24 4048 1 4048 8096 28 67 60 32

After 6 blinks:
2097446912 14168 4048 2 0 2 4 40 48 2024 40 48 80 96 2 8 6 7 6 0 3 2
In this example, after blinking six times, you would have 22 stones. After blinking 25 times, you would have 55312 stones!

Consider the arrangement of stones in front of you. How many stones will you have after blinking 25 times?

--- Part Two ---
The Historians sure are taking a long time. To be fair, the infinite corridors are very large.

How many stones would you have after blinking a total of 75 times?
'''



def main(
    file_location: str,
) -> tuple[int, int]:
    stones     = read_puzzle_input(file_location)
    print('*' * 80)
    part_1_solution = solve_part_1(stones)
    print('*' * 80)
    part_2_solution = solve_part_2(stones)
    print('*' * 80)
    print(f'Solution to day 11 part 1: {part_1_solution}')
    print(f'Solution to day 11 part 2: {part_2_solution}')
    print('*' * 80)
    return (part_1_solution, part_2_solution)


def read_puzzle_input(
    file_location: str,
) -> list[int]:
    stones = []
    with open(file=file_location, mode='r', buffering=-1, encoding='utf-8', newline=None) as file:
        for stone in file.read().split():
            stones.append(int(stone))
    print(stones)
    return stones


def solve_part_1(
    stones: list[int],
) -> int:
    number_of_stones_after_25_blinks = transform_stone_line(stones, 25)
    print(f'There are {number_of_stones_after_25_blinks} stones after 25 blinks')
    return number_of_stones_after_25_blinks


def transform_stone_line(
    stones: list[int],
    blinks: int
) -> int:
    for _ in range(blinks):
        updated_line = []
        for stone in stones:
            if stone == 0: updated_line.append(1)
            elif len(str(stone)) % 2 == 0:
                stone_s = str(stone)
                total = len(stone_s)
                left, right = stone_s[:total//2], stone_s[total//2:]
                updated_line.append(int(left))
                updated_line.append(int(right))
            else:
                updated_line.append(stone * 2024)
        stones = updated_line
    return len(updated_line)


def solve_part_2(
    stones: list[int],
) -> int:
    blinks = 75
    number_of_stones_after_75_blinks = transform_stone_line_still_too_slow(stones, blinks)
    return number_of_stones_after_75_blinks


def transform_stone_line_still_too_slow(
    stones: list[int],
    blinks: int
) -> int:
    total_stones = 0
    for start in stones:
        current = [start]
        for iteration in range(blinks):
            updated_line = []
            for stone in current:
                if stone == 0: updated_line.append(1)
                elif len(str(stone)) % 2 == 0:
                    stone_s = str(stone)
                    total = len(stone_s)
                    left, right = stone_s[:total//2], stone_s[total//2:]
                    updated_line.append(int(left))
                    updated_line.append(int(right))
                else:
                    updated_line.append(stone * 2024)
            current = updated_line
            # print(start, iteration, len(current), current)
        total_stones += len(updated_line)
        # print(stone, total_stones)
    return total_stones


if __name__ == '__main__':
    main('day_11.txt')
