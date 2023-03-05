from turtle import Turtle

STARTING_POSITION = (0, -300)


class Net(Turtle):
    def __init__(self):
        super().__init__(shape="square")
        self.hideturtle()
        self.draw_net()

    def draw_net(self):
        self.pen(pencolor="white", speed=9)
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        while self.ycor() < 300:
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(15)
