import turtle
import time
import random

# Setup the screen 
wn = turtle.Screen()
wn.title("Space Invaders - Turtle Edition")
wn.bgcolor("black")
wn.setup(width=700, height=700)
wn.tracer(0)

# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
for side in range(4):
    border_pen.forward(600)
    border_pen.left(90)
border_pen.hideturtle()

# Score display 
score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 260)
score_pen.write(f"Score: {score}", False, align="left", font=("Courier", 14, "normal"))
score_pen.hideturtle()

#  Player setup 
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setheading(90)
player.setposition(0, -250)
player_speed = 15

# Bullet setup 
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()
bullet_speed = 20
bullet_state = "ready" 

#  Aliens setup 
num_aliens = 6
aliens = []

for i in range(num_aliens):
    alien = turtle.Turtle()
    alien.color("red")
    alien.shape("circle")
    alien.penup()
    alien.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    alien.setposition(x, y)
    aliens.append(alien)

alien_speed = 3

# Player movement 
def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += player_speed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    global bullet_state
    if bullet_state == "ready":
        bullet_state = "fire"
        bullet.setposition(player.xcor(), player.ycor() + 10)
        bullet.showturtle()

# Collision check 
def is_collision(t1, t2):
    distance = t1.distance(t2)
    return distance < 20

# Keyboard bindings 
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(fire_bullet, "space")

#Game loop 
game_over = False

while not game_over:
    wn.update()

    # Move aliens
    for alien in aliens:
        x = alien.xcor()
        x += alien_speed
        alien.setx(x)

        # Bounce aliens and move them down
        if alien.xcor() > 280 or alien.xcor() < -280:
            alien_speed *= -1
            for a in aliens:
                a.sety(a.ycor() - 30)

        # Check for collision with bullet
        if is_collision(bullet, alien):
            bullet.hideturtle()
            bullet_state = "ready"
            bullet.setposition(0, -400)
            alien.setposition(random.randint(-200, 200), random.randint(100, 250))
            score += 10
            score_pen.clear()
            score_pen.write(f"Score: {score}", False, align="left", font=("Courier", 14, "normal"))

        # Check for collision with player
        if is_collision(player, alien) or alien.ycor() < -250:
            player.hideturtle()
            alien.hideturtle()
            score_pen.setposition(-50, 0)
            score_pen.write("GAME OVER", False, align="center", font=("Courier", 30, "bold"))
            game_over = True
            break

    # Move bullet
    if bullet_state == "fire":
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)

        # Check if bullet leaves screen
        if bullet.ycor() > 275:
            bullet.hideturtle()
            bullet_state = "ready"

    time.sleep(0.02)

wn.mainloop()
