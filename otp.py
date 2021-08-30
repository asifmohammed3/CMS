import random
import json
import smtplib

MY_EMAIL = "secureotpcms@gmail.com"
MY_PASSWORD = ''


def generate_otp():
    otp = random.randint(100000, 999999)
    return otp


def save_otp(username, otp):
    otp_dict = {username: otp}
    try:
        with open('otp.json', 'r') as saving_file:
            data = json.load(saving_file)

    except FileNotFoundError:
        with open('otp.json', 'w') as saving_file:
            json.dump(otp_dict, saving_file, indent=4)
    else:
        data.update(otp_dict)
        with open('otp.json', 'w') as saving_file:
            json.dump(data, saving_file, indent=4)


def send_otp_as_mail(gmail, username):
    otp = generate_otp()
    save_otp(username, otp)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=gmail,
            msg=f"Your OTP is {otp}".encode('utf-8')
        )


def send_notification_for_password_change(gmail):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=gmail,
            msg=f"Subject:Security Alert\n\nYour Password has been changed.".encode('utf-8')
        )
