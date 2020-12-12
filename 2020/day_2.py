'''
--- Day 2: Password Philosophy ---
Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?

To begin, get your puzzle input.

Answer:
____________
'''
def main():
    text      = read_puzzle_input('puzzle_day_2.txt')
    all_lines = convert_puzzle_text_to_list_of_lines(text)
    print('*' * 80)
    part_1_solution = solve_part_1(all_lines)
    print('*' * 80)
    print(f'Solution to day 2 part 1: {part_1_solution}')
    print('*' * 80)




def read_puzzle_input(filename):
    with open(filename, 'r', encoding='utf-8') as puzzle_input:
        return puzzle_input.read()

def convert_puzzle_text_to_list_of_lines(text):
    return text.split('\n')




def solve_part_1(all_lines):
    valid_passwords = 0
    for index, line in enumerate(all_lines):
        is_valid = check_password_for_validity(index, line)
        if is_valid:
            valid_passwords += 1
    print(f'There are {valid_passwords} valid passwords in this file based on the independent password requirement for each password.')
    return valid_passwords

def check_password_for_validity(index, line):
    try:
        requirement, password      = line.split(':')
        requirement                = requirement.strip()
        password                   = password.strip()
        number_of_times, character = requirement.split() # split by whitespace (should be one space character)
        least, greatest            = [int(number) for number in number_of_times.split('-')]
    except ValueError as error_message: # example -> ValueError: not enough values to unpack (expected 2, got 1)
        print(f'Line {index} is improperly formatted. The exact message was:\n{error_message}')
    except Exception as some_other_error:
        print(f'There was an unexpected error when processing line {index}. The exact message was:\n{some_other_error}')
    else:
        actual_count_of_character  = password.count(character)
        print(f'Password {index:>4} requires "{character}" to occur {least:>3} to {greatest:>3} times. Actual count: {actual_count_of_character}')
        if least <= actual_count_of_character <= greatest:
            return True
    return False



if __name__ == '__main__':
    main()
