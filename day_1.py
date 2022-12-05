# https://adventofcode.com/2022/day/1
def resolve_calorie_counting():
    input_data = parse_input()
    result = calories_by_elf(input_data)
    result.sort()
    print(f'day 1 - part 1 ==> {result[-1]}')
    print(f'day 1 - part 2 ==> {result[-1] + result[-2] + result[-3]}')


def calories_by_elf(input_list):
    all_sum = []
    current = 0
    for value in input_list:
        if value.isnumeric():
            current += int(value)
        else:
            all_sum.append(current)
            current = 0
    all_sum.append(current)
    return all_sum


def parse_input():
    with open("day_1.input", 'r') as file:
        return [line.strip() for line in file.readlines()]
