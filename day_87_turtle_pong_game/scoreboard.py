from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-350, 260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="left", font=("Courier", 18, "bold"))

    def increase_score(self):
        self.score += 10
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "bold"))

    def you_win(self):
        self.goto(0, 0)
        self.write("YOU WIN!", align="center", font=("Courier", 24, "bold"))
