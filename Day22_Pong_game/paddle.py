from turtle import Turtle

L_STARTING_POSITION = (-350, 0)
R_STARTING_POSITION = (350, 0)
MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__(shape="square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def move_up(self):
        if self.ycor() < 260:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def move_down(self):
        if self.ycor() > -260:
            new_y = self.ycor() - MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def restart(self):
        if self.xcor() == -350:
            self.goto(L_STARTING_POSITION)
        else:
            self.goto(R_STARTING_POSITION)
