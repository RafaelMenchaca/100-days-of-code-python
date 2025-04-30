import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_date = pandas.DataFrame(missing_states)
        new_date.to_csv("states_to_learn.csv")


        break
    # If answer_state is one of the states in all states of the 50_states.csv
    if answer_state in all_states:
        guessed_states.append(answer_state)
        #if they got it right
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        #Create a turtle to write the name of the state at the state's x and y coordenate
        t.write(answer_state)

#states to learn.csv
