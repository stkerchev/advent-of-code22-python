import input


#  https://adventofcode.com/2022/day/14
def resolve():
    input_data = input.parse_day(14)
    area = 700
    cave_map = [['.'] * 200 for x in range(area)]
    x = 500
    y = 0
    cave_map[x][y] = "+"
    highest_y_list = []
    for input_line in input_data:
        lines = input_line.split(" -> ")
        for index in range(len(lines) - 1):
            highest_y_list.append(draw_line(lines[index], lines[index + 1], cave_map))

    print(f'day 14 - part 1 ==> {calculate_sand_fall(x, y, cave_map)}')  # 715

    highest_y_list.sort()
    highest_y = highest_y_list[-1]

    for el in range(area):
        cave_map[el][highest_y + 2] = "#"
    print(f'day 14 - part 2 ==> {calculate_sand_fall(x, y, cave_map)}')  # 25248


def calculate_sand_fall(x, y, cave_map):
    bags = []
    while True:
        result = sand_fall(x, y, cave_map)
        if result is None:
            break
        else:
            bags.append(result)
    return len(bags)


def sand_fall(x, y, cave_map):
    # one sand failing
    while True:
        if cave_map[x][y] == 'O' or y == len(cave_map[0])-2:
            return
        if cave_map[x][y + 1] != '.':
            if cave_map[x - 1][y + 1] == '.':
                return sand_fall(x - 1, y, cave_map)
            elif cave_map[x + 1][y + 1] == '.':
                return sand_fall(x + 1, y, cave_map)
            else:
                cave_map[x][y] = 'O'
                return x, y
        else:
            y += 1


def draw_line(start, end, cave_map):
    start_x, start_y = start.split(",")
    end_x, end_y = end.split(",")
    start_x, start_y, end_x, end_y = [int(value) for value in [start_x, start_y, end_x, end_y]]
    if start_x == end_x:
        draw_vertical_line(start_x, start_y, end_y, cave_map)
    else:
        draw_horizontal_line(start_y, start_x, end_x, cave_map)

    return start_y if start_y > end_y else end_y


def draw_vertical_line(x, start_y, end_y, cave_map):
    max_v = start_y if start_y > end_y else end_y
    min_v = start_y if start_y < end_y else end_y
    for i in range((max_v - min_v) + 1):
        cave_map[x][i + min_v] = "#"


def draw_horizontal_line(y, start_x, end_x, cave_map):
    max_h = start_x if start_x > end_x else end_x
    min_h = start_x if start_x < end_x else end_x
    for i in range((max_h - min_h) + 1):
        cave_map[i + min_h][y] = "#"
