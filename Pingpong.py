import turtle  # import daya from turtle library ,included in python.
# Screen
wind = turtle.Screen()                                      #To Create Screen Object
wind.title ("Ping Pong Game")                               #Title of Window
wind.bgcolor ("Black")                                      # Color of Window 
wind.setup(width =800 , height= 600)                        # Dimensions of window
wind.tracer(0)                                              # To stop auto Update of window

#Madrab 1
madrab1 = turtle.Turtle()                                  #intializr turtle object 
madrab1.speed (0)                                          # Control Speed
madrab1.shape("square")                                    # Control shape 
madrab1.shapesize(stretch_len=1 , stretch_wid=5)           # Control dimensions of shape
madrab1.color ("blue")                                     # Control color
madrab1.penup()                                            #Stop object drawing Lines
madrab1.goto(-350,0)                                       # detemine position of object

#Madrab2
madrab2 = turtle.Turtle()
madrab2.speed (0)  
madrab2.shape("square")
madrab2.shapesize(stretch_len=1 , stretch_wid=5)
madrab2.color ("red")
madrab2.penup()
madrab2.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed (0)  
ball.shape("circle")
ball.shapesize(stretch_len=1 , stretch_wid=1)           # Can be removed due to it is default (1,1)
ball.color ("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.4   # to make the ball moves by 0.4 frame 
ball.dy = 0.4

#Score 
Score1 = 0
Score2 = 0
Score = turtle.Turtle()
Score.speed (0)
Score.color ("white")
Score.penup()
Score.hideturtle()
Score.goto(0, 260)
Score.write("player1: 0  Player2: 0", align="center", font=("Courier",24,"normal"))

#Functions
def madrab1_up():                   
    y = madrab1.ycor()              #define y coordinator of madra
    y += 20                         # get a new y coordinatir to get up 
    madrab1.sety(y)                 # Sets new y to object
def madrab1_down(): 
    y = madrab1.ycor()
    y -= 20                         # get a new y coordinatir to get down
    madrab1.sety(y)
def madrab2_up(): 
    y = madrab2.ycor()
    y += 20
    madrab2.sety(y)
def madrab2_down(): 
    y = madrab2.ycor()
    y -= 20
    madrab2.sety(y)
#Keybord Contrloller
wind.listen()                            #tell window to expect a new input           
wind.onkeypress(madrab1_up,"w")          # set w to get madrab1 up
wind.onkeypress(madrab1_down,"s")        # Set s to get madrab1 down
wind.onkeypress(madrab2_up,"Up")         # Set Up arrow to get madrab2 Up 
wind.onkeypress(madrab2_down,"Down")     # Set Down arrow to get madrab2 down
# Main game Loop
while True:
    wind.update()                                          # To Update Screen in every time loop runs
    ball.setx(ball.xcor() + ball.dx)                       # Moving the ball in X-dirction
    ball.sety(ball.ycor() + ball.dy)                       # Moving the ball in Y-direction
    # Border Check 
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy*= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy*= -1
        

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        Score1 += 1
        Score.clear()
        Score.write("player1: {}  Player2: {}".format(Score1,Score2), align="center", font=("Courier",24,"normal"))
       
    if ball.xcor() < -390:
        ball.goto (0,0)
        ball.dx *= -1
        Score2 += 1
        Score.clear()
        Score.write("player1: {}  Player2: {}".format(Score1,Score2), align="center", font=("Courier",24,"normal"))
        
       
    if (ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < madrab2.ycor() + 40) and (ball.ycor() > madrab2.ycor() + -40) :
        ball.setx(340)
        ball.dx *= -1 
    if (ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < madrab1.ycor() + 40) and (ball.ycor() > madrab1.ycor() + -40) :
        ball.setx(-340)
        ball.dx *= - 1 
