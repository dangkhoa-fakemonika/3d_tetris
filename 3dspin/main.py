import pygame
from enum import Enum


class COLORS(Enum):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)


class Cube:
    def __init__(self, pos):
        self.cube_pos = pos
        self.cube_dimension = [
            [pos[0], pos[1]],
            [pos[0] + 200, pos[1]],
            [pos[0] + 200, pos[1] + 200],
            [pos[0], pos[1] + 200],
            [pos[0] - 50, pos[1] + 150],
            [pos[0] - 50, pos[1] - 50],
            [pos[0] + 150, pos[1] - 50],
        ]

    def get_dimension(self, face):
        if face == 0:
            return [
                self.cube_dimension[0],
                self.cube_dimension[1],
                self.cube_dimension[2],
                self.cube_dimension[3]
            ]
        elif face == 1:
            return [
                self.cube_dimension[0],
                self.cube_dimension[3],
                self.cube_dimension[4],
                self.cube_dimension[5]
            ]
        elif face == 2:
            return [
                self.cube_dimension[0],
                self.cube_dimension[5],
                self.cube_dimension[6],
                self.cube_dimension[1]
            ]

    def print_cube(self, surface):
        for face in range(3):
            pygame.draw.aalines(surface, COLORS['WHITE'].value, True, self.get_dimension(face))

    def spin_x(self):
        pass


WIDTH = 600
HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

new_cube = Cube((200, 200))

run = True
pressed = False
while run:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run = False
            break

    new_cube.print_cube(screen)

    pygame.display.flip()
pygame.quit()
