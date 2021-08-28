
import json
import sys
import time
from signin import login
from otp import send_otp_as_mail
import hashing

email_id = ''
new_user = ''
new_pass = ''


def alphanumeric(given):
    return given.isalnum() and not given.isalpha() and not given.isdigit()


def save_data(first_name, last_name, email, username, password):
    new_data = {username: [first_name, last_name, email, password]}
    try:
        with open('user_data.json', 'r') as saving_file:
            data = json.load(saving_file)

    except FileNotFoundError:
        with open('user_data.json', 'w') as saving_file:
            json.dump(new_data, saving_file, indent=4)
    else:
        data.update(new_data)
        with open('user_data.json', 'w') as saving_file:
            json.dump(data, saving_file, indent=4)


def prompts():
    global email_id, new_user, new_pass
    first_name = input('Please enter your First name: ')
    last_name = input('Please enter your Last name: ')

    proceed_one = False
    while not proceed_one:
        email_id = input('Please enter your Email ID: ')
        if '@gmail.com' not in email_id:
            print('Please enter a valid Email ID')
        else:
            proceed_one = True

    proceed_two = False
    while not proceed_two:
        new_user = input("Please enter a new Username: ")
        try:
            with open('user_data.json', 'r') as read:
                data = json.load(read)
        except FileNotFoundError:
            proceed_two = True
        else:
            if new_user in data:
                print('Username already taken! ')
            else:
                proceed_two = True

    proceed_three = False
    while not proceed_three:
        sub_proceed = False
        while not sub_proceed:
            new_pass = input("Please enter a new Password: ")
            if alphanumeric(new_pass) and len(new_pass) > 8:
                sub_proceed = True
            else:
                print('Password should contain both Alphabets and Numbers and should be greater than 8 characters.')
        confirm_pass = input("Confirm Password: ")
        if new_pass != confirm_pass:
            print('Passwords doesn\'t match! ')
        else:
            proceed_three = True

    send_otp_as_mail(email_id, username=new_user)
    print(f'Successful! Please confirm your mail ID, {first_name} ')
    print('We\'ll send an OTP to the registered Mail ID, Please wait...')
    time.sleep(1)
    print('On the way..!')
    time.sleep(2)

    # TODO: ADD A CODE THAT CHECKS IF MAIL IS SENT OR NOT.
    verified = False
    while not verified:
        print()
        user_otp = input('Kindly check your Email for an OTP\nOTP: ')

        with open('otp.json', 'r') as send_otp:
            mail_otp = json.load(send_otp)
        if int(user_otp) == mail_otp[new_user]:
            hashed_pass = hashing.hash_password(new_pass)
            save_data(first_name, last_name, email_id, new_user, hashed_pass)
            print(f'Successfully created an account for {first_name}! ')
            verified = True
        else:
            print('Wrong OTP.')

    login_quit = input('Do you want to login to your account or quit? (Login/Quit): ').lower()
    if login_quit == 'login':
        login()
    elif login_quit == 'quit':
        sys.exit(0)
    else:
        print('Sorry! That\'s an invalid input. ')
        sys.exit(0)


def new_account():
    prompts()
