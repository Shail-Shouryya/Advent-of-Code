def main():
    with open('puzzle_day_1.txt', 'r', encoding='utf-8') as puzzle_input:
        text = puzzle_input.read()
    part_1_solution = part_one(text)
    print('*' * 80)
    part_2_solution = part_two(text)
    print('*' * 80)
    print(f'Solution to part 1: {part_1_solution}')
    print(f'Solution to part 2: {part_2_solution}')


def part_one(text):
    first, second = find_pair_sum_to_2020(text)
    product = first * second
    print(f'The two numbers that sum to 2020 are: {first}, {second}')
    print (f'The product of these two numbers is: {product}')
    return product


def find_pair_sum_to_2020(text):
    all_numbers = [int(number) for number in text.split()]
    pairs = {}
    for number in all_numbers:
        if number in pairs:
            return number, pairs[number]
        else:
            pairs[2020 - number] = number




def part_two(text):
    return find_triplet_sum_to_2020(text)


def find_triplet_sum_to_2020(text):
    all_numbers = [int(number) for number in text.split()]
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
                first  = all_numbers[first]
                second = all_numbers[mover]
                third  = all_numbers[last]
                product = first * second * third
                print(f'The three numbers that sum to 2020 are: {first}, {second}, {third}')
                print(f'The product of these three numbers is:  {product}')
                return product
        if current_triplet_sum < 2020: first += 1
        else:                          last  -= 1




if __name__ == '__main__':
    main()
