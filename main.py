# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 20)
# for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r, g, b)
#    rgb_colors.append(new_color)
# print(rgb_colors)
import random
import turtle

turtle.colormode(255)
color_list = [(236, 35, 108), (145, 28, 65), (239, 74, 34), (6, 148, 93), (231, 238, 234), (232, 168, 40),
              (184, 158, 46), (44, 191, 233), (27, 127, 195), (126, 193, 74), (253, 223, 0), (85, 28, 93),
              (172, 36, 98), (246, 219, 44), (42, 172, 112), (216, 130, 165), (216, 58, 26)]

tim = turtle.Turtle()
tim.hideturtle()
tim.penup()
tim.speed("fastest")
tim.setposition(-230, -250)
num_of_dots = 100

for dot_count in range(1, num_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


clear_screen = turtle.Screen()
clear_screen.exitonclick()
