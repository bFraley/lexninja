# lexninja text-adventure game - Brett Fraley - 2016
# Class definitions, functions and global values for lexninja.

import os
from random import randint
import utils

# Game Class Definitions
# ----------------------------------------------------------------------------

# An instance of a game, which could be new or loaded from saved game data.
class Game():
    def __init__(self, datafile = None):
        self.datafile = datafile
        self.state = State()
        self.city = City()
        self.ninja = Ninja(self.city)
        self.badguys = self.get_badguys()
        self.hide_sword()
        self.hide_healths()

    # Hide the ancient golden sword in a building.
    def hide_sword(self):
        sword_index = new_golden_sword_index()
        self.city.blocks[sword_index].has_goldensword = True
        self.city.blocks[sword_index].has_badguy = True

    # Place 4 health boosts in buildings without badguys.
    def hide_healths(self):
        for building in self.city.blocks:

            # Put health boosts in buildings that don't have a bad guy.
            if not building.has_badguy:
                building.has_health = True

            # Put health boost in building containing the boss.
            if building.has_goldensword:
                building.has_health = True

    # Randomly pick 5 bad guy location indices to place in buildings.
    def get_badguys(self):
        badguy_index = new_badguy_indexlist()

        # Empty list container for the 5 instances of Badguy
        badguys = []
        
        # For each bad guy's building index, append to badguys list.
        for i in badguy_index:
            self.city.blocks[i].has_badguy = True
            badguys.append(Badguy(self.city))

            # Assign the boss of the building that has golden sword.
            if self.city.blocks[i].has_goldensword:
                badguys[i].is_boss = True
                badguys[i].health = 6
    
        return badguys

    # Command mode prompt loop for player moves.
    def command_mode(self):
        if self.state.menu:
            self.menu_mode()

        # Player won the game.
        elif self.ninja.win_game:
            os.system("clear")
            print_logo()
            print(win_message)
            exit(0)

        else:
            # Ninja under attack is turned on when entering buildings with badguys.
            # Whether they attack is randomly determined. If ninja did not block
            # as last move, the ninja's health is decremented.

            if self.ninja.under_attack_on:
                
                if get_random_attack() == 1:
                    if not self.ninja.is_blocking:
                        print('YOU ARE HIT BY A FIERCE BLOW!')
                        self.ninja.change_health(0, 1)

                        # Warn when health is down to 1.
                        if self.ninja.health == 1:
                            print('Warning! {} health left!'.format(self.ninja.health))

                        # Ninja health is at zero. Player loses game.
                        elif self.ninja.health < 1:
                            print_logo()
                            print(star_line)
                            print('\nYOU LOSE! All ninjas have bad days, try again!\n')
                            print(exit_message)
                            exit(0)
                    else:
                        # Ninja was blocking attack.
                        print("Nice block, that would of hurt!")

                # Reset is_blocking.
                self.ninja.is_blocking = False;

            # Get, parse, and execute player command.
            command = game_prompt('\nNext move: ')

            # If command is enter, or nothing, enter menu mode.
            if command == '' or len(command) == 0:
                self.state.paused = True
                self.state.menu = True
                os.system("clear")
            else:
                command = command.upper()
            
            # Move North, East, South, or West.
            if command in ['N', 'E', 'S', 'W']:
                self.ninja.move_in_direction(command)

            # Use stars, chucks, or sword.
            elif command in ['STARS', 'CHAKU', 'SWORD']:
                self.ninja.change_weapon(command)
                
            # Enter building.
            elif command == 'ENTER':
                self.ninja.enter_building()

            # Exit building.
            elif command == 'EXIT':
                self.ninja.exit_building()

            # Attack   
            elif command == 'ATTACK':
                self.ninja.attack(self.badguys)

            # Block
            elif command == 'BLOCK':
                self.ninja.block_attack()

            # Status
            elif command == 'STATUS':
                os.system("clear")
                print('\nSTATUS\n{}\n'.format(yinyang_line))
                self.ninja.print_location()
                print('\nHEALTH: {}'.format(self.ninja.health))
                print('\nWEAPON: {}'.format(self.ninja.weapon))
                print('\n{} Bad guys left to defeat!'.format(len(self.badguys)))

            # Map
            elif command == 'MAP':
                os.system("clear")
                self.ninja.print_location()
                print_map(self.ninja)

            # Menu
            elif command == 'MENU':
                os.system("clear")
                self.state.menu = True

            # Help
            elif command == 'HELP':
                print_help()

            else:
                print('Invalid command. Type help or try again.')

    # Menu mode loop for main menu operations.
    def menu_mode(self):
        print_menu()
        command = game_prompt('Choose option (1 - 4)\n')
        
        # Process and act on menu option selection.
        if valid_menu_option(command):

            # Resume
            if command == '1':
                self.state.paused = False
                self.state.menu = False
                os.system("clear")
                print('\nYour mission awaits!!!\n')
                print_help()
                self.command_mode()

            # New Game
            elif command == '2':
                self.state = State()
                self.city = City()
                self.ninja = Ninja(self.city)
                self.badguys = self.get_badguys()
                self.hide_sword()
                self.hide_healths()
                print_logo()
                print_help()
                self.state.menu = False
                city_map = reset_city_map()

            # Save Game           
            elif command == '3':
                print('saving game not implemented')

            # Quit Game
            elif command == '4':
                os.system("clear")
                print_logo()
                print('{}'.format(exit_message))
                exit(0)

    # load file of saved game data
    # def get_game_data

# Define various game states that change during runtime.
class State():
    def __init__(self):
        self.paused = False
        self.saved = False
        self.menu = True


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
# Accepts a city instance that is passed in in play.py.
class Ninja():
    def __init__(self, city):
        self.city = city
        self.health = 5
        self.weapon = 'STARS'
        self.block_location = 4 # Starts in middle of city.
        self.inside_building = False
        self.is_blocking = False
        self.under_attack_on = False
        self.win_game = False
        self.beat_boss = False
    
    # Print ninja location.
    def print_location(self):
        if self.inside_building:
            print('Inside Building: {}'.format(self.block_location + 1))
        else:
            print('City Block: {}'.format(self.block_location + 1))
        
    # Move the ninja 1 city block in the direction intended by the player.
    def move_in_direction(self, direction):
        self.direction = direction

        # Ninja can't move within city when ninja is inside building.
        if ninja_is_inside(self):
            print(warn_exit_building)

        # Ninja can't move beyond edges of city.
        elif direction == 'N':      
            if ninja_on_edge(self, [0, 1, 2]):
                print(warn_invalid_direction)
            else:
                self.block_location = self.block_location - 3
                os.system("clear")
                print_map(self)
                self.print_location()

        elif direction == 'E':
            if ninja_on_edge(self, [2, 5, 8]):
                print(warn_invalid_direction)
            else:
                self.block_location = self.block_location + 1
                os.system("clear")
                print_map(self)
                self.print_location()

        elif direction == 'S':
            if ninja_on_edge(self, [6, 7, 8]):
                print(warn_invalid_direction)
            else:
                self.block_location = self.block_location + 3
                os.system("clear")
                print_map(self)
                self.print_location()
            
        elif direction == 'W':
            if ninja_on_edge(self, [0, 3, 6]):
                print(warn_invalid_direction)
            else:
                self.block_location = self.block_location - 1
                os.system("clear")
                print_map(self)
                self.print_location()

    # Increase or decrease ninja health.
    def change_health(self, dec_or_inc, amt):
        amt = amt or 1

        if not dec_or_inc:
            self.health -= amt
        else:
            self.health += amt
    
    # Ninja attack method.
    def attack(self, badguy_list):
        
        # Can't attack if not inside building.
        if not self.inside_building:
            print('You are outside, and there is no one to attack!')

        # Inside, but no bad guy to attack.    
        elif not self.city.blocks[self.block_location].has_badguy:
            print('There is no one here to attack!')

        # Execute attack.
        else:

            list_end = len(badguy_list) - 1
            badguy = badguy_list[list_end]

            # If ninja is facing boss!
            if self.city.blocks[self.block_location].has_goldensword:

                # Assign boss at end of bad guy list.
                for guy in badguy_list:
                    if guy.is_boss:
                        badguy_list[list_end] = guy
                        badguy = badguy_list[list_end]
                    
                # Boss only damaged by sword.
                if not self.weapon == 'SWORD':
                    print('The boss is immune to stars and nanchaku!')

                else:
                    # Decrement boss health if not blocked.
                    if get_random_badguy_block_attack() == 1:
                        print('Your attack was blocked!!!')
                    else:
                        badguy.change_health(0, 1)
                        print("Successful attack!")
            else:
                # Bad guy is not boss.
                # If ninja already beat the boss then they
                # have the golden sword. So if ninja is using 
                # sword, decrement bad guy health to zero.
                if self.beat_boss and self.weapon == 'SWORD':
                    badguy.health = 0
                else:
                    if get_random_badguy_block_attack() == 1:
                        print('Your attack was blocked!!!')
                    else:
                        badguy.change_health(0, 1)
                        print("Successful attack!")

            # When bad guy health reaches zero.
            if badguy.health < 1:
                self.city.blocks[self.block_location].has_badguy = False
                badguy_list.pop()

                # Reset ninja under attack to off.
                self.under_attack_on = False
                
                # Did ninja defeat the boss?
                if self.city.blocks[self.block_location].has_goldensword:
                    self.beat_boss = True
                    self.city.blocks[self.block_location].has_goldensword = False
                    print('\nBOSS DEFEATED!!')
                    print('You have retreived the golden sword!')

                    if len(badguy_list) > 0:
                        print('Defeat remaining bad guys to complete your mission.')
                        print('{} left! Take them out!'.format(len(badguy_list)))
                else:
                    # Normal bad guy defeated.
                    print('\nOpponent Defeated!')

                # Are all badguys defeated ?
                if len(badguy_list) < 1:
                    self.win_game = True
     
    # Ninja execute block. Sets ninja is blocking flag.                   
    def block_attack(self):
        self.is_blocking = True
    
    # Ninja enter building.
    def enter_building(self):

        if self.inside_building == True:
            print('You are already inside a building!')
        else:
            self.inside_building = True
            self.print_location()

            if self.city.blocks[self.block_location].has_health:
                self.change_health(1, 1)
                print('+1 Health Boost!!!')
                print('HEALTH: {}'.format(self.health))

                # Remove the health item!
                self.city.blocks[self.block_location].has_health = False

            # If building has golden sword.
            if self.city.blocks[self.block_location].has_goldensword:
                print('You have found the ancient golden sword!')
                print('Defeat the boss to complete the mission!')

            # If building has a bad guy, turn on ninja under attack flag.
            if self.city.blocks[self.block_location].has_badguy:
                self.under_attack_on = True
                print('You there! Prepare to bleed!')
    
    # Ninja exit building.
    def exit_building(self):
        if self.inside_building == False:
            print('You are not in a building!')
        else:
            if self.city.blocks[self.block_location].has_badguy:
                print('Where do you think you are going?')
                print('Now stay and fight, coward!')
            else:
                self.inside_building = False
                os.system("clear")
                print_map(self)
                self.print_location()
    
    # Ninja change weapon.
    def change_weapon(self, weapon):
        if self.weapon == weapon:
            print('You are already using that weapon!')
        else:
            self.weapon = weapon
            print_weapon(self.weapon)

# Define bad guy character.
# Accepts a city instance that is passed in in play.py.
class Badguy():
    def __init__(self, city):
        self.city = city
        self.health = 3
        self.is_boss = False

    # Decrease or increase health.
    # 0 to decrease or 1 to increase, amt
    def change_health(self, dec_or_inc, amt):
        amt = amt or 1

        if not dec_or_inc:
            self.health -= amt
        else:
            self.health += amt

    def attack(self):
        pass

# Functions Definitions
# ----------------------------------------------------------------------------

# Game logic functions.
# -----------------------------

# Choose which building 'Ancient Golden Sword' is in.
def new_golden_sword_index():
    golden_sword_location = randint(0, 8)
    return golden_sword_location

# Choose which 5 buildings bad guys will occupy.
def new_badguy_indexlist():
    badguy_location_list = []
    for i in range(0, 4):
        badguy_location_list.append(randint(0, 8))
    
    return badguy_location_list

# Compute 1 in 4 chance that a bad guy blocks player's attack.
def get_random_badguy_block_attack():
    return randint(-2, 1)

# Compute 1 in 4 chance that bad guy attacks.
def get_random_attack():
    return randint(-2, 1)

# User command input functions.
# ----------------------------

# Return command value from game prompt.
def game_prompt(msg):
    command_in = input(msg)
    return command_in

# Verify a valid menu option input.
def valid_menu_option(option):
    option = option.upper()

    if option in ['1', '2', '3', '4']:
        return True
    else:
        os.system("clear")
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
menu_options = ['New Game', 'Resume', 'Save Game', 'Quit Game']
exit_message = 'Thank you for playing lexninja, have a nice day!\n'
win_message = 'CONGRATULATIONS, MISSION COMPLETE! YOU HAVE EARNED GREAT HONOR!\n'
warn_exit_building = 'You must first exit the building!\n'
warn_invalid_direction = 'You cannot move further in that direction!'

city_map = [
    '-------    -------    -------',
    '[  1  ]    [  2  ]    [  3  ]',
    '[     ]    [     ]    [     ]',
    '-------    -------    -------',
    '[  4  ]    [  5  ]    [  6  ]',
    '[     ]    [     ]    [     ]',
    '-------    -------    -------',
    '[  7  ]    [  8  ]    [  9  ]',
    '[     ]    [     ]    [     ]',
    '-------    -------    -------'
]

game_commands = [
    '________________________________',
    'COMMAND            WHAT IT DOES',
    '________________________________',
    'N         Move 1 block North.',
    'W         Move 1 block West.',
    'S         Move 1 block South',
    'E         Move 1 block East',
    'ENTER     Enter building.',
    'EXIT      Exit building.',
    'SWORD     Change weapon to sword.',
    'STARS     Change weapon to throwing stars.',
    'CHAKU     Change weapon to nanchaku.',
    'ATTACK    Attack bad guy.',
    'BLOCK     Block bad guy attack.',
    'STATUS    View ninja status.',   
    'MAP       View location on map.',
    'MENU      View main menu.',
    'HELP      View the game commands'
]

# Logo is a list of lines used in print_logo below.
logo = [
    ' _                 _        _       ',
    '| | _____  ___ __ (_)_ __  (_) __ _ ',
    '| |/ _ \ \/ / `_ \| | `_ \ | |/ _` |',
    '| |  __/>  <| | | | | | | || | (_| |',
    '|_|\___/_/\_\_| |_|_|_| |_|/ |\__,_|',
    '                         |__/'
]

# Printing helper functions
# -------------------------

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

    print()

# Print the game command help.
def print_help():
    os.system("clear")
    for command in game_commands:
        print('        {}    {}'.format(yinyang, command))

# Reset city map to original.
def reset_city_map():
    target = ''
    
    for i in [2, 5, 8]:
        target = list(city_map[i])

        for to_reset in [3, 14, 25]:
            target[to_reset] = ' '
            
        city_map[i] = ''.join(target)

    return city_map

# Insert sword character to city map strings.
def update_city_map(row, block):
    visited = 0
    target = ''

    for i in [2, 5, 8]:
        # Update prior location with yin yang.
        if swords in city_map[i]:
            target = list(city_map[i])
            visited = target.index(swords)
            target[visited] = yinyang
            city_map[i] = ''.join(target)

    # Update current location.
    city_map[row] = list(city_map[row])
    city_map[row][block] = swords
    city_map[row] = ''.join(city_map[row])

# Print city map.
def print_map(ninja_self):
    loc = ninja_self.block_location + 1
    if loc == 1:
        update_city_map(2, 3)
    elif loc == 2:
        update_city_map(2, 14)
    elif loc == 3:
        update_city_map(2, 25)
    elif loc == 4:
        update_city_map(5, 3)
    elif loc == 5:
        update_city_map(5, 14)
    elif loc == 6:
        update_city_map(5, 25)
    elif loc == 7:
        update_city_map(8, 3)
    elif loc == 8:
        update_city_map(8, 14)
    elif loc == 9:
        update_city_map(8, 25)

    for line in city_map:
        print(line)

    print()

# Print message for weapon changes.
def print_weapon(weapon_string):
    print('Now using {}'.format(weapon_string))
