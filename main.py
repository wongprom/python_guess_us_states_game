import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
state_text = turtle.Turtle()
state_text.pencolor("red")

states_data = pandas.read_csv("50_states.csv")
guessed_stats = []


while len(guessed_stats) < 50:
    answer_state = screen.textinput(title=f"Guess the State {len(guessed_stats)}/{len(states_data)}", prompt="Whats another state name?").title()

    for state in states_data.state:
        if state == answer_state:
            correct_state_row_data = states_data[states_data.state == answer_state]
            x_corr = int(correct_state_row_data.x.iloc[0])
            y_corr = int(correct_state_row_data.y.iloc[0])

            state_text.goto(x_corr, y_corr)
            state_text.write(answer_state)
            guessed_stats.append(answer_state)


# Get coor when click on image
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
#
screen.exitonclick()