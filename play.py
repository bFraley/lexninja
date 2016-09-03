# lexninja text-adventure game - Brett Fraley - 2016

import os
import lexninja

def Start():

    state = lexninja.State()
    state.menu = True

    def menu_mode():
        command = lexninja.game_prompt('Choose option (1 - 4)')

        if lexninja.valid_menu_option(command):

            # Process and act on menu option selection.

            # Resume
            if command == '1':
                state.paused = False
                state.menu = False
                command_mode()

            # New Game
            elif command == '2':
                Start()

            # Save Game           
            elif command == '3':
                pass

            # Quit Game
            elif command == '4':
                print('{}'.format(lexninja.exit_message))
                exit(0)

            state.menu = False

    
    #lexninja.print_logo()
    #lexninja.print_menu()

    # game = Game(city, ninja, badguys)

    # Instantiate the city.
    city = lexninja.City()

    # Hide the ancient golden sword in a building.
    sword_index = lexninja.new_golden_sword_index()
    city.blocks[sword_index].has_goldensword = True
    city.blocks[sword_index].has_badguy = True

    # Place the 5 bad guys in buildings, where one
    # of them is the boss protecting the sword.

    badguys = lexninja.new_badguy_indexlist()
    for i in badguys:
        city.blocks[i].has_badguy = True
        
    # Place 4 health boosts in buildings without badguys.

    for building in city.blocks:
        if not building.has_badguy:
            building.has_health = True

    # Instantiate the ninja character.
    ninja = lexninja.Ninja(city)

    def command_mode():
        if state.menu:
            menu_mode()

        else:
            # Get, parse, and execute player command.
            command = lexninja.game_prompt('Next move: ')

            # If command is enter, or nothing, enter menu mode.
            if command == '' or len(command) == 0:
                state.paused = True
                state.menu = True
                os.system("clear")
                lexninja.print_menu()
                menu_mode()
            else:
                command = command.upper()
            
            # Refactor THIS!!

            # Move North
            if command == lexninja.game_commands[0]:
                ninja.move_in_direction('N')

            # Move East
            elif command == lexninja.game_commands[1]:
                ninja.move_in_direction('E')

            # Move South
            elif command == lexninja.game_commands[2]:
                ninja.move_in_direction('S')

            # Move West
            elif command == lexninja.game_commands[3]:
                ninja.move_in_direction('W')

            # Use sword.
            elif command == lexninja.game_commands[4]:
                pass
            # Use chucks.
            elif command == lexninja.game_commands[5]:
                pass
            # Use stars.
            elif command == lexninja.game_commands[6]:
                pass
            # Enter building.
            elif command == lexninja.game_commands[7]:
                pass
            # Exit building.
            elif command == lexninja.game_commands[8]:
                pass
            # Attack   
            elif command == lexninja.game_commands[9]:
                pass
            # Block
            elif command == lexninja.game_commands[10]:
                pass


    # Enter game loop.
    RUN = True

    while RUN:
        command_mode()
        

