# lexninja text-adventure game - Brett Fraley - 2016

import lexninja

def Start():

    state = lexninja.State()
    state.menu = True

    # Instantiate the city.
    city = lexninja.City()

    # Hide the ancient golden sword in a building.
    sword_index = lexninja.new_golden_sword_index()
    city.blocks[sword_index].has_goldensword = True
    city.blocks[sword_index].has_badguy = True

    # Place the 5 bad guys in buildings, where one
    # of them is the boss protecting the sword.
    badguy_index = lexninja.new_badguy_indexlist()

    # Empty list container for the 5 instances of Badguy
    badguys = []

    for i in badguy_index:
        city.blocks[i].has_badguy = True
        badguys.append(lexninja.Badguy(city))

    # Place 4 health boosts in buildings without badguys.

    for building in city.blocks:
        if not building.has_badguy:
            building.has_health = True

    # Instantiate the ninja character.
    ninja = lexninja.Ninja(city)

    # Instantiate the main instance of Game
    game = lexninja.Game(city, ninja, badguys, state)
    
    # Enter game loop.
    RUN = True

    #lexninja.print_logo()
    #lexninja.print_menu()

    while RUN:
        game.command_mode()
        