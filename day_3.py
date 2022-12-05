import input


# https://adventofcode.com/2022/day/3
def resolve_rucksack_reorganization():
    input_data = input.parse_day(3)
    print(f'day 3 - part 1 ==> {sum(find_item_index(input_data))}')
    print(f'day 3 - part 2 ==> {sum(find_badge_index(input_data))}')


def find_item_index(input_data):
    index_list = []
    for items in input_data:
        first_compartment = set(items[:int(len(items) / 2)])
        second_compartment = set(items[int(len(items) / 2):])
        intersection = first_compartment.intersection(second_compartment)

        character = list(intersection.pop())[0]
        index = ord(character)

        if ord('a') <= index <= ord('z'):
            index_list.append(index - 96)
        else:
            index_list.append(index - 38)
    return index_list


def find_badge_index(input_data):
    grouped_data = [input_data[n:n + 3] for n in range(0, len(input_data), 3)]
    index_list = []
    for items in grouped_data:
        intersection = set(items[0]).intersection(items[1]).intersection(items[2])
        character = list(intersection.pop())[0]
        index = ord(character)

        if ord('a') <= index <= ord('z'):
            index_list.append(index - 96)
        else:
            index_list.append(index - 38)
    return index_list
