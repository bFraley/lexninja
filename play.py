# lexninja text-adventure game - Brett Fraley - 2016

import lexninja

def Start():
    RUN = True

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


    # Instantiate and Enter Ninja



    # Parse and carry out player's commands 

    while RUN:
        player_command = input('\n Make your move: ')
        print(player_command)

    


