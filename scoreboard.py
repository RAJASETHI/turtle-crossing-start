from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.count = 1
        self.pencolor("black")
        self.goto(-130, 260)
        self.hideturtle()
        self.write(f"Level: {self.count}  MAX:10", False, "center", font=FONT)

    def increment(self):
        self.clear()
        self.count += 1
        self.write(f"Level: {self.count}  MAX:10", False, "center", font=FONT)

    def over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", font=FONT)
