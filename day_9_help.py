import input


def day_9():
    head = (0, 0)
    tail = [(0, 0) for _ in range(9)]
    change_vertical = {'L': 0, 'U': -1, 'R': 0, 'D': 1}
    change_horizontal = {'L': -1, 'U': 0, 'R': 1, 'D': 0}
    tail_position_set = {tail[0]}
    tail_position_set_long = {tail[8]}
    lines = input.parse_day(9)
    for line in lines:
        direction, step = line.split()
        for _ in range(int(step)):
            head = (head[0] + change_vertical[direction], head[1] + change_horizontal[direction])
            tail[0] = adjust(head, tail[0])
            for i in range(1, 9):
                tail[i] = adjust(tail[i - 1], tail[i])
            tail_position_set.add(tail[0])
            tail_position_set_long.add(tail[8])

    print(f'day 9 - part 1 ==> {len(tail_position_set)}')
    print(f'day 9 - part 2 ==> {len(tail_position_set_long)}')


def adjust(head, tail):
    dr = (head[0] - tail[0])
    dc = (head[1] - tail[1])
    if abs(dr) <= 1 and abs(dc) <= 1:
        pass
    elif abs(dr) >= 2 and abs(dc) >= 2:
        tail = (head[0] - 1 if tail[0] < head[0] else head[0] + 1, head[1] - 1 if tail[1] < head[1] else head[1] + 1)
    elif abs(dr) >= 2:
        tail = (head[0] - 1 if tail[0] < head[0] else head[0] + 1, head[1])
    elif abs(dc) >= 2:
        tail = (head[0], head[1] - 1 if tail[1] < head[1] else head[1] + 1)
    return tail
