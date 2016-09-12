# utils.py
# lexninja text-adventure game - Brett Fraley - 2016

import os
from badguy import Badguy
import game

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
    city_line = "\n$city"

    for building in city.blocks:

        city_line += '\n$B\n'
        city_line += str(building.has_health) + '\n'
        city_line += str(building.has_badguy) + '\n'
        city_line += str(building.has_goldensword) + '\n'
        city_line += str(building.visited)

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
    os.system("clear")
    print('Game saved!')

# Load game file (saved_game.txt).

def load_game(filename):
    file = open(filename, 'r')
    file_data = file.read()
    file.close()
    return file_data.split('\n') 

def get_game_data(game_obj, game_data):

    # Get num of badguys saved in game_data
    badguy_count = 0
    for line in game_data:
        if line == ' BGUY$':
            badguy_count += 1

    count_is_less = badguy_count < len(game_obj.badguys) 

    # Reset badguys length equal to game_data
    if count_is_less:
        while badguy_count < len(game_obj.badguys):
            game_obj.badguys.pop()
    else:
        while badguy_count > len(game_obj.badguys):
            game_obj.badguys.append(game_obj.badguys[0])
    
    # Get game data delimiter indices. 
    state_index = game_data.index('$state')
    city_index = game_data.index('$city')
    ninja_index = game_data.index('$ninja')
    badguys_index = game_data.index('$badguys')

    # Read and assign game.state values from game data file.
    line = state_index

    if game_data[line + 1] == 'True':
        game_obj.state.paused = True
    else:
        game_obj.state.paused = False

    if game_data[line + 2] == 'True':
        game_obj.state.saved = True
    else:
        game_obj.state.saved = False

    if game_data[line + 3] == 'True':
        game_obj.state.menu = True
    else:
        game_obj.state.menu = False

    # Read and assign game.city values from game data file.
    block = city_index + 1
    i = 0

    while i < 9:
        health = block + 1
        badguy = block + 2
        sword = block + 3
        visited = block + 4

        if game_data[health] == 'True':
            game_obj.city.blocks[i].has_health = True
        else:
            game_obj.city.blocks[i].has_health = False

        if game_data[badguy] == 'True':
            game_obj.city.blocks[i].has_badguy = True
            game_obj.badguys.append(Badguy(game_obj.city))
        else:
            game_obj.city.blocks[i].has_badguy = False

        if game_data[sword] == 'True':
            game_obj.city.blocks[i].has_goldensword = True
        else:
            game_obj.city.blocks[i].has_goldensword = False

        if game_data[visited] == 'True':
            game_obj.city.blocks[i].has_visited = True
        else:
            game_obj.city.blocks[i].has_visited = False

        block = block + 5
        i += 1

    # Read and assign game.ninja values from game data file.
    line = ninja_index

    game_obj.ninja.city = game_obj.city
    game_obj.ninja.health = int(game_data[line + 1])
    game_obj.ninja.weapon = game_data[line + 2]
    game_obj.ninja.block_location = int(game_data[line + 3])

    if game_data[line + 4] == 'True':
        game_obj.ninja.inside_building = True
    else:
        game_obj.ninja.inside_building = False

    if game_data[line + 6] == 'True':
        game_obj.ninja.under_attack_on = True
    else:
        game_obj.ninja.under_attack_on = False

    if game_data[line + 8] == 'True':
        game_obj.ninja.beat_boss = True
    else:
        game_obj.ninja.beat_boss = False

    game_obj.ninja.is_blocking = False
    game_obj.ninja.win_game = False

    # Read and assign badguys list values from game data file.
    line = badguys_index + 1

    for i in range(0,badguy_count):
        game_obj.badguys[i].health = int(game_data[line + 1])
        game_obj.badguys[i].city = game_obj.city

        if game_data[line + 2] == 'True':
            game_obj.badguys[i].is_boss = True
        else:
            game_obj.badguys[i].is_boss = False

        line = line + 3
        i += 1

    os.system("clear")
    print('Saved game loaded!')
    