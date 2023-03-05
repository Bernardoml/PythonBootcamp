from player import Turtle
from random import randint, choice

CAR_COLORS = ["black", "red", "green", "blue", "yellow", "purple", "cyan", "orange", "pink"]
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.level = 1
        self.add_car()

    def add_car(self):
        if randint(1, 6) == 1:
            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_len=2)
            new_car.color(choice(CAR_COLORS))
            new_car.penup()
            new_car.y_start = randint(-250, 250)
            new_car.move_distance = randint(5, 8) + MOVE_INCREMENT * (self.level - 1)
            new_car.goto(300, new_car.y_start)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.goto(car.xcor() - car.move_distance, car.ycor())

    def increase_level(self):
        self.level += 1
