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
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"Guess the State {len(guessed_states)}/{len(states_data)}", prompt="Whats another state name?").title()

    if answer_state == "Exit":
        study_these_states = []
        states_list = states_data.state.to_list()
        for state_list in states_list:
            if state_list not in guessed_states:
                study_these_states.append(state_list)
        study_data_frame = {
            f"state, {len(study_these_states)}": study_these_states,
        }
        df = pandas.DataFrame(study_data_frame)
        df.to_csv("states_to_learn.csv")

    for state in states_data.state:
        if state == answer_state:
            correct_state_row_data = states_data[states_data.state == answer_state]
            x_corr = int(correct_state_row_data.x.iloc[0])
            y_corr = int(correct_state_row_data.y.iloc[0])

            state_text.goto(x_corr, y_corr)
            state_text.write(answer_state)
            guessed_states.append(answer_state)


# Get coor when click on image
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
#
# screen.exitonclick()