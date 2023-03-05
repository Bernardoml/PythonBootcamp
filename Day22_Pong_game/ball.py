from turtle import Turtle

MOVE_DISTANCE = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.color("white")
        self.width(20)
        self.penup()
        self.x_move = MOVE_DISTANCE
        self.y_move = MOVE_DISTANCE
        self.move_speed = 0.1

    def restart(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_paddle()

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_wall(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -1.0
        self.move_speed *= 0.9
