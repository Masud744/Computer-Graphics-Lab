import math
from turtle import *

speed(3)
pensize(2)

size = 200

# 1. First square (straight/upright)
penup()
goto(-size / 2, -size / 2)
pendown()
for i in range(4):
    forward(size)
    left(90)

# 2. Second square (rotated by 45 degrees - diamond shape)
# Distance from center (0,0) to corner vertex along axes = (size / 2) * sqrt(2)
diagonal_offset = (size / 2) * math.sqrt(2)

penup()
goto(0, -diagonal_offset)
setheading(45)
pendown()
for i in range(4):
    forward(size)
    left(90)

hideturtle()
done()
