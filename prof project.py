

# pong game :D


import turtle
import winsound

# Paddle Movement


def paddle_A_up():
    y = paddle_A.ycor()
    y += 20
    paddle_A.sety(y)


def paddle_A_down():
    y = paddle_A.ycor()
    y -= 20
    paddle_A.sety(y)


def paddle_B_up():
    y = paddle_B.ycor()
    y += 20
    paddle_B.sety(y)


def paddle_B_down():
    y = paddle_B.ycor()
    y -= 20
    paddle_B.sety(y)


# Window
win = turtle.Screen()
win.title("Yikadee Pong")
win.bgpic("low-tier-god.gif")
win.setup(width=800, height=600)
win.tracer(0)

# Left Paddle
paddle_A = turtle.Turtle()
paddle_A.speed(0)
paddle_A.shape('square')
paddle_A.color('black')
paddle_A.shapesize(stretch_wid=5, stretch_len=1)
paddle_A.penup()
paddle_A.goto(-350, 0)

# Right Paddle
paddle_B = turtle.Turtle()
paddle_B.speed(0)
paddle_B.shape('square')
paddle_B.color('pink')
paddle_B.shapesize(stretch_wid=5, stretch_len=1)
paddle_B.penup()
paddle_B.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('red')
ball.penup()
ball.goto(0, 0)
ball.dx = 0.11
ball.dy = 0.11

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('purple')
pen.penup()
pen.hideturtle()
pen.goto(0, 265)
pen.write("Player A: 0 Player B: 0", align='center',
          font=('Comic Sans MS', 24, 'normal'))

# Score
score_a = 0
score_b = 0


# Keyboard Stuff wont work with caps lock on dont troll
win.listen()
win.onkeypress(paddle_A_up, 'w')
win.onkeypress(paddle_A_down, 's')
win.onkeypress(paddle_B_up, '8')
win.onkeypress(paddle_B_down, '2')


# Main Game Loop :D
while True:
    win.update()

    # Ball Movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checks
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("GahDuu.WAV", winsound.SND_ASYNC)

    if ball.ycor() < - 290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("GahDuu.WAV", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b),
                  align='center', font=('Comic Sans MS', 24, 'normal'))
        winsound.PlaySound("Yikadeee.WAV", winsound.SND_ASYNC)

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b),
                  align='center', font=('Comic Sans MS', 24, 'normal'))
        winsound.PlaySound("Yikadeee.WAV", winsound.SND_ASYNC)

    # Paddle Colisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_B.ycor() + 40) and (ball.ycor() > paddle_B.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_A.ycor() + 40) and (ball.ycor() > paddle_A.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
