from random import choice
from turtle import *
from freegames import vector, floor

tiles = []
for count in range(20*20):
    tiles.append(1)
path = Turtle(visible=False)

def fill():
    for count in range(20*20):
        tiles.append(1)

def pyramid():
    tiles.clear()
    for index in range(400):
        x, y = getCornetoIndex(index)
        if x+y>=20 and y>=x:
            tiles.append(1)
        else:
            tiles.append(0)

def chessboard():
    tiles.clear()
    for count in range(20*20):
        if (count % 2 == 0 and floor(count/20, 1) % 2 != 0) or (count % 2 != 0 and floor(count/20, 1) % 2 == 0):
            tiles.append(1)
        else:
            tiles.append(0)

def getCornetoIndex(index):
    x = index%20
    y = floor(index, 20)/20
    return x, y

def leftCorneto():
    tiles.clear()
    for index in range(20 * 20):
        x, y = getCornetoIndex(index)
        print(x)
        print(y)
        if x + y <= 20:
            tiles.append(1)
        else:
            tiles.append(0)
def square(x, y):
    path.up()
    path.goto(x - 210, -y + 190)
    path.down()
    path.begin_fill()
    for count in range(4):
        path.forward(20)
        path.left(90)
    path.end_fill()


def draw():
    for index in range(len(tiles)):
        if tiles[index] == 1:
            square(20 * (index % 20), int(floor(index, 20)))


setup(420, 420, 370, 100)
hideturtle()
tracer(False)
chessboard()
leftCorneto()
pyramid()
square(0, 0)
draw()
done()
