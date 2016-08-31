# install.py
# lexninja text-adventure game - Brett Fraley - 2016
# This module sets up a user directory structure for lexninja.

import os

# Set up initial user directory structure.
def install_dirs():

	# Change to user's home directory ( ~ ).
	os.chdir('os.environ["HOME"]')

    # If first time setup? Make lexninja dir
    if not os.path.exists('lexninja'):
    	os.mkdirs('lexninja')
    	os.chdir('lexninja')
        os.makedirs('users')
	    os.chdir('users')
	else:
		os.chdir('lexninja')

        # Do we have a users directory?
        if not os.path.exists('users'):
        	os.mkdirs('users')
        	os.chdir('users')
        else:
        	os.chdir('users')

    return get_user()
    
# Find out if a username is already taken.
def username_taken(test_name):
	if os.path.exists(test_name):
		return True
	else:
		return False

# Prompt for a new username.
# Goto /users/ dir and make new user dir
def get_user():
    username = input("Please enter your username, or make a new one: ")

    # Set limits on username input.
    if len(username) > 25:
    	print("Usernames must be under 25 characters, try again.")
    	return get_user()

    # Remove username whitespace for directory naming.
    username = ''.join(username.split())
    
    # If the username is new (not taken), make a directory for this user.
    if not username_taken(username):

        # Make new user directory and change into it.
        os.mkdirs(username)
        os.chdir(username)
    
        # Make a new saved games directory for this new user,
        # but don't change into it here.
        os.mkdirs('saved_games')

        # get_user return True
        return True

    # Username exists, so we just jump into their username directory
    else:
    	os.chdir(username)
    	return True
