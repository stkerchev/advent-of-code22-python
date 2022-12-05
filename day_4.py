import input


# https://adventofcode.com/2022/day/4
def resolve_camp_cleanup():
    input_data = input.parse_day(4)
    print(f'day 4 - part 1 ==> {count_fully_contains_section(input_data)}')
    print(f'day 4 - part 2 ==> {count_intersection(input_data)}')


def count_fully_contains_section(input_data):
    counter = 0
    for line in input_data:
        one, two = line.split(',')
        if is_a_wrapper(one, two):
            counter += 1
        elif is_a_wrapper(two, one):
            counter += 1

    return counter


def is_a_wrapper(wrapper, target):
    ws, we = wrapper.split('-')
    ts, te = target.split('-')
    wrapper_start, wrapper_end, target_start, target_end = [int(x) for x in [ws, we, ts, te]]
    return wrapper_start <= target_start and wrapper_end >= target_end


def count_intersection(input_data):
    counter = 0
    for line in input_data:
        one, two = line.split(',')
        s1, e1 = one.split('-')
        s2, e2 = two.split('-')
        s1, e1, s2, e2 = [int(x) for x in [s1, e1, s2, e2]]

        first_set = set(range(s1, e1 + 1))
        second_set = set(range(s2, e2 + 1))

        if len(first_set.intersection(second_set)) > 0:
            counter += 1

    return counter
