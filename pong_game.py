

import datetime
import turtle
import winsound
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)



# Score
score_a = 0
score_b = 0





# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 3.5
ball.dy = 3.5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
player_A = turtle.textinput("Welcome", "Enter the name of player A:")
player_B = turtle.textinput("Welcome", "Enter the name of player B:")
pen.write(player_A + " : 0     " + player_B + ": 0",align="center", font=("Courier", 24, "normal"))


# line
line= turtle.Turtle()
line.speed(0)
line .shape("square")
line.color("white")
line.shapesize(stretch_wid=40,stretch_len=0.03)
line.penup()
line.goto(0, 0)

# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()
    
   # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking

    # Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1


    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Left and right
    if ball.xcor() > 350:
        score_a += 1
        pen.clear()
        pen.write(player_A + ":{}     ".format(score_a) + player_B + ":{}".format(score_b), align="center",
                  font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
        winsound.PlaySound("wall sound",winsound.SND_ASYNC)

    elif ball.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write(player_A + ":{}     ".format(score_a) + player_B + ":{}".format(score_b), align="center",
                  font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
        winsound.PlaySound("wall sound",winsound.SND_ASYNC)

    # Paddle and ball collisions
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1
        winsound.PlaySound("wall sound",winsound.SND_ASYNC)


    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
        winsound.PlaySound("wall sound",winsound.SND_ASYNC)

    # Paddles to remain on screen
    if paddle_a.ycor() > 250:
        paddle_a.sety(250)

    if paddle_a.ycor() < -250:
        paddle_a.sety(-250)

    if paddle_b.ycor() > 250:
        paddle_b.sety(250)

    if paddle_b.ycor() < -250:
        paddle_b.sety(-250)

    if score_a >= 3:
        turtle.bye()
        now = datetime.datetime.now()
        a = now.strftime("%Y-%m-%d %H:%M:%S")
        print(a)
        
        print("Game result", "Well done " +  player_A  + " You Won!!" )
        file = open("Game_Results","a")
        file.write(f"\n\n {a} \n\n {player_A} vs {player_B}\nGame Result:\n Well Done {player_A} You Won")
        file.close()
        break
    if score_b >= 3:
        turtle.bye()
        now = datetime.datetime.now()
        a = now.strftime("%Y-%m-%d %H:%M:%S")
        print(a)
        print("Game result", "Well done " +  player_B  + " You Won!!" )
        file = open("Game_Results","a")
        file.write(f"\n\n {a} \n\n{player_A} vs {player_B}\nGame Result:\t\n Well Done {player_B} You Won")
        file.close()
        break



str = input("Enter yes or no if want to see Game Result Board: ")
if(str == "yes"):
    file = open("Game_Results","r")
    data = file.read()
    print(data)
    file.close()
elif(str == "no"):
    pass
    
   
    


    
        
        
        
    