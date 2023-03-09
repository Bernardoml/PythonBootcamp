import os
import smtplib
import datetime as dt
import random
from dotenv import load_dotenv
import pandas

load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("PASSWORD")
PLACEHOLDER = "[NAME]"

# ------------------------- Extra Hard Starting Project -------------------------
# 1. Update the birthdays.csv - DONE
# 2. Check if today matches a birthday in the birthdays.csv
today_tuple = (dt.datetime.now().month, dt.datetime.now().day)

# Using dict comprehension to create a dict formatted like this:
# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
# }
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME]
    # with the person's actual name from birthdays.csv
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"

    with open(file_path) as letter_file:
        letter = letter_file.read()
        email_body = letter.replace(PLACEHOLDER, birthday_person["name"])

    # 4. Send the letter generated in step 3 to that person's email address.

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday!!!\n\n{email_body}"
        )
