"""write by: M. Amin"""
import turtle
# objects
pen = turtle.Pen()
screen = turtle.Screen()
# initialize settings
pen.speed(-1)
pen.width(3)
pen.ht()
# variables
rings_num = int(turtle.numinput("number of rings", "input an integer: "))
hexagon_len = int(turtle.numinput("hexagon side length", "input an integer: "))
# functions
def hexagon(side_length):
    """a function to draw a hexagon."""
    for side in range(6):
        pen.fd(side_length)
        pen.left(60)
# execute part
hexagon(hexagon_len)
for ring in range(rings_num):
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
        hexagon(hexagon_len)
        pen.up()
        pen.left(60)
        pen.bk(hexagon_len)


screen.exitonclick()
