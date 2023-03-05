from turtle import Turtle

STARTING_POSITION = (0, -280)
FINISH_POSITION = (0, 280)
MOVE_DISTANCE = 20


class Player(Turtle):
    def __init__(self):
        super().__init__(shape="turtle")
        self.setheading(90)
        self.penup()
        self.restart()

    def move_up(self):
        self.goto(0, self.ycor() + MOVE_DISTANCE)

    def move_down(self):
        self.goto(0, self.ycor() - MOVE_DISTANCE)

    def restart(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.position() >= FINISH_POSITION:
            return True
        else:
            return False
