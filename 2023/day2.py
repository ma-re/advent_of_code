# 12 red cubes, 13 green cubes, and 14 blue cubes
import re
from functions import get_data


def find_regex_pattern(games: list) -> list:
    matching_red = re.findall("[0-9]+\s[r]", games[0])
    matching_green = re.findall("[0-9]+\s[g]", games[0])
    matching_blue = re.findall("[0-9]+\s[b]", games[0])
    return matching_red, matching_green, matching_blue

# Part 1
def validate_game(game: str):
    id = game.split(':')[0].strip('Game ')
    games = game.split(': ')[1:]
    red, green, blue = find_regex_pattern(games)
    # Check for impossible games
    red_impossible = [int(x.strip(' r')) for x in red if int(x.strip(' r')) > 12]
    green_impossible = [int(x.strip(' g')) for x in green if int(x.strip(' g')) > 13]
    blue_impossible = [int(x.strip(' b')) for x in blue if int(x.strip(' b')) > 14]
    # Return id of possible games
    if len(red_impossible) == 0 and len(green_impossible) == 0 and len(blue_impossible) == 0:
        return int(id)
    else: 
        return 0

# Part 2
def validate_min_cubes(game):
    games = game.split(': ')[1:]
    red, green, blue = find_regex_pattern(games)
    # Check for max number of cubes needed per game
    max_red = max([int(x.strip(' r')) for x in red])
    max_green = max([int(x.strip(' g')) for x in green])
    max_blue = max([int(x.strip(' b')) for x in blue])
    # Return "power" of the game
    return max_red * max_blue * max_green


# Return results
def calculate_results(data):
    sum_id = 0
    power_cubes = 0
    for game in data:
        sum_id += validate_game(game)
        power_cubes += validate_min_cubes(game)
    return sum_id, power_cubes


data = get_data("data/day2.txt")
print(calculate_results(data))

