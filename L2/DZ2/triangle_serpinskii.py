from turtle import *
import time
import random


coordinate_list = []
speed(10)


def new_coordinate(x, y, base, level):
    if level > 1:
        for i in range(1, level):
            new_base = base / (2 ** i)
            new_x = x
            new_level = level - i
            if new_level > 0:
                for j in range(round(base) // round(new_base) - 1):
                    new_x += new_base
                    if j % 2 == 0:
                        coordinate_list.append((
                            new_x,
                            y,
                            new_base,
                            new_level))


def first_triangle(x, y, base, level):
    color("black", "black")
    begin_fill()
    penup()
    goto(x, y)
    pendown()
    fd(base / 2)
    left(120)
    fd(base)
    left(120)
    fd(base)
    left(120)
    x2, y2 = pos()
    fd(base / 2)
    end_fill()
    new_coordinate(x2, y2, base, level)


def next_triangle(x, y, base, level):
    color("white", "white")
    begin_fill()
    penup()
    # print("y = ", round(y))
    goto(x, y)
    pendown()
    left(60)
    fd(base)
    left(120)
    fd(base)
    x2, y2 = pos()
    left(120)
    fd(base)
    left(120)
    right(60)
    end_fill()
    new_coordinate(x2, y2, base, level)


def triangle_serpinskii(base, level):
    first_triangle(0, -base / 2, base, level)
    while coordinate_list:
        new_p = coordinate_list.pop(0)
        next_triangle(*new_p)


triangle_serpinskii(400, 7)
time.sleep(2)
# input()
