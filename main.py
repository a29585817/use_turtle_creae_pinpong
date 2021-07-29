from turtle import Screen
import time

from paddle import Paddle
from ball import Ball
from score import Score

screen = Screen()
screen.setup(width=800, height=600)
# screen.bgcolor("black")
screen.title("My pong game")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
l_score = Score(-200,"left")
r_score = Score(200, "right")


screen.listen()
screen.onkey(l_paddle.paddle_up, "w")
screen.onkey(l_paddle.paddle_down, "s")
screen.onkey(r_paddle.paddle_up, "Up")
screen.onkey(r_paddle.paddle_down, "Down")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        #bounce
        ball.bounce_y()
    if ball.distance(l_paddle) < 60 and ball.xcor() > -320 or ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        l_score.get_point()
    if ball.xcor() < -380:
        ball.reset_position()
        r_score.get_point()

    if r_score.count_score == 3:
        r_score.game_over("Right")
        game_is_on = False
    if l_score.count_score == 15:
        l_score.game_over("Left")
        game_is_on = False

screen.exitonclick()