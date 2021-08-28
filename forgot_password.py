import json
import sys
from otp import send_otp_as_mail, send_notification_for_password_change
from signup import alphanumeric
from hashing import hash_password


new_pass = ''


def forgot_password():
    global new_pass
    try:
        with open('user_data.json', 'r') as read_data:
            data = json.load(read_data)
    except FileNotFoundError:
        print('Please create an account first! ')
        sys.exit(4)

    username_to_check = input('Username: ')
    if username_to_check in data:
        email = data[username_to_check][2]
        email_hidden = email.split('@')[0]
        send_otp_as_mail(email, username=username_to_check)
        print('We\'ve sent an OTP to ' + email_hidden[0] + '*' * (len(email_hidden) - 3) + email_hidden[len(email_hidden) - 2] +
              email_hidden[len(email_hidden) - 1] + '@gmail.com')

        with open('otp.json', 'r') as read_otp:
            sent_otp = json.load(read_otp)

        chance = 4
        while chance > 0:

            user_otp = input('OTP: ')
            if int(user_otp) == sent_otp[username_to_check]:
                print('Verified! You can now change your password.')

                proceed = False
                while not proceed:
                    sub_proceed = False
                    while not sub_proceed:
                        new_pass = input("Please enter a new Password: ")
                        if alphanumeric(new_pass) and len(new_pass) > 8:
                            sub_proceed = True
                        else:
                            print('Password should contain both Alphabets and Numbers and should be greater than 8 '
                                  'characters.')

                    confirm_pass = input("Confirm Password: ")

                    if new_pass != confirm_pass:
                        print('Passwords doesn\'t match! ')
                    else:
                        proceed = True
                        send_notification_for_password_change(email)

                        with open('user_data.json', 'r') as read_data:
                            user_data = json.load(read_data)
                        user_data[username_to_check][3] = hash_password(new_pass)

                        with open('user_data.json', 'w') as write_data:
                            json.dump(user_data, write_data)

                        print('Successfully Changed! ')
                        sys.exit(1)

            else:    # TODO: INTENSIVE CHECK!
                chance -= 1
                print(f'Wrong OTP! You\'ve got {chance} chances left.')
                if chance == 0:
                    print('Have a nice day! ')
                    sys.exit(2)

    else:
        print('Sorry, Account not found! ')
