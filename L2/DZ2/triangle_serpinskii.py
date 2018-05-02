from turtle import (
    speed, color, begin_fill, penup, goto, pendown, fd,
    left, pos, end_fill, right, tracer,
)


def new_coordinate(x, y, base, level):
    """calculate coordinates"""
    if level <= 0:
        return

    for i in range(1, level):
        new_base = base / (2 ** i)
        new_x = x
        new_level = level - i

        if new_level <= 0:
            break

        for j in range(round(base) // round(new_base) - 1):
            new_x += new_base

            if j % 2 != 0:
                break

            next_triangle(new_x, y, new_base, new_level)


def first_triangle(x, y, base, level):
    """Make first triangle"""
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
    """Make all triangle but first"""
    color("white", "white")
    begin_fill()
    penup()
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


def make_triangle_serpinskii():
    """Main fun"""
    base = input("please enter base: ")

    if base == "":
        base = 400
    else:
        base = int(base)

    level = input("please enter level: ")

    if level == "":
        level = 5
    else:
        level = int(level)

    speed(0)
    tracer(0)
    first_triangle(0, -base / 2, base, level)


if __name__ == "__main__":
    make_triangle_serpinskii()
    input()
