from turtle import Turtle


font =("Courier", 15, "normal")

class Score(Turtle):
    def __init__(self, x, alignment):
        super().__init__()
        self.count_score = 0
        self.hideturtle()
        self.color("purple")
        self.penup()
        self.goto(x, 270)

        self.write(arg= f"Score  {self.count_score}" , move=False, align=alignment
                   , font=font)
        self.alignment = alignment
    def get_point(self):
        self.clear()
        self.count_score += 1
        self.write(arg=f"Score {self.count_score}", move=False, align=self.alignment
                   , font=font)
    def game_over(self, winner):
        self.goto(0, 0)
        self.write(arg=f"Game over\nWinner is {winner}", move=False, align="center"
                   , font=font)