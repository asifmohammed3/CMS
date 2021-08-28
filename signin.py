import json
import sys
import hashing


def check_if_user_exists(name):
    try:
        with open('user_data.json', 'r') as read:
            data = json.load(read)
    except FileNotFoundError:
        print('Please consider signing up for an account first! ')
        sys.exit(4)  # TODO: ASIF, CHANGE IT INTO SIGNUP FUNCTION.
    else:
        if name in data:
            return True
        else:
            return False


def correct_password(username, password):
    try:
        with open('user_data.json', 'r') as read:
            data = json.load(read)
    except FileNotFoundError:
        print('Please consider signing up for an account first! ')
        sys.exit(4)  # TODO: ASIF, CHANGE IT INTO SIGNUP FUNCTION.
    else:
        if hashing.check_password(data[username][3], password):
            return True
        else:
            return False


def login():
    try:
        with open('user_data.json', 'r') as read:
            data = json.load(read)
    except FileNotFoundError:
        print('Please consider signing up for an account first! ')
        sys.exit(4)  # TODO: ASIF, CHANGE IT INTO SIGNUP FUNCTION.
    else:
        valid = False
        while not valid:
            username = input('Please enter your Username: ')
            if check_if_user_exists(username):
                password = input('Please enter your Password: ')
                # hashed_user_entered_pass = hashing.hash_password(password)
                if correct_password(username, password):
                    print(f'Welcome back, {data[username][0]}! ')
                    valid = True
                else:
                    print('Wrong Password, Try again!')
            else:
                print('Username Doesn\'t exist! ')
