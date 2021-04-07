import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")

image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

count = 0

df = pd.read_csv('50_states.csv')

states = df.state.to_list()

correct_answers = []
while len(correct_answers) < 50:
    answer_state = screen.textinput(title=f'{len(correct_answers)}/50 States Correct',
                                    prompt="What's a state's name?").title()
    if answer_state == 'Exit':
        break

    if answer_state not in states:
        continue
    correct_answers.append(answer_state)

    x = int(df[df.state == answer_state].x)
    y = int(df[df.state == answer_state].y)

    answer_state_turtle = turtle.Turtle()
    answer_state_turtle.penup()
    answer_state_turtle.hideturtle()
    answer_state_turtle.goto(x, y)
    answer_state_turtle.write(answer_state)

missing_states = []
for state in states:
    if state not in correct_answers:
        missing_states.append(state)
states_to_learn = pd.DataFrame(missing_states)
states_to_learn.to_csv('states_to_learn.csv')
