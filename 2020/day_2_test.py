import day_2

def main():
    part_1, part_2 = day_2.main()
    part_1_is_correct = part_1 == 655
    part_2_is_correct = part_2 == 673
    return f'Day 2 part 1 answer is correct: {part_1_is_correct}\nDay 2 part 2 answer is correct: {part_2_is_correct}'

if __name__ == '__main__':
    print(main())
