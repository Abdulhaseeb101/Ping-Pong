#											pInG PoNg 
# Started on 9|4|20

import turtle

# Game Window Properties
gameWindow = turtle.Screen()
gameWindow.title("`*pInG PoNg*")
gameWindow.bgcolor("blue")
gameWindow.setup(width = 800, height = 600)
gameWindow.tracer(0)

# Paddle A
paddleA = turtle.Turtle()
paddleA.speed("slowest")
paddleA.shape("square")
paddleA.color("brown")
paddleA.shapesize(stretch_wid = 5, stretch_len = 1)
paddleA.penup()
paddleA.goto(-350, 0)



# Paddle B
paddleB = turtle.Turtle()
paddleB.speed("slowest")
paddleB.shape("square")
paddleB.color("brown")
paddleB.shapesize(stretch_wid = 5, stretch_len = 1)
paddleB.penup()
paddleB.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed("slowest")
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.mvX = 0.3
ball.mvY = 0.3

# Paddle A Functions
def paddleAUp():
	ycor = paddleA.ycor()
	ycor += 20
	paddleA.sety(ycor)

def paddleADown():
	ycor = paddleA.ycor()
	ycor -= 20
	paddleA.sety(ycor)

# Paddle B Functions
def paddleBUp():
	ycor = paddleB.ycor()
	ycor += 20
	paddleB.sety(ycor)

def paddleBDown():
	ycor = paddleB.ycor()
	ycor -= 20
	paddleB.sety(ycor)

# Keyboard Binding
gameWindow.listen()
gameWindow.onkeypress(paddleAUp, "w")
gameWindow.onkeypress(paddleADown, "s")
gameWindow.onkeypress(paddleBUp, "Up")
gameWindow.onkeypress(paddleBDown, "Down")

# Game loop
gameOver = False
while not gameOver:
	gameWindow.update()

	# Mving the ball
	ball.setx(ball.xcor() + ball.mvX)
	ball.sety(ball.ycor() + ball.mvY)
 
 	# Borders
	if ball.ycor() > 290:
		ball.sety(290)
		ball.mvY *= -1

	if ball.ycor() < -290:
		ball.sety(-290)
		ball.mvY *= -1

	if ball.xcor() > 390:
		ball.goto(0, 0)
		ball.mvX *= -1

	if ball.xcor() < -390:
		ball.goto(0, 0)
		ball.mvX *= -1

	# Collisions
	if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddleB.ycor() + 50 and ball.ycor() > paddleB.ycor() - 50):
		ball.setx(340)
		ball.mvX *= -1
		
	if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddleA.ycor() + 50 and ball.ycor() > paddleA.ycor() - 50):
		ball.setx(-340)
		ball.mvX *= -1	

print("GAME OVER")