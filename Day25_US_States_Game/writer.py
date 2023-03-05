from turtle import Turtle

TIMER_POSITION = (360, 230)
ALIGNMENT = "center"
FONT = ("Arial", 10, "normal")


class Writer(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()

    def write_state(self, state_name, state_position):
        self.goto(state_position)
        self.write(f"{state_name}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"Congratulations!", False, align="center", font=("Arial", 40, "normal"))
