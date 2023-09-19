import time
import requests
import datetime
import smtplib


LATITUDE = 29.681888
LONGITUDE = 90.600594


def overhead():

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()

    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])
    iss_position = (latitude, longitude)

    print(iss_position)
    if LATITUDE-5 <= latitude <= LATITUDE+5 and LONGITUDE-5 <= longitude <= LONGITUDE+5:
        return True


overhead()


def is_night():
    parameters = {
        'lat': LATITUDE,
        'lng': LONGITUDE,
        'formatted': 0,
    }

    response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_night() and overhead():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user="mexample@gmail.com", password="example")

            connection.sendmail(to_addrs="example1@gmail.com", from_addr="example@gmail.com",
                                msg=f"Subject: Look Up \n\nLookUp above"
                                    f" to see the International Space Station!")
