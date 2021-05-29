# import smtplib
#
# my_email = "buddychaddi76@gmail.com"
# password = "Qwer@123"
# connection = smtplib.SMTP("smtp.gmail.com", 587)
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs=my_email,msg="Subject:Hello\n\n this is the message")
# connection.close()

import smtplib
import datetime as dt
import random

my_email = "buddychaddi76@gmail.com"
password = "Qwer@123"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 5:
    with open('quotes.txt') as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)
        print(quote)
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(my_email,password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:Monday motivation\n\n{quote}")