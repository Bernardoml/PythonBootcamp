import turtle as t

START_POSITION = (0, 270)
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")
MY_FILE = 'data.txt'


class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(MY_FILE) as data:
            self.high_score = int(data.read())
        self.high_score = 0
        self.hideturtle()
        self.goto(START_POSITION)
        self.speed("fastest")
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(MY_FILE, mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
