from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self,hiscore):
        super().__init__()
        self.score = 0
        self.hiscore = hiscore
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score} High Score: {self.hiscore}", align="center", font=("Arial", 8, "normal"))
        self.hideturtle()

    def check_hiscore(self):
        return self.score > self.hiscore

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.hiscore}", align="center", font=("Arial", 8, "normal"))

    def reset(self):
        if self.check_hiscore():
            self.hiscore = self.score
        self.score = 0
        self.update_score()

    def new_score(self):
        self.score +=1
        self.update_score()
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align="center", font=("Arial", 8, "normal"))
