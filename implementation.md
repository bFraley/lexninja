# Feature Implementation Outline

## Overall project structure
* Create `utils.py` file for miscellaneous helper functions for the game.
* Define all game classes in the `lexninja.py` file

* Run game setup functions, instantiate initial game classes, and enter game loop
in the `play.py` file.

* Run game setup functions, instantiate initial game classes, and enter game runtime loop
in the `run.py` file.

## Game Classes

### Environment
* City
* Block
* Building (1 of 9 buildings will contain the 'Ancient Golden Sword')

### Characters
* Ninja
* Opponent

### Items
* Weapons
* Heart (health boost)

The city will be an array of Building objects.

* 5 of 9 buildings will contain an opponent. While the other
* 4 of 9 buildings will contain a heart health item.

* Inside 1 of the 5 buildings that contain an opponent will be the
ancient golden sword item.

* The opponent in the building that contains the golden sword will take
6 strikes to defeat and will be immune to nunchuck and throwing star strikes.
So, only 6 strikes of the sword will defeat the 'boss' protecting the sword.

* Regular opponents are defeated after 3 strikes of any weapon.

## Main Menu

The main menu will appear when the game launches, and can be pulled up again
when a user enters a pause command. The pause command will be an uppercase `P`
character. Pause will be the only special command. Other text input commands are
explicitly for game play actions.

Main menu options

1. Resume

2. New Game

3. Save Game

4. Quit Game

## Game Loop

For game saving functionality, the game's data structures and corresponding
values will be written to file. The game loop must be able to update this file
when a user chooses save game from a main menu. The game loop must be  able to 
copy values from the saved game file and start from that state.

Player moves (or turns) allow for one action to be taken.
On each turn, a player can enter one of the following commands:
 
#### Move one city block in a cardinal direction.

N, E, S, W

#### Switch weapon.

SWORD, NUNCHUCK, STAR

#### Enter bulding.

ENTER

#### Exit building.

EXIT

#### Attack opponent with one strike.

ATTACK

#### Block an opponent's strike.

BLOCK 
