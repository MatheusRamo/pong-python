import turtle

#creating the window

width, height = 800,600

window = turtle.Screen()
window.title("Pong")
window.bgcolor("blue")
window.setup(width,height)
window.tracer(0)

# Player A
player_a = turtle.Turtle()
player_a.speed(0)
player_a.shape("square")
player_a.shapesize(stretch_wid=5, stretch_len=1)
player_a.color("yellow")
player_a.penup()
player_a.goto(-350, 0)

# Player B
player_b = turtle.Turtle()
player_b.speed(0)
player_b.shape("square")
player_b.shapesize(stretch_wid=5, stretch_len=1)
player_b.color("yellow")
player_b.penup()
player_b.goto(350, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0,0)

ball.dx = 1
ball.dy = 1



# Functions
def player_a_up():
    y = player_a.ycor()
    y = y + 15
    player_a.sety(y)

def player_a_down():
    y = player_a.ycor()
    y = y - 15
    player_a.sety(y)

def player_b_up():
    y = player_b.ycor()
    y = y + 15
    player_b.sety(y)

def player_b_down():
    y = player_b.ycor()
    y = y - 15
    player_b.sety(y)


# Keyboard Binding
window.listen()
window.onkeypress(player_a_up, "w")
window.onkeypress(player_a_down, "s")
window.onkeypress(player_b_up, "Up")
window.onkeypress(player_b_down, "Down")


#Main game loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy = ball.dy * (-1)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy = ball.dy * (-1)

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx = ball.dx * (-1)

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx = ball.dx * (-1)

    # Colision betewen Ball and Player 
