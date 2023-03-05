from turtle import Turtle

START_POSITION = (0, 240)
ALIGNMENT = "center"
FONT = ("Courier", 35, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.goto(START_POSITION)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.l_score}   {self.r_score}", False, align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0, 50)
        self.write(f"GAME OVER", False, align=ALIGNMENT, font=FONT)
        self.goto(0, -50)
        self.write(f"{self.l_score}   {self.r_score}", False, align=ALIGNMENT, font=FONT)
