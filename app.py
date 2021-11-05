import turtle
import helpers as hlp
import time



# GAME VARIABLES
FPS = 1/240

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600



scr = hlp.init_screen(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

# ball

ball = hlp.create_ball()
ball.dx = 1
ball.dy = 1
ball.goto(0,-250)




# brick

bricks = []
BRICK_ROWS = 4
BRICK_COLS = SCREEN_WIDTH//100
top_left = (-SCREEN_WIDTH//2 + 50, SCREEN_HEIGHT//2 - 20)




brick_coordinates = []

for row in range(BRICK_ROWS):

	y_offset = row * 40

	for col in range(BRICK_COLS):

		x_offset = col * 100

		brick_coordinates.append((top_left[0] + x_offset, top_left[1] - y_offset))






for i in range(len(brick_coordinates)):
	bricks.append(hlp.create_brick())




for i, brick in enumerate(bricks):
	brick.goto(brick_coordinates[i])




# paddle 

paddle = hlp.create_paddle()
paddle.goto(0,-280)







def is_colliding_paddle():

	paddle_collision_conditons = [
		ball.ycor() < paddle.ycor() + 20,
		ball.xcor() < paddle.xcor() + 50,
		ball.xcor() > paddle.xcor() - 50
	]

	if all(paddle_collision_conditons):
		return True

	return False




# Checking top and bottom collison of ball and top and bottom edge
def is_top_or_bottom_collision():

	top_bottom_conditions = [
		ball.ycor() > SCREEN_HEIGHT//2 -10,
		
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



def paddle_right():

	paddle.setx(paddle.xcor() + 20)



def paddle_left():

	paddle.setx(paddle.xcor() - 20)



scr.listen()
scr.onkeypress(paddle_right,'d')
scr.onkeypress(paddle_left, 'a')




while True:

	# Move the ball

	
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	

	# check borders 

	if ball.ycor() < -SCREEN_HEIGHT//2 - 20:
		ball.dy *= -1
		ball.goto(0,-250)


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



	if is_colliding_paddle():
		ball.dy *= -1



	scr.update()
	time.sleep(FPS)
