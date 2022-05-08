from turtle import Turtle


FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(x=-280, y=260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.level}", font=FONT)

    def increase_level(self):
        self.clear()
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center",  font=FONT)





