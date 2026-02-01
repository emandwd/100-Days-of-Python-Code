import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

# def get_mouse_click_coor(x,y):
    # print(x,y)
# turtle.onscreenclick(get_mouse_click_coor) # When the user clicks on the screen, it will call your function get_mouse_click_coor(x, y) with the coordinates of the click.
# turtle.mainloop()
# screen.exitonclick() # This waits for one click, then closes the turtle window so we don't need it

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title= f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    print(answer_state)


    if answer_state == "Exit": # We don't need this line : screen.exitonclick()
        missing_states = [state for state in all_states if item not in guessed_states]
        # missing_states = []
        # for state in all_states:
            # if state not in guessed_states:
                # missing_states.append(state)
        # print(missing_states)
        """ To convert the list of missing states into a CSV file, we create a new data frame from missing_states. This data frame will have a single column containing the state names. Once created, we save this data frame as a CSV file named states_to_learn.csv. """
        new_data = pandas.DataFrame(missing_states) # data frame is created
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item()) # item is a method in the panda series -> it return the first element


