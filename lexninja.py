# lexninja text-adventure game - Brett Fraley - 2016
# Class definitions, functions and global values for lexninja.

from random import randint
import utils

# Game Class Definitions
# ----------------------------------------------------------------------------


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

        """
        Building index map

        0 1 2
        3 4 5
        6 7 8
        """

# Define ninja character.
# Accepts a city instance that is passed in in play.py.
class Ninja():
    def __init__(self, city):
        self.city = city
        self.health = 3
        self.weapon = 1 # 1 is stars, 2 is nunchucks, 3 is sword.
        self.block_location = 4 # Starts in middle of city.
        self.inside_building = False


    def print_location(self):
        if self.inside_building:
            print('Inside Building: {}'.format(self.block_location + 1))
        else:
            print('City Block: {}'.format(self.block_location + 1))
        

    # Move the ninja 1 city block in the direction intended by the player.
    def move_in_direction(self, direction):
        self.direction = direction

        if ninja_is_inside(self):
            print(warn_exit_building)

        elif direction == 'N':
            
            if ninja_on_edge(self, [0, 1, 2]):
                print(warn_invalid_direction)
            else:
                self.block_location = self.block_location - 3
                self.print_location()

        elif direction == 'E':

            if ninja_on_edge(self, [2, 5, 8]):
                print(warn_invalid_direction)
            else:
                self.block_location = self.block_location + 1
                self.print_location()

        elif direction == 'S':

            if ninja_on_edge(self, [6, 7, 8]):
                print(warn_invalid_direction)
            else:
                self.block_location = self.block_location + 3
                self.print_location()
            
        elif direction == 'W':

            if ninja_on_edge(self, [0, 3, 6]):
                print(warn_invalid_direction)
            else:
                self.block_location = self.block_location - 1
                self.print_location()


    def attack(self):
        pass    

    def block_attack(self):
        pass

    def enter_building(self):
        self.inside_building = True

    def exit_building(self):
        self.inside_building = False
    
    # Weapon arg is either 1, 2, or 3
    def change_weapon(self, weapon):
        self.weapon = weapon


# Define bad guy character.
# Accepts a city instance that is passed in in play.py.
class Badguy():
    def __init__(self, city):
        self.city = city
        self.health = 3
        self.boss = False

    def attack(self):
        pass

    def block_attack(self):
        pass

# Functions Definitions
# ----------------------------------------------------------------------------

# Game logic functions.
# -----------------------------

# Choose which building 'Ancient Golden Sword' is in.
def new_golden_sword_index():
    golden_sword_location = randint(0, 8)
    print('Ancient Golden Sword located at {}'.format(golden_sword_location))
    return golden_sword_location

# Choose which 5 buildings bad guys will occupy.
# Ignoring the 'boss' building for now.
def new_badguy_indexlist():
    badguy_location_list = []
    for i in range(0, 5):
        badguy_location_list.append(randint(0, 8))
    
    print('Bad guys located in buildings {}'.format(badguy_location_list))
    return badguy_location_list

# User command input functions.
# ----------------------------

# Return command value from game prompt.
def game_prompt(msg):
    command_in = input(msg)
    return command_in

# Verify a valid menu option input
def valid_menu_option(option):
    option = option.upper()

    if option in ['1', '2', '3', '4']:
        return True
    else:
        print('Unrecognized menu option. Try again.')
        return False

# Ninja character logic functions.
# -------------------------------

# Check if ninja is inside a building.
def ninja_is_inside(ninja_self):
    if ninja_self.inside_building:
        return True
    else:
        return False

# Check if ninja is on city edges.
# So, they can't move further in that direction.
# Accepts a ninja, and list of 3 block indices.

def ninja_on_edge(ninja_self, indices_list):
    if ninja_self.block_location in indices_list:
        return True
    else:
        return False


# Game data saving functions
# --------------------------

# Output copy of city.blocks state.
def copy_city_data(city_instance):

    city_data_output = []
    i = 0

    while i < len(city_instance.blocks):
        city_data_output.append(city.blocks[i])
        i = i + 1

    return city_data_output

# Output copy of ninja character state.

# Output copy of game state values
    

# Textual content and dialogue
# ----------------------------------------------------------------------------

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
game_commands = ['N', 'E', 'S', 'W', 'SWORD', 'CHUCKS', 'STAR',
                    'ENTER', 'EXIT', 'ATTACK', 'BLOCK']
exit_message = 'Thank you for playing lexninja, have a nice day!\n'
warn_exit_building = 'You must first exit the building!\n'
warn_invalid_direction = 'You cannot move further in that direction!'


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
    i = 1
    while i <= len(menu_options):
        print('{} {}. {}'.format(dharma, i, menu_options[i - 1]))
        i = i + 1

# Print the game commands.
def print_game_commands():
    for command in game_commands:
        print('{} '.format(command))



