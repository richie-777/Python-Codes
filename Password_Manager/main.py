from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_numbers + password_letters + password_symbols
    random.shuffle(password_list)

    rnd_password = "".join(password_list)

    password.delete(0, END)
    password.insert(0, rnd_password)

    pyperclip.copy(rnd_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def clear():
    website_entry.delete(0, END)
    password.delete(0, END)


def save():
    web = website_entry.get().lower()
    email = user.get()
    pwd = password.get()

    new_data = {
        web: {
            'email': email,
            'password': pwd,
        }
    }

    if len(web) == 0 or len(pwd) == 0:
        messagebox.showwarning(title='Warning', message="Enter all the required Fields")
    else:

        try:
            with open('data.json', mode='r') as saved:
                # read old data
                data = json.load(saved)
        except FileNotFoundError:
            with open('data.json', mode='w') as saved:
                json.dump(new_data, saved, indent=4)
        else:
            # update old data with new data
            data.update(new_data)

            with open('data.json', mode='w') as saved:
                # saving updated data
                json.dump(data, saved, indent=4)
        finally:
            clear()


# ---------------------------- PASSWORD FINDER ------------------------------- #
def password_finder():
    website = website_entry.get().lower()
    try:
        with open('data.json') as saved:
            data = json.load(saved)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='No Data File found')

    else:
        if website in data:
            email = data[website]['email']
            pwd = data[website]['password']
            messagebox.showinfo(title=website, message=f'Email : {email}\nPassword : {pwd}\n')
        else:
            messagebox.showinfo(title="Error", message=f'No details for {website} Exists')


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

label1 = Label(text="Website:")
label1.grid(column=0, row=1)

label2 = Label(text="Email/Username:")
label2.grid(column=0, row=2)

label3 = Label(text="Password:")
label3.grid(column=0, row=3)

website_entry = Entry(width=28)
website_entry.grid(column=1, row=1, columnspan=1)
website_entry.focus()

user = Entry(width=46)
user.grid(column=1, row=2, columnspan=2)
user.insert(0, "example@gmail.com")

password = Entry(width=28)
password.grid(column=1, row=3)

button1 = Button(text='Generate Password', command=generate)
button1.grid(column=2, row=3)

button2 = Button(text='Add', width=46, command=save)
button2.grid(column=1, row=4, columnspan=4)

button3 = Button(text='Search', width=16, command=password_finder)
button3.grid(column=2, row=1, columnspan=2)

window.mainloop()
