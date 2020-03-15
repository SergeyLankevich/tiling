from local import *
from turtle import *
from math import *
colors = ['Green', 'Blue', 'Yellow', 'Black', 'Red', 'Maroon']


def get_color_choice():
    color = input(COLOR_CHOICE)
    while color.capitalize() not in colors:
        color = input(COLOR_EXCEPTION)
    print(COLOR_ACCEPTANCE)
    return color


def get_num_hexagons():
    hexagons_num = int(input(HEXAGONS_NUMBER))
    while not 4 <= hexagons_num <= 20:
        hexagons_num = int(input(HEXAGONS_EXCEPTION))
    return hexagons_num


first_color = get_color_choice().capitalize()
second_color = get_color_choice().capitalize()
number_of_hexagons = get_num_hexagons()
side_length = 500 / (1.5 * number_of_hexagons)

def draw_hex(hex_num):
    for i in range(6):
        forward(side_length)
        right(60)


def draw_line(hex_num):
    for hexagon in range(hex_num):
        pendown()
        left(90)
        if hexagon % 2 == 0:
            color('black', second_color)
        elif hexagon % 2 == 1:
            color('black', first_color)
        begin_fill()
        draw_hex(hex_num)
        end_fill()
        right(90)
        penup()
        forward(sin(radians(60)) * 2 * side_length)
    backward(2 * side_length * (hex_num - 1))
