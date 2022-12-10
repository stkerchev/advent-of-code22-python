import input


#  https://adventofcode.com/2022/day/8
def resolve_treetop_tree_house():
    input_data = input.parse_day(8)
    print(f'day 8 - part 1 ==> {count_visible(input_data)}')
    print(f'day 8 - part 2 ==> {scenic_score(input_data)}')


def count_visible(input_data):
    visible = 0
    for r in range(len(input_data)):
        row = input_data[r]
        for c in range(len(row)):
            if is_visible(r, c, input_data):
                visible += 1
    return visible


def is_visible(r, c, input_data):
    return is_visible_left(r, c, input_data) or is_visible_right(r, c, input_data) \
        or is_visible_up(r, c, input_data) or is_visible_down(r, c, input_data)


def is_visible_left(r, c, input_data):
    if c == 0:
        return True
    else:
        tree_h = int(input_data[r][c])
        for left in range(c - 1, -1, -1):
            if int(input_data[r][left]) >= tree_h:
                return False
    return True


def is_visible_up(r, c, input_data):
    if r == 0:
        return True
    else:
        tree_h = int(input_data[r][c])
        for up in range(r - 1, -1, -1):
            if int(input_data[up][c]) >= tree_h:
                return False
    return True


def is_visible_right(r, c, input_data):
    if c == len(input_data[r]):
        return True
    else:
        tree_h = int(input_data[r][c])
        for right in range(c + 1, len(input_data[0])):
            if int(input_data[r][right]) >= tree_h:
                return False
    return True


def is_visible_down(r, c, input_data):
    if r == len(input_data):
        return True
    else:
        tree_h = int(input_data[r][c])
        for down in range(r + 1, len(input_data)):
            if int(input_data[down][c]) >= tree_h:
                return False
    return True


def scenic_score(input_data):
    score = []
    for r in range(len(input_data)):
        row = input_data[r]
        for c in range(len(row)):
            s = viewing_distance_right(r, c, input_data) * viewing_distance_left(r, c, input_data) \
                * viewing_distance_up(r, c, input_data) * viewing_distance_down(r, c, input_data)
            score.append(s)

    score.sort()
    return score[-1]


def viewing_distance_left(r, c, input_data):
    if c == 0:
        return 0
    else:
        tree_h = int(input_data[r][c])
        score = 0
        for left in range(c - 1, -1, -1):
            if int(input_data[r][left]) < tree_h:
                score += 1
            else:
                score += 1
                break
    return score


def viewing_distance_up(r, c, input_data):
    if r == 0:
        return 0
    else:
        tree_h = int(input_data[r][c])
        score = 0
        for up in range(r - 1, -1, -1):
            if int(input_data[up][c]) < tree_h:
                score += 1
            else:
                score += 1
                break
    return score


def viewing_distance_right(r, c, input_data):
    if c == len(input_data[r]) - 1:
        return 0
    else:
        tree_h = int(input_data[r][c])
        score = 0
        for right in range(c + 1, len(input_data[0])):
            if int(input_data[r][right]) < tree_h:
                score += 1
            else:
                score += 1
                break
    return score


def viewing_distance_down(r, c, input_data):
    if r == len(input_data) - 1:
        return 0
    else:
        tree_h = int(input_data[r][c])
        score = 0
        for step in range(r + 1, len(input_data)):
            if int(input_data[step][c]) < tree_h:
                score += 1
            else:
                score += 1
                break
    return score
