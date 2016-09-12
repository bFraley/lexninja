# lexninja text-adventure game - Brett Fraley - 2016
# ninja.py

import os
import text
import logic
import maps

# Define ninja character.
# Accepts a city instance.

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
        if self.inside_building:
            print(text.warn_exit_building)

        # Ninja can't move beyond edges of city.
        elif direction == 'N':      
            if self.ninja_on_edge(maps.north_edge):
                print(text.warn_invalid_direction)
            else:
                self.block_location = self.block_location - 3
                os.system("clear")
                maps.print_map(self)
                self.print_location()

        elif direction == 'E':
            if self.ninja_on_edge(maps.east_edge):
                print(text.warn_invalid_direction)
            else:
                self.block_location = self.block_location + 1
                os.system("clear")
                maps.print_map(self)
                self.print_location()

        elif direction == 'S':
            if self.ninja_on_edge(maps.south_edge):
                print(text.warn_invalid_direction)
            else:
                self.block_location = self.block_location + 3
                os.system("clear")
                maps.print_map(self)
                self.print_location()
            
        elif direction == 'W':
            if self.ninja_on_edge(maps.west_edge):
                print(text.warn_invalid_direction)
            else:
                self.block_location = self.block_location - 1
                os.system("clear")
                maps.print_map(self)
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
                    if logic.get_random_badguy_block_attack() == 1:
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
                    if logic.get_random_badguy_block_attack() == 1:
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

        if self.inside_building:
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
        if not self.inside_building:
            print('You are not in a building!')
        else:
            if self.city.blocks[self.block_location].has_badguy:
                print('Where do you think you are going?')
                print('Now stay and fight, coward!')
            else:
                self.inside_building = False
                os.system("clear")
                maps.print_map(self)
                self.print_location()
    
    # Check if ninja is on city edges.
    # So, they can't move further in that direction.
    # Accepts a ninja, and list of 3 block indices.

    def ninja_on_edge(self, indices_list):
        if self.block_location in indices_list:
            return True
        else:
            return False

        # Ninja change weapon.
    def change_weapon(self, weapon):
        if self.weapon == weapon:
            print('You are already using that weapon!')
        else:
            self.weapon = weapon
            print('Now using {}'.format(self.weapon))
