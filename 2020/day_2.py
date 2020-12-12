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


--- Part Two ---
While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
How many passwords are valid according to the new interpretation of the policies?

Answer:
____________
'''
def main():
    text      = read_puzzle_input('puzzle_day_2.txt')
    all_lines = convert_puzzle_text_to_list_of_lines(text)
    print('*' * 80)
    part_1_solution = solve_part_1(all_lines)
    print('*' * 80)
    part_2_solution = solve_part_2(all_lines)
    print('*' * 80)
    print(f'Solution to day 2 part 1: {part_1_solution}')
    print(f'Solution to day 2 part 2: {part_2_solution}')
    print('*' * 80)
    return part_1_solution, part_2_solution




def read_puzzle_input(filename):
    with open(filename, 'r', encoding='utf-8') as puzzle_input:
        return puzzle_input.read()

def convert_puzzle_text_to_list_of_lines(text):
    return text.split('\n')




def parse_line(index, line):
    try:
        requirement, password    = line.split(':')
        requirement              = requirement.strip()
        password                 = password.strip()
        p_range, character       = requirement.split() # split by whitespace (should be one space character)
        first, second = [int(number) for number in p_range.split('-')]
    except ValueError as error_message: # example -> ValueError: not enough values to unpack (expected 2, got 1)
        print(f'Line {index} is improperly formatted. The exact message was:\n{error_message}')
    except Exception as some_other_error:
        print(f'There was an unexpected error when processing line {index}. The exact message was:\n{some_other_error}')
    else:
        return password, character, first, second
    # if we get here, this means there was some error,
    # so we return the falsy value for the expected data type
    # https://docs.python.org/3/library/stdtypes.html
    return ('', '', 0, 0)




def solve_part_1(all_lines):
    valid_passwords = 0
    for index, line in enumerate(all_lines):
        is_valid = check_password_for_validity(index, line)
        if is_valid:
            valid_passwords += 1
    print(f'There are {valid_passwords} valid passwords in this file based on the independent password requirement for each password.')
    return valid_passwords

def check_password_for_validity(index, line):
    password, character, least, greatest = parse_line(index, line)
    # python checks for falsy values when evaluating conditionals
    # this is faster than performing
    # password == ''
    if not password:
        return False
    actual_count_of_character  = password.count(character)
    print(f'Password {index:>4} requires "{character}" to occur {least:>3} to {greatest:>3} times. Actual count: {actual_count_of_character}')
    return least <= actual_count_of_character <= greatest




def solve_part_2(all_lines):
    valid_passwords = 0
    for index, line in enumerate(all_lines):
        is_valid = check_password_for_validity_using_official_policy(index, line)
        if is_valid:
            valid_passwords += 1
    print(f'There are {valid_passwords} valid passwords in this file based on the independent password requirement for each password using the OFFICIAL policy.')
    return valid_passwords


def check_password_for_validity_using_official_policy(index, line):
    password, character, position_1, position_2 = parse_line(index, line)
    # python checks for falsy values when evaluating conditionals
    # this is faster than performing
    # password == ''
    if not password:
        return False
    position_1_is_valid = False
    position_2_is_valid = False
    password_length = len(password)
    if 0 <= position_1 - 1 < password_length: position_1_is_valid = password[position_1 - 1] == character
    if 0 <= position_2 - 1 < password_length: position_2_is_valid = password[position_2 - 1] == character
    # ^ is the XOR operator, and the result is caluclated by
    # flipping the bits at any position where the two arguments have a different value
    # since position_1_is_valid and position_2_is_valid can only have the value of
    # True or False in this scenario, the possible bit values for the arguments can only be
    # either 0 (False) or 1 (True)
    # 1 ^ 1 -> 0
    # 1 ^ 0 -> 1
    # 0 ^ 1 -> 1
    # 0 ^ 0 -> 0
    # since we want to determine if the password has the designated character appear
    # only in ONE of the designated positions, performing
    # position_1_is_valid XOR position_2_is_valid
    # gives us exactly what we want
    is_valid = position_1_is_valid ^ position_2_is_valid
    print(f'Password {index:>4} requires "{character}" to occur at either position {position_1:>3} OR {position_2:>3} (but not at both nor neither positions): This is {is_valid}')
    return is_valid




if __name__ == '__main__':
    main()
