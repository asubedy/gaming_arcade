import turtle

def main_game(score_A,score_B):
    # Creating the game window
    win = turtle.Screen()
    win.title("Ping Pong")
    win.bgcolor("#000")
    win.setup(width=800, height=600)
    win.tracer(0)
    
    # Drawing the paddles
    # Paddle A
    paddle_A = turtle.Turtle()
    paddle_A.speed(0)
    paddle_A.shape("square")
    paddle_A.color("white")
    paddle_A.shapesize(stretch_wid=5, stretch_len=1)
    paddle_A.penup()
    paddle_A.goto(-350, 0)
    
    # Paddle B
    paddle_B = turtle.Turtle()
    paddle_B.speed(0)
    paddle_B.shape("square")
    paddle_B.color("white")
    paddle_B.shapesize(stretch_wid=5, stretch_len=1)
    paddle_B.penup()
    paddle_B.goto(350, 0)
    
    # Placing the ball
    # Ball
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("square")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 0.2
    ball.dy = 0.2
    
    # Score
    # global score_A  
    # global score_B  
    
    score = turtle.Turtle()
    score.speed(0)
    score.color("white")
    score.penup()
    score.hideturtle()
    score.goto(0, 260)
    score.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))
    
    
    # For the movement of the game objects
    def paddle_a_up():
        y = paddle_A.ycor()
        y += 20
        paddle_A.sety(y)
    
    
    def paddle_a_down():
        y = paddle_A.ycor()
        y -= 20
        paddle_A.sety(y)
    
    
    def paddle_b_up():
        y = paddle_B.ycor()
        y += 20
        paddle_B.sety(y)
    
    
    def paddle_b_down():
        y = paddle_B.ycor()
        y -= 20
        paddle_B.sety(y)
    
    
    # To know the button pressing from the keyboard
    win.listen()
    win.onkeypress(paddle_a_up, "w")
    win.onkeypress(paddle_a_down, "s")
    win.onkeypress(paddle_b_up, "Up")
    win.onkeypress(paddle_b_down, "Down")
    
    
    # End of game
    def game_end():
        end = turtle.Turtle()
        end.speed(0)
        end.color("white")
        end.penup()
        end.hideturtle()
        end.goto(0, 0)
        score.clear()
        paddle_B.goto(-350, 0)
        paddle_A.goto(350, 0)
        ball.goto(0, 0)
        end.write("GAME OVER", align="center", font=("Courier", 60, "normal"))
    

    
    # Main game loop
    while True:
        win.update()

        # Movement of the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Setting Boundary for the ball
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
            #winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
            #winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_A += 1
            score.clear()
            score.write("Player A: {}  Player B: {}".format(score_A, score_B), align="center",
                        font=("Courier", 24, "normal"))

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_B += 1
            score.clear()
            score.write("Player A: {}  Player B: {}".format(score_A, score_B), align="center",
                        font=("Courier", 24, "normal"))

        # Setting boundary for the paddles
        if paddle_A.ycor() > 260:
            paddle_A.sety(250)

        if paddle_A.ycor() < -260:
            paddle_A.sety(-250)

        if paddle_B.ycor() > 260:
            paddle_B.sety(250)

        if paddle_B.ycor() < -260:
            paddle_B.sety(-250)
        # Collision detection
        if (ball.xcor() > 340 and ball.xcor() < 350) and (
                ball.ycor() < paddle_B.ycor() + 40 and ball.ycor() > paddle_B.ycor() - 40):
            ball.setx(340)
            ball.dx *= -1
            #winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        if (ball.xcor() < -340 and ball.xcor() > -350) and (
                ball.ycor() < paddle_A.ycor() + 40 and ball.ycor() > paddle_A.ycor() - 40):
            ball.setx(-340)
            ball.dx *= -1
            #winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        if score_A == 10 or score_B == 10:
            game_end()

#main_game(0,0)