from turtle import Screen
import car as c
import player as p
import scoreboard as sc
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title(titlestring="Turtle Cross 2k23")
screen.tracer(0)

player = p.Player()
car_manager = c.CarManager()
scoreboard = sc.Scoreboard()

screen.listen()
screen.onkey(fun=player.move_up, key="Up")
screen.onkey(fun=player.move_down, key="Down")

game_is_on = True
loop_counter = 0

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.add_car()

    # Put cars to run on the screen
    car_manager.move_car()

    for car in car_manager.all_cars:
        # Check if car got to the end of the screen
        if car.xcor() < -280:
            car.hideturtle()
            car_manager.all_cars.remove(car)

        # Check if player has hit a car
        y_distance = player.ycor() - car.ycor()
        x_distance = player.xcor() - car.xcor()
        if -25 < y_distance < 20 and -20 < player.distance(car) < 20:
            game_is_on = False

    # Check if player got to the end of the screen
    if player.is_at_finish_line():
        scoreboard.increase_level()
        car_manager.increase_level()
        player.restart()

scoreboard.game_over()
screen.exitonclick()
