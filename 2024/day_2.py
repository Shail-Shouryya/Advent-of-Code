'''
--- Day 2: Red-Nosed Reports ---
Fortunately, the first location The Historians want to search isn't a long walk from the Chief Historian's office.

While the Red-Nosed Reindeer nuclear fusion/fission plant appears to contain no sign of the Chief Historian, the engineers there run up to you as soon as they see you. Apparently, they still talk about the time Rudolph was saved through molecular synthesis from a single electron.

They're quick to add that - since you're already here - they'd really appreciate your help analyzing some unusual data from the Red-Nosed reactor. You turn to check if The Historians are waiting for you, but they seem to have already divided into groups that are currently searching every corner of the facility. You offer to help with the unusual data.

The unusual data (your puzzle input) consists of many reports, one report per line. Each report is a list of numbers called levels that are separated by spaces. For example:

7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
This example data contains six reports each containing five levels.

The engineers are trying to figure out which reports are safe. The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the following are true:

The levels are either all increasing or all decreasing.
Any two adjacent levels differ by at least one and at most three.
In the example above, the reports can be found safe or unsafe by checking those rules:

7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.
So, in this example, 2 reports are safe.

Analyze the unusual data from the engineers. How many reports are safe?

--- Part Two ---
The engineers are surprised by the low number of safe reports until they realize they forgot to tell you about the Problem Dampener.

The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single bad level in what would otherwise be a safe report. It's like the bad level never happened!

Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.

More of the above example's reports are now safe:

7 6 4 2 1: Safe without removing any level.
1 2 7 8 9: Unsafe regardless of which level is removed.
9 7 6 2 1: Unsafe regardless of which level is removed.
1 3 2 4 5: Safe by removing the second level, 3.
8 6 4 4 1: Safe by removing the third level, 4.
1 3 6 7 9: Safe without removing any level.
Thanks to the Problem Dampener, 4 reports are actually safe!

Update your analysis by handling situations where the Problem Dampener can remove a single level from unsafe reports. How many reports are now safe?
'''


def main(
    file_location: str,
) -> tuple[int, int]:
    reports         = read_puzzle_input(file_location)
    print('*' * 80)
    part_1_solution = solve_part_1(reports)
    print('*' * 80)
    part_2_solution = solve_part_2(reports)
    print('*' * 80)
    print(f'Solution to day 2 part 1: {part_1_solution}')
    print(f'Solution to day 2 part 2: {part_2_solution}')
    print('*' * 80)
    return (part_1_solution, part_2_solution)


def read_puzzle_input(
    file_location: str,
) -> list[list[int]]:
    reports = []
    with open(file=file_location, mode='r', buffering=-1, encoding='utf-8', newline=None) as file:
        for line in file:
            levels = line.split()
            reports.append([int(level) for level in levels])
    return reports


def solve_part_1(
    reports: list[list[int]],
) -> int:
    safe_reports = 0
    for count, report in enumerate(reports, 1):
        safe_reports += report_is_safe(report)
    print(f'The number of safe reports from {count} reports is: {safe_reports}')
    return safe_reports


def report_is_safe(
    report: list[int],
    absolute_difference: int = 3,
) -> int:
    is_safe  = 1
    previous = report[0]                   # initialize to first value of list
    change   = (report[1] - report[0]) > 0 # all changes must be either positive or negative
    for index in range(1, len(report)):
        level          = report[index]
        current_change = level - previous
        if (
            abs(current_change) > absolute_difference or # change is greater than allowed difference
            (current_change > 0) != change            or # change is not consistently montonically increasing/decreasing
            current_change == 0                          # there is no change
        ):
            is_safe = 0
            break
        previous = level
    return is_safe


def solve_part_2(
    reports: list[list[int]],
) -> int:
    safe_reports = 0
    for count, report in enumerate(reports, 1):
        already_safe = report_is_safe(report)
        if already_safe:
            safe_reports += 1
        else:
            safe_reports += report_is_safe_after_dampening(report)
    print(f'The number of safe reports from {count} reports after dampening is: {safe_reports}')
    return safe_reports


def report_is_safe_after_dampening(
    report: list[int],
    absolute_difference: int = 3,
) -> int:
    levels = len(report)
    safe_after_dampening = 0
    for index in range(levels):
        safe_after_dampening = report_is_safe(
            report[:index]   # all levels up to but excluding index level
            +
            report[index+1:] # all levels after index level
            )
        if safe_after_dampening:
            break
    return safe_after_dampening


if __name__ == '__main__':
    main('day_2.txt')
