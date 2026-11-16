"""
Automated script to capture high-quality render screenshots of the rotating cuboid
at multiple rotation angles for the lab report and documentation.
"""

import os
from PIL import Image
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Modified vertices for rectangular cuboid
vertices = (
    (2.0, -1.0, -1.5),
    (2.0, 1.0, -1.5),
    (-2.0, 1.0, -1.5),
    (-2.0, -1.0, -1.5),
    (2.0, -1.0, 1.5),
    (2.0, 1.0, 1.5),
    (-2.0, -1.0, 1.5),
    (-2.0, 1.0, 1.5),
)

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7),
)


def draw_cuboid():
    glLineWidth(3.0)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def capture_frame(filename, target_dirs, width=800, height=600):
    glPixelStorei(GL_PACK_ALIGNMENT, 1)
    data = glReadPixels(0, 0, width, height, GL_RGB, GL_UNSIGNED_BYTE)
    image = Image.frombytes("RGB", (width, height), data)
    image = image.transpose(Image.FLIP_TOP_BOTTOM)

    for d in target_dirs:
        os.makedirs(d, exist_ok=True)
        save_path = os.path.join(d, filename)
        image.save(save_path)
        print(f"Saved: {save_path}")


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    dirs = [
        os.path.join(base_dir, "screenshots"),
        os.path.join(base_dir, "submission_report", "screenshots"),
    ]

    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(0.0, 0.0, 0.0, 1.0)

    # Initial capture at 0 deg, 35 deg, 70 deg, 120 deg
    angles = [
        (0, "cuboid_angle_0.png"),
        (35, "cuboid_angle_35.png"),
        (70, "cuboid_angle_70.png"),
        (120, "cuboid_angle_120.png"),
    ]

    for angle, fname in angles:
        glLoadIdentity()
        gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
        glTranslatef(0.0, 0.0, -8.0)
        glRotatef(20, 1, 0, 0)
        glRotatef(angle, 0, 1, 0)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_cuboid()
        pygame.display.flip()

        capture_frame(fname, dirs)

    # Also save primary screenshot as cuboid_output.png
    glLoadIdentity()
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -8.0)
    glRotatef(20, 1, 0, 0)
    glRotatef(40, 0, 1, 0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_cuboid()
    pygame.display.flip()
    capture_frame("cuboid_output.png", dirs)

    pygame.quit()
    print("All screenshots generated successfully!")


if __name__ == "__main__":
    main()
