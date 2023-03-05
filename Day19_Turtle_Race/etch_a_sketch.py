import turtle as t

tim = t.Turtle()
screen = t.Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.back(10)


def rotate_left():
    tim.left(5)


def rotate_right():
    tim.right(5)


def reset_screen():
    tim.reset()


screen.listen()
screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=rotate_left, key="a")
screen.onkey(fun=rotate_right, key="d")
screen.onkey(fun=reset_screen, key="c")

screen.exitonclick()
