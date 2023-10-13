import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

title = "Guess the State"
states_questions = 50
score = 0
score_title = f"{score}/{states_questions} States correct"


turtle.shape(image)

country = turtle.Turtle()
country.hideturtle()


# Step 1. Prompt the user for a state.
while True:
    answer_state = screen.textinput(title=title, prompt="What's another state's name? ").title()

    data = pandas.read_csv("50_states.csv")
    states = data.state.dropna().unique()

    # If answer_state exists in dataset, get the row of info.
    for state in states:
        if answer_state == state:
            state_details = data[data.state == answer_state]
            x_cor = int(state_details.x)
            y_cor = int(state_details.y)
            country.penup()
            country.setpos(x_cor, y_cor)
            country.write(answer_state)

            # Set new title to track score
            score += 1

            score_title = f"{score}/{states_questions} States correct"
    title = score_title



screen.exitonclick()