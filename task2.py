from turtle import *

speed(3)

# Flag dimensions with 10:6 ratio
length = 600
height = 360

# 1. Green background rectangle
penup()
goto(-300, -180)
pendown()
color("green", "green")
begin_fill()
for i in range(2):
    forward(length)
    left(90)
    forward(height)
    left(90)
end_fill()

# 2. Red circle inside
# Circle centre is placed at 1/5 of the length from the left edge (-300 + 600/5 = -180)
circle_center_x = -300 + (length / 5)
radius = 80

penup()
goto(circle_center_x, -radius)
pendown()
color("red", "red")
begin_fill()
circle(radius)
end_fill()

hideturtle()
done()
