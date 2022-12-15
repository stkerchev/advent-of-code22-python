import input


#  https://adventofcode.com/2022/day/15
def resolve():
    input_data = input.parse_day(15)
    print(f'day 15 - part 1 ==> {calculate_covered(input_data)}')  # 5832528
    print(f'day 15 - part 2 ==> {find_beacon(input_data)}')  # 13360899249595


def calculate_covered(input_data):
    sensors = [line_to_sensor(line) for line in input_data]
    res = set()
    for sensor in sensors:
        res.update(sensor.covered_coordinates_by_y(2000000))
    return len(set([sensor.covered_coordinates_by_y(2000000) for sensor in sensors]))


def find_beacon(input_data):
    sensors = [line_to_sensor(line) for line in input_data]
    res = set()
    for sensor in sensors:
        res.update(sensor.get_border())
        print(len(res))
    for point in res:
        if is_not_covered(point, sensors):
            return point[0] * 4000000 + point[1]


def is_not_covered(point, sensors):
    for s in sensors:
        if s.is_covered(point):
            return False
    return True


def line_to_sensor(line: str):
    x, y, xx, yy = [int(value) for value in
                    line.replace("Sensor at x=", "").replace(", y=", "|")
                    .replace(": closest beacon is at x=", "|").split("|")]
    return Sensor((x, y,), (xx, yy))


class Sensor:
    def __init__(self, sensor_position: tuple, beacon_position: tuple):
        self.sensor_point = sensor_position
        self.beacon_point = beacon_position
        self.coverage = self._calculate_coverage()

    def _calculate_coverage(self) -> int:
        s_x, s_y = self.sensor_point[0], self.sensor_point[1]
        b_x, b_y = self.beacon_point[0], self.beacon_point[1]
        distance_x = s_x - b_x if s_x > b_x else b_x - s_x
        distance_y = s_y - b_y if s_y > b_y else b_y - s_y
        return distance_x + distance_y

    def covered_coordinates_by_y(self, y: int) -> set:
        s_y = self.sensor_point[1]
        distance_y = s_y - y if s_y > y else y - s_y
        if distance_y > self.coverage:
            return set()
        x_values = self.coverage - distance_y
        internal = [(x, y,) for x in range(self.sensor_point[0] - x_values, self.sensor_point[0] + x_values, +1)]
        return set(internal)

    def is_covered(self, point) -> bool:
        x = point[0]
        y = point[1]
        s_x, s_y = self.sensor_point[0], self.sensor_point[1]
        distance_x = s_x - x if s_x > x else x - s_x
        distance_y = s_y - y if s_y > y else y - s_y
        return self.coverage >= distance_x + distance_y

    def get_border(self) -> set:
        x = self.sensor_point[0]
        y = self.sensor_point[1]
        y_d = d = self.coverage + 1
        x_d = 0
        res = set()
        change = [(1, -1), (-1, -1), (-1, 1), (1, 1)]
        for i in range(4):
            for _ in range(d):
                if 0 <= x + x_d <= 4000000 and 0 <= y + y_d <= 4000000:
                    res.add((x + x_d, y + y_d,))
                x_d += change[i][0]
                y_d += change[i][1]
        return res
