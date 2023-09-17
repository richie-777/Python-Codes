import random
from tkinter import *
import pandas as pd
import time


# ----------------------------------------------- #
df = pd.read_csv('data/German_Words.csv')
word_dict = df.to_dict(orient="records")
rand_word = {}

# ----------------------------------------------- #

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv('data/German_Words.csv')
    word_dict = original_data.to_dict(orient="records")
else:
    word_dict = data.to_dict(orient="records")


def next_card():
    global rand_word, flip_timer
    windows.after_cancel(flip_timer)

    rand_word = random.choice(word_dict)

    canvas.itemconfig(trans_title, text="German", fill="black")
    canvas.itemconfig(trans_text, text=f"{rand_word['German']}", fill="black")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = windows.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(trans_title, text="English", fill="White")
    canvas.itemconfig(trans_text, text=f'{rand_word["English"]}', fill="White")
    canvas.itemconfig(card_background, image=card_back)


def is_known():
    word_dict.remove(rand_word)
    print(len(word_dict))
    next_card()
    data = pd.DataFrame(word_dict)
    data.to_csv("data/words_to_learn.csv", index=False)


# ---------------------------------------------- #

BACKGROUND_COLOR = "#B1DDC6"

windows = Tk()
windows.title = "Flash Card Game"
windows.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = windows.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR)

card_front = PhotoImage(file='./images/card_front.png')
card_back = PhotoImage(file='./images/card_back.png')

card_background = canvas.create_image(400, 260,image=card_front)
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)

trans_title = canvas.create_text(400, 150, text="Lang", font=('Ariel', 40, "italic"))
trans_text = canvas.create_text(400, 265, text="Word", font=('Ariel', 40, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

green_img = PhotoImage(file="./images/right.png")
green_button = Button(image=green_img, highlightthickness=0, pady=50, command=is_known)
green_button.grid(row=1, column=1)

red_img = PhotoImage(file="./images/wrong.png")
red_button = Button(image=red_img, highlightthickness=0, pady=50, command=next_card)
red_button.grid(row=1, column=0)

next_card()


windows.mainloop()
