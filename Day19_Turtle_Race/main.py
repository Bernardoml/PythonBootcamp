import turtle as t
import random

screen = t.Screen()
screen.title(titlestring="Turtle Race 2k23")
screen.setup(width=500, height=400)

is_race_on = False
x_start = -220
y_start = 150
turtles = []
colors = ['purple', 'yellow', 'blue', 'pink', 'green', 'orange', 'red']
colors_str = "/".join(colors)

user_bet = screen.textinput(title="Make your bet",
                            prompt=f"Which turtle will win the race?\n"
                                   f"{colors_str} \n"
                                   f"Enter a color:")
print(user_bet)

for i in range(0, len(colors)):
    new_turtle = t.Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=x_start, y=y_start + (-50 * i))
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() >= 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"Congratulations, the {user_bet} turtle won!")
            else:
                print(f"You lost. The {winner} turtle won the race.")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
