import math
from collections import deque


#  https://adventofcode.com/2022/day/11
def resolve_monkey_in_the_middle():
    grouped_input = parse_day()
    print(f'day 11 - part 1 ==> {resolve_part_one(grouped_input)}')  # 10605
    print(f'day 11 - part 2 ==> {resolve_part_two(grouped_input)}')  # 23612457316


def parse_day():
    with open(f"day_11.input", 'r') as file:
        return [[line.strip() for line in text.split("\n")] for text in file.read().split("\n\n")]


def resolve_part_one(grouped_input):
    monkeys = [Monkey(data) for data in grouped_input]
    for round_ in range(20):
        for monkey in monkeys:
            monkey.is_your_turn(monkeys)
    return calculate_result(monkeys)


def resolve_part_two(grouped_input):
    worry_reducer = 1
    for divisible_by in [int(group[3].split(' ')[-1]) for group in grouped_input]:
        worry_reducer *= (worry_reducer * divisible_by) \
                         // math.gcd(worry_reducer, divisible_by)  # Greatest Common Divisor
    monkeys = [Monkey(data, worry_level_divider=1, worry_reducer=worry_reducer) for data in grouped_input]
    for round_ in range(10000):
        for monkey in monkeys:
            monkey.is_your_turn(monkeys)
    return calculate_result(monkeys)


def calculate_result(monkeys):
    processed_counter = [m.number_of_processed for m in monkeys]
    processed_counter.sort()
    return processed_counter[-1] * processed_counter[-2]


class Monkey:

    def __init__(self, monkey_behavior: list[str], worry_level_divider=3, worry_reducer=1):
        self.name = monkey_behavior[0].lower().replace(':', '')
        self.items = deque([int(x) for x in monkey_behavior[1].replace('Starting items: ', '').split(', ')])
        self.operation = monkey_behavior[2].split('= ')[-1]
        self.divisible = int(monkey_behavior[3].split(' ')[-1])
        self.on_positive = monkey_behavior[4].split(': ')[-1].replace('throw to ', '')
        self.on_negative = monkey_behavior[5].split(': ')[-1].replace('throw to ', '')
        self.worry_level_divider = worry_level_divider
        self.worry_reducer = worry_reducer
        self.number_of_processed = 0

    def is_your_turn(self, monkeys: list):
        if len(self.items) > 0:
            for _ in range(len(self.items)):
                self.number_of_processed += 1
                item = self._inspect_item(self.items.popleft())
                self._throw_item(item, monkeys)

    def receive_item(self, item: int):
        self.items.append(item)

    def get_number_of_processed(self):
        return self.number_of_processed

    def _inspect_item(self, item: int):
        if self.worry_reducer > 1:
            item = item % self.worry_reducer
        if 'old * old' in self.operation:
            return item * item // self.worry_level_divider
        if '*' in self.operation:
            return item * int(self.operation.split(' ')[-1]) // self.worry_level_divider
        return (item + int(self.operation.split(' ')[-1])) // self.worry_level_divider

    def _throw_item(self, item: int, monkeys: list):
        if item % self.divisible == 0:
            receiver = next((m for m in monkeys if m.name == self.on_positive), None)
            receiver.receive_item(item)
        else:
            receiver = next((m for m in monkeys if m.name == self.on_negative), None)
            receiver.receive_item(item)
