import turtle
import helpers as hlp
import time



# GAME VARIABLES
FPS = 1/120

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600



scr = hlp.init_screen(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

# ball

ball = hlp.create_ball()
ball.dx = 2
ball.dy = 2
ball.goto(0,-250)




# brick

bricks = []

brick_coordinates = [
	(-300,150),(-150, 150), (0,150), (150,150), (300,150),
	(-300,75), (-150,75), (0,75), (150,75), (300,75),
	(-300,0), (-150,0), (0,0), (150,0), (300,0)

]

for i in range(len(brick_coordinates)):
	bricks.append(hlp.create_brick())




for i, brick in enumerate(bricks):
	brick.goto(brick_coordinates[i])









# Checking top and bottom collison of ball and top and bottom edge
def is_top_or_bottom_collision():

	top_bottom_conditions = [
		ball.ycor() > SCREEN_HEIGHT//2 -10,
		ball.ycor() < -SCREEN_HEIGHT//2 + 10
	]

	if any(top_bottom_conditions):
		return True

	return False



# checking left and right collision for ball and right and left edge
def is_right_or_left_collision():

	right_left_conditions = [
		ball.xcor() > SCREEN_WIDTH//2 - 10,
		ball.xcor() < -SCREEN_WIDTH//2 + 10
	]

	if any(right_left_conditions):
		return True


	return False




while True:

	# Move the ball

	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)



	# check borders 

	if is_top_or_bottom_collision():
		ball.dy *= -1


	if is_right_or_left_collision():
		ball.dx *= -1



	# check brick and ball collisions


	for brick in bricks:

		within_x = ball.xcor() < brick.xcor() + 50 and ball.xcor() > brick.xcor() - 50
		within_y = ball.ycor() < brick.ycor() + 30 and ball.ycor() > brick.ycor() - 30


		if within_x and within_y:
			if ball.xcor() > brick.xcor() + 40 or ball.xcor() < brick.xcor() - 40:
				ball.dx *= -1

			elif ball.ycor() > brick.ycor() + 20 or ball.ycor() < brick.ycor() - 20:
				ball.dy *= -1

			bricks.remove(brick)
			brick.hideturtle()





	scr.update()
	time.sleep(FPS)