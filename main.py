"""write by: M. Amin"""
import turtle
from math import tan, radians
# objects
pen = turtle.Pen()
screen = turtle.Screen()
# initialize settings
pen.speed(-1)
pen.width(3)
pen.ht()
pen.color("white", "white")
colors = ["red", "blue", "orange", "#E43AC2", "gold", "light green"]
# variables
rings_num = int(turtle.numinput("number of rings", "input an integer: "))
hexagon_len = int(turtle.numinput("hexagon side length", "input an integer: "))
# functions
def hexagon(side_length):
    """a function to draw a hexagon."""
    pen.begin_fill()
    for side in range(6):
        pen.fd(side_length)
        pen.left(60)
    pen.end_fill()
# execute part
hexagon(hexagon_len)
for ring in range(rings_num):
    # transform between rings
    pen.fillcolor(colors[ring % len(colors)])
    pen.up()
    pen.right(90)
    pen.fd(hexagon_len * tan(radians(60)))
    pen.left(90)
    pen.down()
    # draw a ring
    for i in range(6):
        # big hexagon side
        for side_hexagon in range(ring + 1):
            hexagon(hexagon_len)
            pen.up()
            pen.fd(hexagon_len)
            pen.left(60)
            pen.fd(hexagon_len)
            pen.right(60)
            pen.down()
        # big hexagon corner
        pen.up()
        pen.fd(hexagon_len)
        pen.left(60)
        pen.down()


screen.exitonclick()
