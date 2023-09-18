import smtplib
import datetime as dt
import random


rand_quotes = []


def quote_generator():
    with open('quotes.txt') as data:
        quotes = data.readlines()
        global rand_quotes
        rand_quotes = random.choice(quotes)
        print(rand_quotes)


def send_mail():
    quote_generator()
    my_email = "example@gmail.com"
    password = "example"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=["example@gmail.com"],
                            msg=f"Subject:Sunday Motivation\n\n {rand_quotes}")


now = dt.datetime.now()
week = now.weekday()
print(week)
if week == 0:
    send_mail()
