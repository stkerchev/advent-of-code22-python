import input
from functools import reduce


# https://adventofcode.com/2022/day/10
def resolve_cathode_ray_tube():
    input_data = input.parse_day(10)
    calculate(input_data)


def calculate(input_data):
    signal_strengths = []
    image = "." * 240
    check_point = 20
    value = 1
    skip_one_cycle = True
    value_correction, line_index = 0, 0
    for cycle in range(1, len(input_data) * 2):
        if line_index > len(input_data) - 1:
            break
        # calculate signal strength
        if cycle == check_point:
            check_point += 40
            signal_strengths.append(cycle * value)

        # render image
        current_index = 40 if cycle % 40 == 0 else cycle % 40
        if value <= current_index <= value + 2:
            image = image[:cycle - 1] + "#" + image[cycle:]  # draw pixel

        line = input_data[line_index]
        if line == "noop":
            line_index += 1
            continue
        if skip_one_cycle:
            skip_one_cycle = False
            value_correction = int(line.split(" ")[1])
        else:
            skip_one_cycle = True
            value += value_correction
            value_correction = 0
            line_index += 1
    print(f'day 10 - part 1 ==> {reduce((lambda x, y: x + y), signal_strengths)}')  # 14760
    print(f'day 10 - part 2 ==> ')
    print(image[0:40])
    print(image[40:80])
    print(image[80:120])
    print(image[120:160])
    print(image[160:200])
    print(image[200:240])
