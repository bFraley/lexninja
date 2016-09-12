# lexninja text-adventure game - Brett Fraley - 2016
# logic.py

from random import randint

# lexninja logic functions.
# -------------------------

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