import turtle as t

START_POSITION = (-220, 260)
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.goto(START_POSITION)
        self.speed("fastest")
        self.color("black")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", False, align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0, 50)
        self.write(f"GAME OVER", False, align=ALIGNMENT, font=FONT)
        self.goto(0, -50)
        self.write(f"Final Level: {self.level}", False, align=ALIGNMENT, font=FONT)