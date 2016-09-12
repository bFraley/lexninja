# lexninja text-adventure game - Brett Fraley - 2016
# state.py

# Define game states that change during runtime.
class State():
    def __init__(self):
        self.paused = False
        self.saved = False # NOTE: not using this yet.
        self.menu = True