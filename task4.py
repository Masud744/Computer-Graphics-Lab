from turtle import *

speed(3)
pensize(2)

# Drawing 5 squares rotated around a single corner
# Total angle 360 / 5 = 72 degrees
for i in range(5):
    # Draw one square
    for j in range(4):
        forward(150)
        right(90)
    # Rotate 72 degrees for the next square
    right(72)

hideturtle()
done()
