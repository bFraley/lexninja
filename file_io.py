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
    city_line = "\n$city"

    for building in city.blocks:
        has_health = str(building.has_health)
        has_badguy = str(building.has_badguy)
        has_goldensword = str(building.has_goldensword)
        visited = str(building.visited)

        city_line += '\n$B'
        city_line += '\n' + has_health + ' '
        city_line += '\n' + has_badguy + ' '
        city_line += '\n' + has_goldensword + ' '
        city_line += '\n' + visited

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

    return file_data  


def get_game_data(game_data):
    game_out = lexninja.Game()

    state_index = game_data.index('$state')
    city_index = game_data.index('$city')
    ninja_index = game_data.index('$ninja')
    bdguys_index = game_data.index('$badguys')


        if line == '$city':
            game_out.state.paused = bool(line)
            game_out.state.saved = bool(line)

    
    game_out.state = state_out
    game_out.city = city_out
    game_out.ninja = ninja_out
    game_out.badguys = badguys_out



























