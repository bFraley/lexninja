# lexninja text-adventure game - Brett Fraley - 2016
# Class definitions, functions and global values for lexninja.

from random import randint
import utils

# An instance of a game, which could be new or loaded from saved game data.
class Game():
    def __init__(self, city_t, ninja_t, badguys_t, datafile):
        self.datafile = datafile or None
        self.city = city_t
        self.ninja = ninja_t
        self.badguys = badguys_t

        # load file of saved game data
        # def get_game_data

# Define various game states that change during runtime.
class State():
    def __init__(self):
        self.paused = False
        self.saved = False
        self.player_win = False
        self.menu = False


# Define loadable saved user data specific to their game instance.
class User_Game_Data():
    def __init__(self, game_t):
        self.game_data = game_t


# Building class definition.
class Building():
    def __init__(self):
        self.has_health = False
        self.has_badguy = False
        self.has_goldensword = False
        self.visited = False

        
# There is a single instance of city in the game.
class City():
    def __init__(self):

        self.blocks = [
            Building(), Building(), Building(),
            Building(), Building(), Building(),
            Building(), Building(), Building()
        ]

# Define ninja character.
class Ninja():
    def __init__(self):
        self.health = 3
        self.weapon = 1 # 1 is stars, 2 is nunchucks, 3 is sword.
        self.block_location = 5 # Starts in middle of city.
        self.inside_building = False


    def move_in_direction(self):
        pass

    def attack(self):
        pass

    def block_attack(self):
        pass

    def enter_building(self):
        pass

    def exit_building(self):
        pass

    def change_weapon(self):
        pass


# Define opponent character.
class Opponent():
    def __init__(self):
        self.health = 3
        self.boss = False

    def attack(self):
        pass

    def block_attack(self):
        pass


# Choose which building 'Ancient Golden Sword' is in.
def new_golden_sword_index():
    return randint(0, 8)

# Output copy of city.blocks state.
def copy_city_data(city_instance):

    city_data_output = []
    i = 0

    while i < len(city_instance.blocks):
        city_data_output.append(city.blocks[i])
        i = i + 1

    return city_data_output
    

# Textual content and dialogue
#-----------------------------

# Unicode graphical characters
blackstar = '\u2605'
whitestar = '\u2606'
yinyang = '\u262f'
dharma = '\u2638'
swords = '\u2694'
sword_line = swords*36
yinyang_line = yinyang*36
star_line = '{} {}'.format(blackstar, whitestar)
star_line = star_line*12

# Dialogue text.
author = '       By Brett Fraley - 2016       '
menu_options = ['Resume', 'New Game', 'Save Game', 'Quit Game']

# Logo is a list of lines used in print_logo below.
logo = [
    ' _                 _        _       ',
    '| | _____  ___ __ (_)_ __  (_) __ _ ',
    '| |/ _ \ \/ / `_ \| | `_ \ | |/ _` |',
    '| |  __/>  <| | | | | | | || | (_| |',
    '|_|\___/_/\_\_| |_|_|_| |_|/ |\__,_|',
    '                         |__/'
]

# Print game logo.
def print_logo():
    os.system("clear")
    print('\n')

    for line in logo:
        print(line)

    print('{}\n{}\n{}\n'.format(sword_line, yinyang_line, author))


# Print main menu.
def print_menu():
    print('\n{}\n'.format(star_line))
    i = 0
    while i < len(menu_options):
        print('{} {}. {}'.format(dharma, i, menu_options[i]))
        i = i + 1







