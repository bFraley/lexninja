# lexninja text-adventure game - Brett Fraley - 2016
# play.py

import text
import game

def Start():
    # Instantiate an instance of Game and enter game loop.
    play = game.Game()
    RUN = True
    text.print_logo()

    while RUN:
        play.command_mode()

# Execute game.
Start()
 