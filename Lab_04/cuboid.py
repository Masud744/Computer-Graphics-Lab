"""
Lab 04: 3D Wireframe Rectangular Cuboid with OpenGL & Pygame
Course: IRE 404 - Computer Graphics and Animation Sessional
Student: Shahriar Alom Masud (ID: 2201032)

Requirements:
1. Create an OpenGL window with a resolution of 800 x 600 pixels using pygame.display.set_mode()
2. Set the background color to black using glClearColor()
3. Set the cuboid's edges to red using glColor3f()
4. Increase the thickness of the edges to 3 pixels using glLineWidth()
5. Modify the existing vertices coordinates so that the object has different width, height, and depth
6. Rotate the cuboid continuously around the Y-axis using glRotatef()
7. Run the program and verify that the red rectangular cuboid rotates smoothly against a black background
"""

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Requirement 5: Distinct Width, Height, and Depth
# Width  (X-axis) = 4.0  (from -2.0 to +2.0)
# Height (Y-axis) = 2.0  (from -1.0 to +1.0)
# Depth  (Z-axis) = 3.0  (from -1.5 to +1.5)
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

# 12 edges connecting the 8 vertices
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
    # Requirement 4: Set edge thickness to 3 pixels
    glLineWidth(3.0)

    # Requirement 3: Set edge color to Red
    glColor3f(1.0, 0.0, 0.0)

    # Render lines
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def main():
    # Initialize Pygame
    pygame.init()

    # Requirement 1: 800 x 600 OpenGL window
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Lab 04: Rotating Red Cuboid (OpenGL)")

    # Set up perspective projection
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    # Move back so the cuboid fits comfortably in the viewport
    glTranslatef(0.0, 0.0, -8.0)

    # Slight pitch around X-axis for better 3D depth perception
    glRotatef(20, 1, 0, 0)

    # Requirement 2: Black background color
    glClearColor(0.0, 0.0, 0.0, 1.0)

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # Requirement 6: Continuous rotation around Y-axis
        glRotatef(1.0, 0.0, 1.0, 0.0)

        # Clear color and depth buffers
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Draw wireframe cuboid
        draw_cuboid()

        # Update frame
        pygame.display.flip()

        # Requirement 7: Smooth 60 FPS animation
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
