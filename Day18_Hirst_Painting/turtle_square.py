import turtle as t
from random import randint, choice

timmy = t.Turtle()
# timmy.shape("turtle")
t.colormode(255)


def random_color():
    return randint(0, 255), randint(0, 255), randint(0, 255)


# TODO: draw a square with sides of 100px
# def draw_square():
#     for _ in range(4):
#         timmy.forward(100)
#         timmy.left(90)
#
#
# draw_square()


# Draw a dash line n number of times
# def draw_dash_line(dashes=10):
#     for _ in range(dashes):
#         timmy.forward(10)
#         timmy.penup()
#         timmy.forward(10)
#         timmy.pendown()
#
#
# draw_dash_line(15)


# Draw various polygons from 3 to 10 sides, changing color between each
# def draw_shape(num_sides):
#     exterior_angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(exterior_angle)
#
#
# def draw_polygons():
#     for n in range(3, 11):
#         draw_shape(n)
#         timmy.color(random_color())
#
# draw_polygons()


# Draw a random walk changing color between each step
# def draw_random_walk(steps=100):
#     direction = [0.0, 90.0, 180.0, 270.0]
#     timmy.speed('fast')
#     timmy.pensize(10)
#     for _ in range(steps):
#         heading = choice(direction)
#         timmy.setheading(heading)
#         timmy.forward(30)
#         timmy.color(random_color())
#
#
# draw_random_walk()


# Draw a spirograph using circles of 100px radius
def draw_spirograph(turns=60):
    for _ in range(turns):
        timmy.speed('fastest')
        timmy.circle(100)
        timmy.left(360 / turns)
        timmy.color(random_color())


draw_spirograph(90)

screen = t.Screen()
screen.exitonclick()
