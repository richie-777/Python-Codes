import pandas as pd
import smtplib
import random
from datetime import datetime


USER_NAME = "example@gmail.com"
PASSWORD = "example"

today = datetime.now()
today_tuple = (today.month, today.day)


df = pd.read_csv('birthday.csv')
new_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in df.iterrows()}

if today_tuple in new_dict:
    birthday_person = new_dict[today_tuple]
    file_path = f"letter_templates/letter{random.randint(1,3)}.txt"
    with open(file_path) as file:
        text = file.read()
        text = text.replace("[name]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=USER_NAME, password=PASSWORD)
        connection.sendmail(from_addr=USER_NAME,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject: Happy Birthday!\n\n{text}")







