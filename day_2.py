import input


# https://adventofcode.com/2022/day/2
def resolve_rock_paper_scissors():
    input_data = input.parse_day(2)
    scores_table_game_one = {
        "A Y": 2 + 6, "A X": 1 + 3, "A Z": 3 + 0,
        "B Y": 2 + 3, "B X": 1 + 0, "B Z": 3 + 6,
        "C Z": 3 + 3, "C X": 1 + 6, "C Y": 2 + 0
    }
    print(f'day 2 - part 1 ==> {calculate_game(input_data, scores_table_game_one)}')

    scores_table_game_two = {
        "A Y": 1 + 3, "A X": 3 + 0, "A Z": 2 + 6,
        "B Y": 2 + 3, "B X": 1 + 0, "B Z": 3 + 6,
        "C Z": 1 + 6, "C X": 2 + 0, "C Y": 3 + 3
    }
    print(f'day 2 - part 2 ==> {calculate_game(input_data, scores_table_game_two)}')


def calculate_game(input_data, scores_table):
    game_result = 0
    for game in input_data:
        game_result += scores_table.get(game)
    return game_result
