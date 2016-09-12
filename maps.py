# lexninja text-adventure game - Brett Fraley - 2016
# maps.py

from text import swords
from text import yinyang

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

# City map edge indices for determining boundaries.
north_edge = [0, 1, 2]
east_edge = [2, 5, 8]
south_edge = [6, 7, 8]
west_edge = [0, 3, 6]

# Reset city map to original.
def reset_city_map():
    target = ''
    
    for i in north_edge:
        target = list(city_map[i])

        for to_reset in [3, 14, 25]:
            target[to_reset] = ' '
            
        city_map[i] = ''.join(target)

    return city_map

# Insert sword character to city map strings.
def update_city_map(row, block):
    visited = 0
    target = ''

    for i in east_edge:
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
