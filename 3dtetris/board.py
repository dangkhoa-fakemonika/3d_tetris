import pygame.draw

from all_assets import *
import blocks


def draw_border(surface):
    pygame.draw.aalines(surface, (255, 255, 255), False, [
        (100, 200),
        (100, 520),
        (230, 595),
        (360, 520),
        (360, 200),
        (230, 125),
        (100, 200),
        (230, 125),
        (230, 445),
        (100, 520),
        (230, 445),
        (360, 520)
    ])


class Board:
    def __init__(self):
        self.board_size = [[[0 for x in range(10)] for y in range(24)] for z in range(10)]

    def insert_block(self, cord, color):
        self.board_size[cord[0]][cord[1]][cord[2]] = color

    def insert_blocks(self, cords):
        for coord in cords:
            self.insert_block(coord[0], coord[1])

    def insert_piece(self, shape, center, color):
        for block in shape.value:
            self.insert_block((block[0] + center[0], block[1] + center[1], block[2] + center[2]), color)

    def clear_board(self):
        for z in range(10):
            for y in range(24):
                for x in range(10):
                    self.board_size[x][y][z] = 0

    def print_board_data(self, screen, view=0):
        if view == 0:
            for z in range(10):
                for y in range(23, -1, -1):
                    for x in range(10):
                        if self.board_size[x][y][z] != 0:
                            blocks.print_cube((x, y, z), screen, COLOR_ARRAY[abs(self.board_size[x][y][z]) - 1])
        elif view == 1:
            for z in range(10):
                for y in range(23, -1, -1):
                    for x in range(9, -1, -1):
                        if self.board_size[x][y][z] != 0:
                            blocks.print_cube((z, y, (9 - x)), screen, COLOR_ARRAY[abs(self.board_size[x][y][z]) - 1])

        elif view == 2:
            for z in range(9, -1, -1):
                for y in range(23, -1, -1):
                    for x in range(9, -1, -1):
                        if self.board_size[x][y][z] != 0:
                            blocks.print_cube(((9 - x), y, (9 - z)), screen, COLOR_ARRAY[abs(self.board_size[x][y][z]) - 1])

        elif view == 3:
            for z in range(9, -1, -1):
                for y in range(23, -1, -1):
                    for x in range(10):
                        if self.board_size[x][y][z] != 0:
                            blocks.print_cube(((9 - z), y, x), screen, COLOR_ARRAY[abs(self.board_size[x][y][z]) - 1])

    def print_x_view(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (400, 200, 200, 400), width=1)
        for z in range(10):
            for y in range(23, -1, -1):
                for x in range(10):
                    if self.board_size[x][y][z] != 0:
                        pygame.draw.rect(screen, COLOR_ARRAY[abs(self.board_size[x][y][z]) - 1],
                                         (400 + x * 20, 120 + y * 20, 20, 20))
                        pygame.draw.rect(screen, (255, 255, 255),
                                         (400 + x * 20, 120 + y * 20, 20, 20), width=1)

    def print_y_view(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (600, 200, 200, 200), width=1)
        for z in range(10):
            for y in range(24):
                for x in range(10):
                    if self.board_size[x][y][z] != 0:
                        pygame.draw.rect(screen, COLOR_ARRAY[abs(self.board_size[x][y][z]) - 1],
                                         (600 + x * 20, 200 + z * 20, 20, 20))
                        pygame.draw.rect(screen, (255, 255, 255),
                                         (600 + x * 20, 200 + z * 20, 20, 20), width=1)

    def print_z_view(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (800, 200, 200, 400), width=1)
        for z in range(10):
            for y in range(23, -1, -1):
                for x in range(10):
                    if self.board_size[x][y][z] != 0:
                        pygame.draw.rect(screen, COLOR_ARRAY[abs(self.board_size[x][y][z]) - 1],
                                         (800 + (9 - z) * 20, 120 + y * 20, 20, 20))
                        pygame.draw.rect(screen, (255, 255, 255),
                                         (800 + (9 - z) * 20, 120 + y * 20, 20, 20), width=1)

    def update_board(self):
        for y in range(23, -1, -1):
            for z in range(10):
                for x in range(10):
                    if self.board_size[x][y][z] <= 0:
                        continue

                    if y == 23 or self.board_size[x][y + 1][z] != 0:
                        self.board_size[x][y][z] *= -1

                    else:
                        self.board_size[x][y + 1][z] = self.board_size[x][y][z]
                        self.board_size[x][y][z] = 0
