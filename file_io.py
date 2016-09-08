# utils.py
# lexninja text-adventure game - Brett Fraley - 2016


import os 
import lexninja

def changeto_saved_dir():
    if os.chdir('saved_games'):
        return True
    else:
        return False

# Accept an instance of game and write data to game file.

def save_game(game_in, filename):
    state = game_in.state
    city = game_in.city
    ninja = game_in.ninja
    badguys = game_in.badguys
    
    # State attributes.
    state_line = "$state"
    state_line += "\n" + str(state.paused)
    state_line += "\n" + str(state.saved)
    state_line += "\n" + str(state.menu)
    
    # City.Building attributes.
    city_line = ""
    city_line += "$city"

    for building in city.blocks:

        city_line += '\n$B'
        city_line += str(building.has_health) + ''
        city_line += str(building.has_badguy) + ' '
        city_line += str(building.has_goldensword) + ' '
        city_line += str(building.visited) + ' '

    # Ninja attributes.

    ninja_line = "\n$ninja"
    ninja_line += '\n' + str(ninja.health)
    ninja_line += '\n' + str(ninja.weapon)
    ninja_line += '\n' + str(ninja.block_location)
    ninja_line += '\n' + str(ninja.inside_building)
    ninja_line += '\n' + str(ninja.is_blocking)
    ninja_line += '\n' + str(ninja.under_attack_on)
    ninja_line += '\n' + str(ninja.win_game)
    ninja_line += '\n' + str(ninja.beat_boss)

    # Badguy attributes.

    badguy_line = "\n$badguys"

    for guy in badguys:
        badguy_line += "\n $BGUY"
        badguy_line += "\n" + str(guy.health)
        badguy_line += "\n" + str(guy.is_boss)


    file = open(filename, 'w')
    file.write(state_line)
    file.write(city_line)
    file.write(ninja_line)
    file.write(badguy_line)
    file.close()

# -----------------------------------------------

def load_game(filename):
    file = open(filename, 'r')
    file_data = file.read()
    file.close()

    return file_data.split('\n') 


def get_game_data(game_data):
    game_out = lexninja.Game()

    line = 0
    
    # Get game data delimiter indices. 
    state_index = game_data.index('$state')
    city_index = game_data.index('$city')
    ninja_index = game_data.index('$ninja')
    badguys_index = game_data.index('$badguys')

    # Read and assign game.state values from game data file.
    line = state_index
    game_out.state.paused = bool(game_data[line + 1])
    game_out.state.saved = bool(game_data[line + 2])
    game_out.state.saved = bool(game_data[line + 3])
    
    # Read and assign game.state values from game data file.
    bstart = city_index + 1
    i = 0

    while i < 9:
        health = bstart + 1
        badguy = bstart + 2
        sword = bstart + 3
        visited = bstart + 4

        game_out.city.blocks[i].has_health = str(game_data[health])
        game_out.city.blocks[i].has_badguy = str(game_data[badguy])
        game_out.city.blocks[i].has_goldensword = str(game_data[sword])
        game_out.city.blocks[i].has_visited = str(game_data[visited])

        bstart = bstart + 5
        i += 1

    # Read and assign game.ninja values from game data file.
    line = ninja_index

    game_out.ninja.city = game_out.city
    game_out.ninja.health = str(game_data[line + 1])
    game_out.ninja.weapon = str(game_data[line + 2])
    game_out.ninja.block_location = str(game_data[line + 3])
    game_out.ninja.inside_building = str(game_data[line + 4])
    game_out.ninja.is_blocking = str(game_data[line + 5])
    game_out.ninja.under_attack_on = str(game_data[line + 6])
    game_out.ninja.win_game = str(game_data[line + 7])
    game_out.ninja.beat_boss = str(game_data[line + 8])

    # Read and assign badguys list values from game data file




































    






















