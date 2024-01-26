from turtle import Screen
from paddle import Paddle
from ball import Ball
from bricks import Brick
from random import randint
import time

#SCREEN SETUP
screen = Screen()
screen.bgcolor("black")
screen.setup(width=1000, height=600)
screen.title("Breakout Game")
screen.tracer(0)


#INITIATING FUNCTIONS
paddle = Paddle((0, -260))

ball = Ball()

# Create bricks
bricks = []
brick_colors = ["red", "orange", "yellow", "green", "blue"]
rows = 8
brick_width = 60
brick_height = 20

for row in range(rows):
    for i in range(12):
        brick = Brick(brick_colors[randint(0, 4)], brick_width, brick_height)
        brick.set_position(-450 + (i * 80), 280 - (row * brick_height * 1.5))
        # brick.set_position(-450 + (i * 80), 280 - (row * brick_height * 1.5))
        bricks.append(brick)

screen.listen()
screen.onkeypress(paddle.go_left, "Left")
screen.onkeypress(paddle.go_right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280:
        ball.bounce_y()

    if ball.xcor() > 480 or ball.xcor() < -480:
        ball.bounce_x()

    if ball.distance(paddle) < 50 and ball.ycor() < -240:
        ball.bounce_y()

    if ball.ycor() < - 280:
        ball.reset_position()

    for brick in bricks:
        if ball.distance(brick) < 30:
            ball.bounce_y()
            bricks.remove(brick)
            brick.clear()


screen.mainloop()
