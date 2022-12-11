def parse_day(day: int):
    with open(f"day_{day}.input", 'r') as file:
        return [line.strip() for line in file.readlines()]
