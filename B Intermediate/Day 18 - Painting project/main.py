import colorgram
from turtle import Turtle, Screen
from random import choice

t = Turtle()
t.shape("classic")
t.speed("normal")
t.penup()
t.hideturtle()
t.setheading(225)
t.forward(300)
t.setheading(0)
s = Screen()
s.colormode(255)

# colors = colorgram.extract('damien_hirst.jpg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

color_list = [(236, 35, 108), (221, 231, 237), (145, 28, 66), (230, 237, 232),
              (239, 75, 35), (7, 148, 95), (220, 171, 45), (183, 158, 47), (45, 191, 232), (28, 127, 194),
              (254, 223, 0),
              (125, 192, 78), (85, 27, 91), (243, 218, 56), (178, 40, 98), (44, 170, 114), (211, 132, 166),
              (206, 57, 35),
              (239, 162, 193), (145, 27, 25), (243, 167, 156), (163, 211, 178), (26, 187, 225), (6, 116, 54),
              (138, 210, 232), (74, 135, 184), (170, 191, 221), (114, 10, 8)]

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    t.dot(20, choice(color_list))
    t.forward(50)

    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)

s.exitonclick()
