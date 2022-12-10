import input


def resolve_rope_bridge():
    input_data = input.parse_day(9)
    print(f'day 9 - part 1 ==> {count_tail_positions(input_data)}')
    #print(f'day 9 - part 2 ==> {input_data}')


def count_tail_positions(input_data):
    H=(0,0)
    T=(0,0)

    array_size = 10

    row = ["."] * array_size
    area = [row.copy() for _ in range(array_size)]

    row_2 = ["."] * array_size
    area_2 = [row_2.copy() for _ in range(array_size)]
    area_2[array_size-3][3] = "#"

    t = [array_size-3, 3]
    h = [array_size-3, 3]
    for line in input_data:
        direction, steps = line.split(" ")[0], int(line.split(" ")[1])
        for number_of_move in range(steps):
            move_head(area, h, direction)
            move_tail(area, t, area_2)

    res = 0
    for x in range(len(area_2)):
        for y in range(len(area_2[0])):
            if area_2[x][y] == "#":
                res += 1
    print_area(area)
    print_area(area_2)
    return res


def move_head(area, h, direction):
    if direction == "R":
        h[1] = h[1] + 1
        area[h[0]][h[1]] = "H"
    if direction == "L":
        h[1] = h[1] - 1
        area[h[0]][h[1]] = "H"
    if direction == "U":
        h[0] = h[0] - 1
        area[h[0]][h[1]] = "H"
    if direction == "D":
        h[0] = h[0] + 1
        area[h[0]][h[1]] = "H"


def move_tail(area, t, area_2):
    if area[t[0]][t[1] + 2] == "H":  # right
        t[1] = t[1] + 1
    if area[t[0]][t[1] - 2] == "H":  # left
        t[1] = t[1] - 1
    if area[t[0] - 2][t[1]] == "H":  # down
        t[0] = t[0] - 1
    if area[t[0] + 2][t[1]] == "H":  # up
        t[0] = t[0] + 1

    if area[t[0] - 2][t[1] + 1] == "H" or area[t[0] - 1][t[1] + 2] == "H":  # right-up
        t[0] = t[0] - 1
        t[1] = t[1] + 1
    if area[t[0] - 2][t[1] - 1] == "H" or area[t[0] - 1][t[1] - 2] == "H":  # left-up
        t[0] = t[0] - 1
        t[1] = t[1] - 1
    if area[t[0] + 2][t[1] - 1] == "H" or area[t[0] + 1][t[1] - 2] == "H":  # left-down
        t[0] = t[0] + 1
        t[1] = t[1] - 1
    if area[t[0] + 2][t[1] + 1] == "H" or area[t[0] + 1][t[1] + 2] == "H":  # right-down
        t[0] = t[0] + 1
        t[1] = t[1] + 1

    area_2[t[0]][t[1]] = "#"
    # print_area(area_2)


def print_area(area):
    for line in area:
        print(line)
    print("--------------------------------------------------")
