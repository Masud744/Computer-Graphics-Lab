from turtle import *

speed(3)

# 1. Main face outline (radius 300 circle)
pensize(3)
pencolor("black")
penup()
goto(0, -300)
pendown()
circle(300)

# 2. Smiling mouth
# Red blot first, then a white blot slightly above it to make a crescent
penup()
goto(0, -90)
pendown()
dot(180, "red")

penup()
goto(0, -65)
pendown()
dot(180, "white")

# 3. Nose (thick blue triangle)
# Drawn after mouth so the white blot doesn't cover it
pensize(5)
pencolor("blue")
penup()
goto(0, 30)
pendown()
goto(-35, -40)
goto(35, -40)
goto(0, 30)

# 4. Eyes (small green filled circles)
penup()
goto(-90, 90)
pendown()
dot(40, "green")

penup()
goto(90, 90)
pendown()
dot(40, "green")

hideturtle()
done()
