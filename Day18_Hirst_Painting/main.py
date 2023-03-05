import turtle as t
from random import randint, choice
# import colorgram
#
# colors = colorgram.extract('image.jpg', 15)
#
# colors_rgb = []
#
# for color in colors:
#     rgb = color.rgb
#     r = rgb.r
#     g = rgb.g
#     b = rgb.b
#     colors_rgb.append((r, g, b))
#
# print(colors_rgb)

# colors with background whites removed (first 3 of the list and one near the end)
colors = [(198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157),
           (215, 74, 12), (15, 154, 16), (199, 14, 10), (85, 81, 83), (243, 33, 165)]

timmy = t.Turtle()
timmy.penup()
timmy.speed('fastest')
timmy.hideturtle()
t.colormode(255)


def draw_hirsh(columns, rows, spacing):
    spacing = 50
    reset_x = -spacing * columns / 2
    reset_y = spacing * rows / 2
    timmy.goto(reset_x, reset_y)

    for _ in range(rows):
        for _ in range(columns):
            timmy.dot(20, choice(colors))
            timmy.forward(spacing)
        reset_y -= spacing
        timmy.goto(reset_x, reset_y)


draw_hirsh(10, 10, 50)

screen = t.Screen()
screen.exitonclick()
