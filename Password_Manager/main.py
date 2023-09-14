from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_numbers + password_letters + password_symbols
    random.shuffle(password_list)

    rnd_password = "".join(password_list)

    password.delete(0,END)
    password.insert(0, rnd_password)

    pyperclip.copy(rnd_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def clear():
    website.delete(0, END)
    password.delete(0, END)


def save():
    web = website.get()
    email = user.get()
    pwd = password.get()

    if len(web) == 0 or len(pwd) == 0:
        messagebox.showwarning(title='Warning', message="Enter all the required Fields")
    else:
        messagebox.askokcancel(title=f'{web}', message=f"Details Entered: \nEmail : {email}"
                                                       f"\nPassword : {pwd}\nOk to Save?")
        with open('data.txt', mode='a') as saved:
            saved.write(f" Website: {web} | email: {email} | password: {pwd}\n")
            clear()
        # messagebox.showinfo("Details Copied to ClipBoard")


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

website = Entry(width=46)
website.grid(column=1, row=1, columnspan=2)
website.focus()

user = Entry(width=46)
user.grid(column=1, row=2, columnspan=2)
user.insert(0, "example@gmail.com")

password = Entry(width=28)
password.grid(column=1, row=3)

button1 = Button(text='Generate Password', command=generate)
button1.grid(column=2, row=3)

button2 = Button(text='Add', width=46, command=save)
button2.grid(column=1, row=4, columnspan=2)

# with open('data.txt', mode='a') as save:
#     save.append(add())

window.mainloop()
