import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Vertices for the rectangular cuboid
# Using different values so width, height, and depth are all different
# Width = 4.0, Height = 2.0, Depth = 3.0
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
    # Set line thickness to 3 pixels and color to red
    glLineWidth(3.0)
    glColor3f(1.0, 0.0, 0.0)

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def main():
    pygame.init()

    # Create 800x600 window with OpenGL
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Rotating Cuboid")

    # Set up perspective view
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    # Move back so the cuboid is clearly visible
    glTranslatef(0.0, 0.0, -8.0)

    # Slight tilt to see the 3D shape better
    glRotatef(20, 1, 0, 0)

    # Set background color to black
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

        # Rotate around Y-axis
        glRotatef(1.0, 0.0, 1.0, 0.0)

        # Clear screen and draw
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_cuboid()
        pygame.display.flip()

        # Limit frame rate to 60 FPS
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
