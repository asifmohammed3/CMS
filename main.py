import sys
from signup import new_account
from signin import login
from forgot_password import forgot_password


def display():
    valid = False
    while not valid:
        print('Choose one; ')
        prompt = input('1. Create an account. \n2. Already have an account? Login. \n3. Forgot Password \n4. Quit \n:')
        if prompt == '1':
            new_account()
        elif prompt == '2':
            login()
        elif prompt == '3':
            forgot_password()
        elif prompt == '4':
            sys.exit(1)
        else:
            print('Invalid Input! ')


# ---------------------------------------------- Main Body -----------------------------------------------------------

display()
