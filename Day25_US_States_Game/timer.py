from turtle import Turtle
import time

TIMER_POSITION = (320, 210)
ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")


class Timer(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.seconds = 600

    def countdown(self):
        if self.seconds > 0:
            self.seconds -= 1
            time.sleep(1)
            self.show_timer()

    def show_timer(self):
        self.goto(TIMER_POSITION)
        self.clear()
        timer = divmod(self.seconds, 60)
        self.write(f"{timer[0]}:{timer[1]}", False, align=ALIGNMENT, font=FONT)
