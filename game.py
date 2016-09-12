# lexninja text-adventure game - Brett Fraley - 2016
# game.py

import os

# lexninja modules
import file_io
import maps
import logic
import text
from state import State
from city import City
from ninja import Ninja
from badguy import Badguy

# Game Class Definition
# Game contains most other game assets and is the core runtime.
# -------------------------------------------------------------

class Game():
    def __init__(self):
        self.state = State()
        self.city = City()
        self.ninja = Ninja(self.city)
        self.badguys = self.get_badguys()
        self.hide_sword()
        self.hide_healths()

    # Hide the ancient golden sword in a building.
    def hide_sword(self):
        sword_index = logic.new_golden_sword_index()
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
        badguy_index = logic.new_badguy_indexlist()

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
            text.print_logo()
            print(text.win_message)
            exit(0)

        else:
            # Ninja under attack is turned on when entering buildings with badguys.
            # Whether they attack is randomly determined. If ninja did not block
            # as last move, the ninja's health is decremented.

            if self.ninja.under_attack_on:
                
                if logic.get_random_attack() == 1:
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
            command = self.game_prompt('\nNext move: ')

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
                print('\nSTATUS\n{}\n'.format(text.yinyang_line))
                self.ninja.print_location()
                print('\nHEALTH: {}'.format(self.ninja.health))
                print('\nWEAPON: {}'.format(self.ninja.weapon))
                print('\n{} Bad guys left to defeat!'.format(len(self.badguys)))

            # Map
            elif command == 'MAP':
                os.system("clear")
                self.ninja.print_location()
                maps.print_map(self.ninja)

            # Menu
            elif command == 'MENU':
                os.system("clear")
                self.state.menu = True

            # Help
            elif command == 'HELP':
                text.print_help()

            else:
                print('Invalid command. Type help or try again.')

    # Menu mode loop for main menu operations.
    def menu_mode(self):
        text.print_menu()
        command = self.game_prompt('Choose option (1 - 5)\n')
        
        # Process and act on menu option selection.
        if self.valid_menu_option(command):

            # Resume
            if command == '2':
                self.state.paused = False
                self.state.menu = False
                os.system("clear")
                print('\nYour mission awaits!!!\n')
                text.print_help()
                self.command_mode()

            # New Game
            elif command == '1':
                self.state = State()
                self.city = City()
                self.ninja = Ninja(self.city)
                self.badguys = self.get_badguys()
                self.hide_sword()
                self.hide_healths()
                self.state.paused = False
                self.state.menu = False
                os.system("clear")
                text.print_logo()
                text.print_help()                
                maps.city_map = maps.reset_city_map()
                self.command_mode()
 
            # Load game data.
            elif command == '3':
                loaded_file = file_io.load_game('saved_game.txt')
                file_io.get_game_data(self, loaded_file)
                self.command_mode()
                
            # Save Game           
            elif command == '4':
                file_io.save_game(self, 'saved_game.txt')

            # Quit Game
            elif command == '5':
                os.system("clear")
                print_logo()
                print('{}'.format(exit_message))
                exit(0)

    # Return command value from game prompt.
    def game_prompt(self, msg):
        command_in = input(msg)
        return command_in

    # Verify a valid menu option input.
    def valid_menu_option(self, option):
        option = option.upper()

        if option in ['1', '2', '3', '4', '5']:
            return True
        else:
            os.system("clear")
            print('Unrecognized menu option. Try again.')
            return False
