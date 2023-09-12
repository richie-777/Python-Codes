import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
img = 'blank_states_img.gif'
screen.addshape(img)
turtle.shape(img)

data = pandas.read_csv('50_states.csv')
state_data = data['state'].to_list()
guessed = []

while len(guessed) < 50:
    answer = screen.textinput(title=f"{len(guessed)}/50 states are correct", prompt="Next state's name?").title()

    if answer == "exit".title():
        missing_st = [st for st in state_data if st not in guessed]
        new_data = pandas.DataFrame(missing_st)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer in state_data:
        guessed.append(answer)
        tim = turtle.Turtle()
        tim.ht()
        tim.pu()
        st = data[data['state'] == answer]
        tim.goto(int(st.x), int(st.y))
        tim.write(st.state.item())

screen.exitonclick()
