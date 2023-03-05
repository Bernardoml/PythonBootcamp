import turtle as t
import paddle as p
import ball as b
import net as n
import scoreboard as sc
import time

screen = t.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title(titlestring="Pong Game 2k23")
screen.tracer(0)

l_paddle = p.Paddle(p.L_STARTING_POSITION)
r_paddle = p.Paddle(p.R_STARTING_POSITION)
net = n.Net()
ball = b.Ball()
scoreboard = sc.Scoreboard()

screen.listen()
screen.onkey(fun=r_paddle.move_up, key="Up")
screen.onkey(fun=r_paddle.move_down, key="Down")
screen.onkey(fun=l_paddle.move_up, key="w")
screen.onkey(fun=l_paddle.move_down, key="s")


game_is_on = True
point_is_on = False
ball.move_ball()

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()

    ball.move_ball()

    # Check if bounce on the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    # Check if bounce on the paddle
    if ball.xcor() < -320 and ball.distance(l_paddle) < 50 or ball.xcor() > 320 and ball.distance(r_paddle) < 50:
        ball.bounce_paddle()

    # Check if L paddle misses the ball
    if ball.xcor() < -380:
        scoreboard.r_point()
        l_paddle.restart()
        r_paddle.restart()
        ball.restart()

    # Check if RL paddle misses the ball
    elif ball.xcor() > 380:
        scoreboard.l_point()
        l_paddle.restart()
        r_paddle.restart()
        ball.restart()

    if scoreboard.l_score == 5 or scoreboard.r_score == 5:
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
