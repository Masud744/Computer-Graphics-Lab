"""
Automated script to run each task and save clean output images into screenshots/
"""
import os
import subprocess
import turtle

SCREENSHOTS_DIR = os.path.join(os.path.dirname(__file__), "screenshots")
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

def render_and_save(draw_func, filename, width=800, height=800):
    turtle.clearscreen()
    turtle.tracer(0, 0)
    turtle.setup(width, height)
    turtle.hideturtle()
    
    draw_func()
    
    turtle.update()
    eps_file = os.path.join(SCREENSHOTS_DIR, f"{filename}.eps")
    png_file = os.path.join(SCREENSHOTS_DIR, f"{filename}.png")
    
    cv = turtle.getscreen().getcanvas()
    cv.postscript(file=eps_file, colormode="color")
    
    # Convert EPS to PNG with Ghostscript
    cmd = [
        "gs", "-dSAFER", "-dBATCH", "-dNOPAUSE", "-dEPSCrop",
        "-sDEVICE=png16m", "-r150", f"-sOutputFile={png_file}", eps_file
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if os.path.exists(eps_file):
        os.remove(eps_file)
    print(f"Generated: {png_file}")

# Task 1 Drawing
def draw_task1():
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    
    # 1. Main circle
    t.pensize(3)
    t.pencolor("black")
    t.penup()
    t.goto(0, -300)
    t.pendown()
    t.circle(300)
    
    # 2. Smiling mouth
    t.penup()
    t.goto(0, -90)
    t.pendown()
    t.dot(180, "red")
    
    t.penup()
    t.goto(0, -65)
    t.pendown()
    t.dot(180, "white")
    
    # 3. Nose
    t.pensize(5)
    t.pencolor("blue")
    t.penup()
    t.goto(0, 30)
    t.pendown()
    t.goto(-35, -40)
    t.goto(35, -40)
    t.goto(0, 30)
    
    # 4. Eyes
    t.penup()
    t.goto(-90, 90)
    t.pendown()
    t.dot(40, "green")
    
    t.penup()
    t.goto(90, 90)
    t.pendown()
    t.dot(40, "green")

# Task 2 Drawing
def draw_task2():
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    
    length = 600
    height = 360
    
    t.penup()
    t.goto(-300, -180)
    t.pendown()
    t.color("green", "green")
    t.begin_fill()
    for _ in range(2):
        t.forward(length)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()
    
    circle_center_x = -300 + (length / 5)
    radius = 80
    
    t.penup()
    t.goto(circle_center_x, -radius)
    t.pendown()
    t.color("red", "red")
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Task 3 Drawing
def draw_task3():
    import math
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.pensize(2)
    
    size = 200
    
    t.penup()
    t.goto(-size / 2, -size / 2)
    t.pendown()
    for _ in range(4):
        t.forward(size)
        t.left(90)
        
    diagonal_offset = (size / 2) * math.sqrt(2)
    t.penup()
    t.goto(0, -diagonal_offset)
    t.setheading(45)
    t.pendown()
    for _ in range(4):
        t.forward(size)
        t.left(90)

# Task 4 Drawing
def draw_task4():
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.pensize(2)
    
    for _ in range(5):
        for _ in range(4):
            t.forward(150)
            t.right(90)
        t.right(72)

if __name__ == "__main__":
    render_and_save(draw_task1, "task1_output", 700, 700)
    render_and_save(draw_task2, "task2_output", 700, 500)
    render_and_save(draw_task3, "task3_output", 500, 500)
    render_and_save(draw_task4, "task4_output", 500, 500)
    turtle.bye()
    print("All task screenshots generated successfully!")
