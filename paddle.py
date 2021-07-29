from turtle import Turtle

move_distance = 20

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("red")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.setheading(90)
        self.penup()
        self.goto(position)


    def paddle_up(self):
        self.setheading(90)
        self.forward(move_distance)

    def paddle_down(self):
        self.setheading(270)
        self.forward(move_distance)

