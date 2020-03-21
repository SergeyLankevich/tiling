from local import *
import turtle as t
import math
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


first_color = 'Yellow' # get_color_choice().capitalize()
second_color = 'Black' # get_color_choice().capitalize()
number_of_hexagons = 20 # get_num_hexagons()
side_length =  500 / (1.5 * number_of_hexagons)


def draw_hex():
    for i in range(6):
        t.forward(side_length)
        t.right(60)


def draw_line_even(hex_num: int, flag: bool):
    '''

    :param hex_num: amount of hexagons
    :param flag: color inversion condition
    '''
    for hexagon in range(hex_num):
        t.pendown()
        t.left(90)
        if flag:
            if hexagon % 2 == 0:
                t.color('black', first_color)
            elif hexagon % 2 == 1:
                t.color('black', second_color)
        else:
            if hexagon % 2 == 0:
                t.color('black', second_color)
            elif hexagon % 2 == 1:
                t.color('black', first_color)
        t.begin_fill()
        draw_hex()
        t.end_fill()
        t.right(90)
        t.penup()
        t.forward(math.sqrt(3) * side_length)
    t.backward(math.sqrt(3) * side_length * hex_num + math.sqrt(3) * side_length / 2)
    t.right(90)
    t.fd(side_length * 1.5)
    t.lt(90)


def draw_line_odd(hex_num: int, flag: bool):
    '''

    :param hex_num: amount of hexagons
    :param flag: color inversion condition
    '''
    for hexagon in range(hex_num):
        t.pendown()
        t.left(90)
        if flag:
            if hexagon % 2 == 0:
                t.color('black', first_color)
            elif hexagon % 2 == 1:
                t.color('black', second_color)
        else:
            if hexagon % 2 == 0:
                t.color('black', second_color)
            elif hexagon % 2 == 1:
                t.color('black', first_color)
        t.begin_fill()
        draw_hex()
        t.end_fill()
        t.right(90)
        t.penup()
        t.forward(math.sqrt(3) * side_length)
    t.backward(math.sqrt(3) * side_length * (hex_num - 1) + math.sqrt(3) * side_length / 2)
    t.right(90)
    t.fd(side_length * 1.5)
    t.lt(90)


def set_start_position(hex_num: int, side: int):
    '''

    :param hex_num: amount of hexagons
    :param side: side length of hexagon
    '''
    t.penup()
    high = 2 * side * math.ceil(hex_num / 2) + side * math.floor(hex_num / 2) + 0.5 * side * (1 - hex_num % 2)
    print(math.floor(hex_num / 2))
    print(math.ceil(hex_num / 2))
    width = math.sqrt(3) * side * hex_num + math.sqrt(3) * side / 2
    x0 = -width / 2
    y0 = high / 2

    x = x0 + math.sqrt(3) * side / 2
    y = y0 - 1.5 * side
    t.setposition(x, y)



t.speed(0)
set_start_position(number_of_hexagons, side_length)
for i in range(number_of_hexagons // 4):
    draw_line_even(number_of_hexagons, False)
    draw_line_odd(number_of_hexagons, False)
    draw_line_even(number_of_hexagons, True)
    draw_line_odd(number_of_hexagons, True)
if number_of_hexagons % 4 == 3:
    draw_line_even(number_of_hexagons, False)
    draw_line_odd(number_of_hexagons, False)
    draw_line_even(number_of_hexagons, True)
elif number_of_hexagons % 4 == 2:
    draw_line_even(number_of_hexagons, False)
    draw_line_odd(number_of_hexagons, False)
elif number_of_hexagons % 4 == 1:
    draw_line_even(number_of_hexagons, False)

t.exitonclick()