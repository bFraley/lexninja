# lexninja text-adventure game - Brett Fraley - 2016
# text.py

import os

# Textual content and dialogue
# ----------------------------

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
menu_options = ['New Game', 'Resume', 'Load Game', 'Save Game', 'Quit Game']
exit_message = 'Thank you for playing lexninja, have a nice day!\n'
win_message = 'CONGRATULATIONS, MISSION COMPLETE! YOU HAVE EARNED GREAT HONOR!\n'
warn_exit_building = 'You must first exit the building!\n'
warn_invalid_direction = 'You cannot move further in that direction!'

game_commands = [
    '________________________________',
    'COMMAND            WHAT IT DOES',
    '________________________________',
    'N         Move 1 block North.',
    'W         Move 1 block West.',
    'S         Move 1 block South.',
    'E         Move 1 block East.',
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
    'HELP      View the game commands.'
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
