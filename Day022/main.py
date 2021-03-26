from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()
sleep_time = 0.1


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(sleep_time)
    ball.move()
    # Detect collision with the wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # Detect collision with the paddle
    if ball.xcor() > 330 and ball.distance(r_paddle) < 50 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    #  Detect a right miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        sleep_time *= 0.9

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        sleep_time *= 0.9




    screen.update()


screen.exitonclick()