import day_1

def main():
    part_1, part_2    = day_1.main()
    part_1_is_correct = part_1 == 388075
    part_2_is_correct = part_2 == 293450526
    return f'Day 1 part 1 answer is correct: {part_1_is_correct}\nDay 1 part 2 answer is correct: {part_2_is_correct}'

if __name__ == '__main__':
    print(main())
