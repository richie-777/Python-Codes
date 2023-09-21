import time
from tkinter import *
from data import question_data
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.score = Label(text="score : 0", fg="White", bg=THEME_COLOR, font=("Arial", 15, 'normal'), pady=20)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=500, height=500, bg="White")
        self.question_text = self.canvas.create_text(250, 250, text="Hello",
                                                     fill=THEME_COLOR, font=("Arial", 20, "italic"), width=490)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        green_img = PhotoImage(file="./images/true.png")
        self.green_button = Button(image=green_img, highlightthickness=0, pady=50, command=self.true_pressed)
        self.green_button.grid(row=2, column=1)
        red_img = PhotoImage(file="./images/false.png")
        self.red_button = Button(image=red_img, highlightthickness=0, pady=50, command=self.false_pressed)
        self.red_button.grid(row=2, column=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="White")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score : {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the Quiz!")
            self.green_button.config(state="disabled")
            self.red_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="Green")
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.config(bg="Red")
            self.window.after(1000, self.get_next_question)
