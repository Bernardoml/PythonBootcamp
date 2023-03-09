# import os
# import smtplib
# from dotenv import load_dotenv
# load_dotenv()

# MY_EMAIL = os.getenv("MY_EMAIL")
# PASSWORD = os.getenv("PASSWORD")
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="bernardoml@hotmail.com",
#         msg="Subject: Test Subject\n\nTesting email body..."
#     )

import datetime as dt

now = dt.datetime.now()
year = now.year
print(now)
print(year)
print(type(year))
month = now.month
day_of_week = now.weekday()
print(month)
print(day_of_week)

date_of_birth = dt.datetime(year=1987, month=8, day=26)