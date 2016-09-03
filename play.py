# lexninja text-adventure game - Brett Fraley - 2016

import lexninja

def Start():
    # Instantiate an instance of Game and enter game loop.
    game = lexninja.Game()
    RUN = True
    lexninja.print_logo()

    while RUN:
        game.command_mode()


# Execute game.
Start()
        