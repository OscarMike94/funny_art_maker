import random
import colorgram
import turtle as t
import math
from turtle import Screen

t.colormode(255)
t.hideturtle()
t.speed("fastest")
t.penup()

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)


class Art:

    def random_color(self):

        """Takes a random color from image and returning rgb value as tuple"""
        color_format = random.choice(rgb_colors)
        new_color = (color_format[0], color_format[1], color_format[2])
        return new_color

    def draw_art(self, dot_size, total_dot):
        """Takes dot size and total dot number input and draws expensive art with turtle"""
        x = -dot_size * 4
        y = x
        dot_number = round(math.sqrt(total_dot))
        for _ in range(dot_number):
            t.setposition(x, y)
            y += dot_size
            for _ in range(dot_number):
                t.dot(dot_size / 2, self.random_color())
                t.forward(dot_size)
        Screen().exitonclick()


art1 = Art()
art1.draw_art(50, 100)
