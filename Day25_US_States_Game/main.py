import pandas as pd
from turtle import Screen
import writer as w

IMG = "blank_states_img.gif"
CSV = "50_states.csv"

screen = Screen()
screen.setup(width=725, height=491, startx=2300)
screen.bgpic(IMG)
screen.title("US States Game 2k23")
screen.tracer(0)

data = pd.read_csv(CSV)
all_states = data.state.to_list()
guessed_states = []
writer = w.Writer()
score = 0

while len(guessed_states) < 50:
    screen.update()

    answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                              prompt=f"What's another state name?").title()

    if answer == "Exit":
        # Using a for loop
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)

        # Using list comprehension
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer in all_states:
        guessed_states.append(answer)
        state_data = data[data.state == answer]
        writer.write_state(state_name=answer, state_position=(int(state_data.x), int(state_data.y)))

writer.game_over()
screen.exitonclick()
