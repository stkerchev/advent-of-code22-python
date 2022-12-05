import input


# https://adventofcode.com/2022/day/5
def resolve_supply_stacks():
    input_data = input.parse_day(5)
    print(f'day 5 - part 1 ==> {move_crates(parce_commands(input_data), parce_stacks(input_data))}')  # TGWSMRBPN
    print(f'day 5 - part 2 ==> {move_crates_9001(parce_commands(input_data), parce_stacks(input_data))}')  # TZLTLWRNF


def parce_stacks(input_data):
    stacks_data = []
    for line in input_data:
        if line == "":
            break
        stacks_data.append(line)

    number_of_stacks = int(stacks_data.pop().split(" ").pop())
    stacks_data.reverse()

    stacks = [[]]
    for row in stacks_data:
        for column_number in range(1, number_of_stacks + 1):
            if len(stacks) <= column_number:
                stacks.append([])
            current = stacks[column_number]
            # 1->1 2->5 3->9 4->13
            parsed_item = column_number * 4 - 3
            if len(row) >= parsed_item:
                item = row[parsed_item]
                if item != ' ':
                    current.append(item)
    return stacks


def parce_commands(input_data):
    commands = []
    for line in input_data:
        if line != "" and line.startswith('m'):
            c = line.split(" ")
            commands.append([int(c[1]), int(c[3]), int(c[5])])
    return commands


def move_crates(commands, stacks):
    for command in commands:
        move_from = stacks[command[1]]
        move_to = stacks[command[2]]

        # performs the movement
        for i in range(command[0]):
            item = move_from.pop()
            move_to.append(item)

    return build_result(stacks)


def move_crates_9001(commands, stacks):
    for command in commands:
        move_from = stacks[command[1]]
        move_to = stacks[command[2]]
        crates_to_move = []

        # performs the movement
        for i in range(command[0]):
            item = move_from.pop()
            crates_to_move.append(item)
        crates_to_move.reverse()
        for crates in crates_to_move:
            move_to.append(crates)

    return build_result(stacks)


def build_result(stacks):
    result = ""
    for stack in stacks:
        if len(stack) > 0:
            result += stack.pop()
    return result
