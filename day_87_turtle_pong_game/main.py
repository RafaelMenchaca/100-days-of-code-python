from turtle import Screen
from paddle import Paddle
from ball import Ball
from brick import Brick
from scoreboard import Scoreboard
import time

# Setup screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout Game 🎮")
screen.tracer(0)

# Create paddle
paddle = Paddle((0, -250))

# Create ball
ball = Ball()

# Create scoreboard
scoreboard = Scoreboard()

# Create bricks
bricks = []
colors = ["red", "orange", "yellow", "green", "blue"]
y_positions = [250, 230, 210, 190, 170]

for i, color in enumerate(colors):
    y = y_positions[i]
    for x in range(-350, 400, 70):
        brick = Brick((x, y), color)
        bricks.append(brick)

# Paddle movement
screen.listen()
screen.onkeypress(paddle.go_left, "Left")
screen.onkeypress(paddle.go_right, "Right")

# Game loop
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Bounce off walls
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()
    if ball.ycor() > 280:
        ball.bounce_y()

    # Bounce off paddle
    if ball.distance(paddle) < 50 and ball.ycor() < -230:
        ball.bounce_y()

    # Detect collision with brick
    for brick in bricks:
        if ball.distance(brick) < 30:
            brick.destroy()
            bricks.remove(brick)
            ball.bounce_y()
            scoreboard.increase_score()
            break

    # Detect ball out of bounds
    if ball.ycor() < -300:
        scoreboard.game_over()
        game_is_on = False

    # Win condition
    if not bricks:
        scoreboard.you_win()
        game_is_on = False

screen.exitonclick()
