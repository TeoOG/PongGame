import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
# Change screen background color
screen.bgcolor("black")
# Set window title
screen.title("Pong Game")

screen.tracer(0)

r_paddle = Paddle(starting_x=350, starting_y=0, color="red")
l_paddle = Paddle(starting_x=-350, starting_y=0, color="blue")
ball = Ball()
scoreboard = Scoreboard()

# Listening for input here
screen.listen()
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")

for w_key in ["w", "W"]:
    screen.onkeypress(l_paddle.move_up, w_key)
for s_key in ["s", "S"]:
    screen.onkeypress(l_paddle.move_down, s_key)

game_is_on = True
while game_is_on:

    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with both of the paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when r_paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect when the l_paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
