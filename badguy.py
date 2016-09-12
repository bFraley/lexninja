# lexninja text-adventure game - Brett Fraley - 2016
# badguy.py

# Define bad guy character.
# Accepts a city instance.

class Badguy():
    def __init__(self, city):
        self.city = city
        self.health = 3
        self.is_boss = False

    # Decrease or increase health.
    # 0 to decrease or 1 to increase, amt
    def change_health(self, dec_or_inc, amt):
        amt = amt or 1

        if not dec_or_inc:
            self.health -= amt
        else:
            self.health += amt