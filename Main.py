def setup():
    global screen
    global plate
    global ball
    try:
        screen.clear() #Clear scrreen if it already exists
    except:
        None
    screen=t.Screen() #Set up the screen
    screen.title("Ping Pong")
    screen.bgcolor("black")
    screen.setup(width=800,height=600)
    screen.tracer(0)
    plate=t.Turtle() #Set up the plate
    plate.color("white")
    plate.shape("square")
    plate.shapesize(0.5,3)
    plate.penup()
    plate.goto(0,-275)
    ball=t.Turtle() #Set up the ball
    ball.color("red")
    ball.shape("circle")
    ball.shapesize(1,1)
    ball.penup()
    ball.goto(0,0)
    screen.update()
    main()

def main():
    global screen
    global plate
    global ball
    global pen
    global start
    pen=t.Turtle() #Set up the pen
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0,150)
    pen.pendown()
    style = ("Arial", 25, "bold")
    pen.write("Press Enter to start", font=style, align="center")
    pen.penup()
    start=False
    screen.update()
    screen.listen()
    screen.onkeypress(game_start,"Return")
    screen.mainloop() #Keep the window open

def game_start():
    global screen
    global game
    global pen
    global speed
    global ball
    global score
    score=0
    speed=10
    game=True
    pen.clear()
    ball.left(random.randint(30,60)) #Set a random angle for the ball
    ball.speed=0
    screen.onkeypress(None,"Return")
    screen.onkeypress(move_left,"a")
    screen.onkeypress(move_right,"d")
    screen.update()
    Game()

def Game():
    global ball
    global pen
    global game
    global speed
    global score
    if game:
        ball.forward(speed)
        if ball.xcor()>390 or ball.xcor()<-390: #If the ball hits the wall, it bounces
            ball.setheading(180-ball.heading())
            ball.forward(speed)
        elif ball.ycor()>300: #If the ball hits the ceiling, it bounces
            ball.setheading(-ball.heading())
            ball.forward(speed)
        elif ball.ycor()<-300: #If the ball hits the floor, the game is over
            end()
        elif ball.ycor()<-250 and ball.distance(plate)<50: #If the ball hits the plate, it bounces
            ball.setheading(-ball.heading())
            speed=speed*1.1 #Increase the speed of the ball
            score=score+1 #Increase the score
            pen.clear()
        screen.update()
        screen.ontimer(Game, 20)

def move_left(): #Move the plate to the left
    global plate
    global speed
    x=plate.xcor()
    x=x-speed*2
    if x<-350:
        x=-350
    plate.setx(x)
    screen.update()

def move_right(): #Move the plate to the right
    global plate
    global speed
    x=plate.xcor()
    x=x+speed*2
    if x>350:
        x=350
    plate.setx(x)
    screen.update()

def end(): #End the game
    global pen
    global ball
    global game
    global score
    game=False
    pen.clear()
    text="Score: "+str(score)
    style = ("Arial", 25, "bold")
    pen.write("Game Over", font=style, align="center")
    pen.goto(0,pen.ycor()-50)
    pen.write(text, font=style, align="center")
    pen.goto(0,pen.ycor()-50)
    pen.write("Press Enter to restart", font=style, align="center")
    #ball.goto(0,0)
    ball.degrees=0
    screen.update()
    screen.onkeypress(None,"a")
    screen.onkeypress(None,"d")
    screen.onkeypress(setup,"Return")
    screen.listen()

import turtle as t
import random
setup()
