import input


def resolve_tuning_trouble():
    input_data = input.parse_day(6)
    print(f'day 6 - part 1 ==> {find_marker(input_data[0], 4)}')  # 1987
    print(f'day 6 - part 2 ==> {find_marker(input_data[0], 14)}')  # 3059


def find_marker(message, marker_size):
    for i in range(0, len(message) - (marker_size - 1)):
        if len(set(message[i:i + marker_size])) == marker_size:
            return i + marker_size
