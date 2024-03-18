import pygame.draw

from all_assets import *
import blocks
import all_rotations


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
    # New board
    def __init__(self):
        self.board_size = [[[0 for x in range(10)] for y in range(24)] for z in range(10)]
        self.is_falling_piece = False
        self.current_piece = [[0, 0, 0], [0, 0, 0]]
        self.piece_type = "I_PIECE"
        self.piece_color = 0

    # Insert singular block
    def insert_block(self, cord, color):
        self.board_size[cord[0]][cord[1]][cord[2]] = color

    # Insert multiple blocks
    def insert_blocks(self, cords):
        for coord in cords:
            self.insert_block(coord[0], coord[1])

    # Insert
    def insert_piece(self, shape, center, color):
        # print("inserted")
        if not self.is_falling_piece:
            for block in shape.value:
                self.insert_block((block[0] + center[0], block[1] + center[1], block[2] + center[2]), color)
            self.is_falling_piece = True
            self.current_piece[0][0] = center[0] - 1
            self.current_piece[0][1] = center[1]
            self.current_piece[0][2] = center[2] - 1
            self.current_piece[1][0] = center[0] + 2
            self.current_piece[1][1] = center[1] + 3
            self.current_piece[1][2] = center[2] + 2
            self.piece_color = color

    def spin_piece(self, dirt_x, dirt_y, dirt_z):
        rot = [[[0 for z in range(4)] for y in range(4)] for x in range(4)]
        if dirt_x == 1:
            for x in range(4):
                for y in range(4):
                    for z in range(4):
                        try:
                            if (
                                0 <= x + self.current_piece[0][0] <= 9 and
                                y + self.current_piece[0][1] <= 23 and
                                0 <= z + self.current_piece[0][2] <= 23 and
                                self.board_size[x + self.current_piece[0][0]][y + self.current_piece[0][1]][z + self.current_piece[0][2]] > 0
                            ):
                                rot[x][3 - z][y] = \
                                    self.board_size[x + self.current_piece[0][0]][y + self.current_piece[0][1]][z + self.current_piece[0][2]]
                        except IndexError:
                            del rot
                            return

            for x in range(4):
                for y in range(4):
                    for z in range(4):
                        try:
                            if (self.board_size[x + self.current_piece[0][0]][y + self.current_piece[0][1]][z + self.current_piece[0][2]] < 0 <
                                    rot[x][y][z]):
                                del rot
                                return
                        except IndexError:
                            del rot
                            return

            for x in range(4):
                for y in range(4):
                    for z in range(4):
                        if self.board_size[x + self.current_piece[0][0]][y + self.current_piece[0][1]][
                                z + self.current_piece[0][2]] > 0:
                            self.board_size[x + self.current_piece[0][0]][y + self.current_piece[0][1]][
                                z + self.current_piece[0][2]] = 0
                        if rot[x][y][z] > 0:
                            self.board_size[x + self.current_piece[0][0]][y + self.current_piece[0][1]][
                                z + self.current_piece[0][2]] = rot[x][y][z]

        if dirt_x == -1:
            for x in range(4):
                for y in range(4):
                    for z in range(4):
                        try:
                            if (
                                0 <= x + self.current_piece[0][0] <= 9 and
                                y + self.current_piece[0][1] <= 23 and
                                0 <= z + self.current_piece[0][2] <= 23 and
                                self.board_size[x + self.current_piece[0][0]][y + self.current_piece[0][1]][z + self.current_piece[0][2]] > 0
                            ):
                                rot[x][z][3 - y] = \
                                    self.board_size[x + self.current_piece[0][0]][y + self.current_piece[0][1]][z + self.current_piece[0][2]]
                        except IndexError:
                            del rot
                            return

            for x in range(4):
                for y in range(4):
                    for z in range(4):
                        try:
                            if (self.board_size[x + self.current_piece[0][0]][y + self.current_piece[0][1]][z + self.current_piece[0][2]] < 0 <
                                    rot[x][y][z]):
                                del rot
                                return
                        except IndexError:
                            del rot
                            return

            for x in range(4):
                for y in range(4):
                    for z in range(4):
                        if self.board_size[x + self.current_piece[0][0]][y + self.current_piece[0][1]][
                                z + self.current_piece[0][2]] > 0:
                            self.board_size[x + self.current_piece[0][0]][y + self.current_piece[0][1]][
                                z + self.current_piece[0][2]] = 0
                        if rot[x][y][z] > 0:
                            self.board_size[x + self.current_piece[0][0]][y + self.current_piece[0][1]][
                                z + self.current_piece[0][2]] = rot[x][y][z]
        if dirt_y == 1:
            for x in range(4):
                for y in range(4):
                    for z in range(4):
                        try:
                            if (
                                0 <= x + self.current_piece[0][0] <= 9 and
                                y + self.current_piece[0][1] <= 23 and
                                0 <= z + self.current_piece[0][2] <= 23 and
                                self.board_size[x + self.current_piece[0][0]][y + self.current_piece[0][1]][z + self.current_piece[0][2]] > 0
                            ):
                                rot[z][y][3 - x] = \
                                    self.board_size[x + self.current_piece[0][0]][y + self.current_piece[0][1]][z + self.current_piece[0][2]]
                        except IndexError:
                            del rot
                            return

            for x in range(4):
                for y in range(4):
                    for z in range(4):
                        try:
                            if (self.board_size[x + self.current_piece[0][0]][y + self.current_piece[0][1]][z + self.current_piece[0][2]] < 0 <
                                    rot[x][y][z]):
                                del rot
                                return
                        except IndexError:
                            del rot
                            return

            for x in range(4):
                for y in range(4):
                    for z in range(4):
                        if self.board_size[x + self.current_piece[0][0]][y + self.current_piece[0][1]][
                                z + self.current_piece[0][2]] > 0:
                            self.board_size[x + self.current_piece[0][0]][y + self.current_piece[0][1]][
                                z + self.current_piece[0][2]] = 0
                        if rot[x][y][z] > 0:
                            self.board_size[x + self.current_piece[0][0]][y + self.current_piece[0][1]][
                                z + self.current_piece[0][2]] = rot[x][y][z]

        if dirt_y == -1:
            for x in range(4):
                for y in range(4):
                    for z in range(4):
                        try:
                            if (
                                0 <= x + self.current_piece[0][0] <= 9 and
                                y + self.current_piece[0][1] <= 23 and
                                0 <= z + self.current_piece[0][2] <= 23 and
                                self.board_size[x + self.current_piece[0][0]][y + self.current_piece[0][1]][z + self.current_piece[0][2]] > 0
                            ):
                                rot[3 - z][y][x] = \
                                    self.board_size[x + self.current_piece[0][0]][y + self.current_piece[0][1]][z + self.current_piece[0][2]]
                        except IndexError:
                            del rot
                            return

            for x in range(4):
                for y in range(4):
                    for z in range(4):
                        try:
                            if (self.board_size[x + self.current_piece[0][0]][y + self.current_piece[0][1]][z + self.current_piece[0][2]] < 0 <
                                    rot[x][y][z]):
                                del rot
                                return
                        except IndexError:
                            del rot
                            return

            for x in range(4):
                for y in range(4):
                    for z in range(4):
                        if self.board_size[x + self.current_piece[0][0]][y + self.current_piece[0][1]][
                                z + self.current_piece[0][2]] > 0:
                            self.board_size[x + self.current_piece[0][0]][y + self.current_piece[0][1]][
                                z + self.current_piece[0][2]] = 0
                        if rot[x][y][z] > 0:
                            self.board_size[x + self.current_piece[0][0]][y + self.current_piece[0][1]][
                                z + self.current_piece[0][2]] = rot[x][y][z]
        if dirt_z == 1:
            for x in range(4):
                for y in range(4):
                    for z in range(4):
                        try:
                            if (
                                0 <= x + self.current_piece[0][0] <= 9 and
                                y + self.current_piece[0][1] <= 23 and
                                0 <= z + self.current_piece[0][2] <= 23 and
                                self.board_size[x + self.current_piece[0][0]][y + self.current_piece[0][1]][z + self.current_piece[0][2]] > 0
                            ):
                                rot[y][3 - x][z] = \
                                    self.board_size[x + self.current_piece[0][0]][y + self.current_piece[0][1]][z + self.current_piece[0][2]]
                        except IndexError:
                            del rot
                            return

            for x in range(4):
                for y in range(4):
                    for z in range(4):
                        try:
                            if (self.board_size[x + self.current_piece[0][0]][y + self.current_piece[0][1]][z + self.current_piece[0][2]] < 0 <
                                    rot[x][y][z]):
                                del rot
                                return
                        except IndexError:
                            del rot
                            return

            for x in range(4):
                for y in range(4):
                    for z in range(4):
                        if self.board_size[x + self.current_piece[0][0]][y + self.current_piece[0][1]][
                                z + self.current_piece[0][2]] > 0:
                            self.board_size[x + self.current_piece[0][0]][y + self.current_piece[0][1]][
                                z + self.current_piece[0][2]] = 0
                        if rot[x][y][z] > 0:
                            self.board_size[x + self.current_piece[0][0]][y + self.current_piece[0][1]][
                                z + self.current_piece[0][2]] = rot[x][y][z]

        if dirt_z == -1:
            for x in range(4):
                for y in range(4):
                    for z in range(4):
                        try:
                            if (
                                0 <= x + self.current_piece[0][0] <= 9 and
                                y + self.current_piece[0][1] <= 23 and
                                0 <= z + self.current_piece[0][2] <= 23 and
                                self.board_size[x + self.current_piece[0][0]][y + self.current_piece[0][1]][z + self.current_piece[0][2]] > 0
                            ):
                                rot[3 - y][x][z] = \
                                    self.board_size[x + self.current_piece[0][0]][y + self.current_piece[0][1]][z + self.current_piece[0][2]]
                        except IndexError:
                            del rot
                            return

            for x in range(4):
                for y in range(4):
                    for z in range(4):
                        try:
                            if (self.board_size[x + self.current_piece[0][0]][y + self.current_piece[0][1]][z + self.current_piece[0][2]] < 0 <
                                    rot[x][y][z]):
                                del rot
                                return
                        except IndexError:
                            del rot
                            return

            for x in range(4):
                for y in range(4):
                    for z in range(4):
                        if self.board_size[x + self.current_piece[0][0]][y + self.current_piece[0][1]][
                                z + self.current_piece[0][2]] > 0:
                            self.board_size[x + self.current_piece[0][0]][y + self.current_piece[0][1]][
                                z + self.current_piece[0][2]] = 0
                        if rot[x][y][z] > 0:
                            self.board_size[x + self.current_piece[0][0]][y + self.current_piece[0][1]][
                                z + self.current_piece[0][2]] = rot[x][y][z]

    def move_piece(self, x, y, z):
        if x == 1:
            for x in range(self.current_piece[0][0], self.current_piece[1][0] + 1):
                for y in range(self.current_piece[0][1], self.current_piece[1][1] + 1):
                    for z in range(self.current_piece[0][2], self.current_piece[1][2] + 1):
                        if y < 24 and 0 <= z <= 9 and 0 <= x <= 9 and self.board_size[x][y][z] > 0:
                            if x == 9 or self.board_size[x + 1][y][z] < 0:
                                return

            for x in range(self.current_piece[1][0], self.current_piece[0][0] - 1, -1):
                for y in range(self.current_piece[0][1], self.current_piece[1][1] + 1):
                    for z in range(self.current_piece[0][2], self.current_piece[1][2] + 1):
                        if y < 24 and 0 <= z <= 9 and 0 <= x <= 8 and self.board_size[x][y][z] > 0:
                            self.board_size[x + 1][y][z] = self.board_size[x][y][z]
                            self.board_size[x][y][z] = 0
            self.current_piece[0][0] += 1
            self.current_piece[1][0] += 1

        elif x == -1:
            for x in range(self.current_piece[0][0], self.current_piece[1][0] + 1):
                for y in range(self.current_piece[0][1], self.current_piece[1][1] + 1):
                    for z in range(self.current_piece[0][2], self.current_piece[1][2] + 1):
                        if y < 24 and 0 <= z <= 9 and 0 <= x <= 9 and self.board_size[x][y][z] > 0:
                            if x == 0 or self.board_size[x - 1][y][z] < 0:
                                return

            for x in range(self.current_piece[0][0], self.current_piece[1][0] + 1):
                for y in range(self.current_piece[0][1], self.current_piece[1][1] + 1):
                    for z in range(self.current_piece[0][2], self.current_piece[1][2] + 1):
                        if y < 24 and 0 <= z <= 9 and 1 <= x <= 9 and self.board_size[x][y][z] > 0:
                            self.board_size[x - 1][y][z] = self.board_size[x][y][z]
                            self.board_size[x][y][z] = 0
            self.current_piece[0][0] -= 1
            self.current_piece[1][0] -= 1

        elif z == 1:
            for x in range(self.current_piece[0][0], self.current_piece[1][0] + 1):
                for y in range(self.current_piece[0][1], self.current_piece[1][1] + 1):
                    for z in range(self.current_piece[0][2], self.current_piece[1][2] + 1):
                        if y < 24 and 0 <= z <= 9 and 0 <= x <= 9 and self.board_size[x][y][z] > 0:
                            if z == 9 or self.board_size[x][y][z + 1] < 0:
                                return

            for x in range(self.current_piece[0][0], self.current_piece[1][0] + 1):
                for y in range(self.current_piece[0][1], self.current_piece[1][1] + 1):
                    for z in range(self.current_piece[1][2], self.current_piece[0][2] - 1, -1):
                        if y < 24 and 0 <= z <= 8 and 0 <= x <= 9 and self.board_size[x][y][z] > 0:
                            self.board_size[x][y][z + 1] = self.board_size[x][y][z]
                            self.board_size[x][y][z] = 0
            self.current_piece[0][2] += 1
            self.current_piece[1][2] += 1

        elif z == -1:
            for x in range(self.current_piece[0][0], self.current_piece[1][0] + 1):
                for y in range(self.current_piece[0][1], self.current_piece[1][1] + 1):
                    for z in range(self.current_piece[0][2], self.current_piece[1][2] + 1):
                        if y < 24 and 0 <= z <= 9 and 0 <= x <= 9 and self.board_size[x][y][z] > 0:
                            if z == 0 or self.board_size[x][y][z - 1] < 0:
                                return

            for x in range(self.current_piece[0][0], self.current_piece[1][0] + 1):
                for y in range(self.current_piece[0][1], self.current_piece[1][1] + 1):
                    for z in range(self.current_piece[0][2], self.current_piece[1][2] + 1):
                        if y < 24 and 1 <= z <= 9 and 0 <= x <= 9 and self.board_size[x][y][z] > 0:
                            self.board_size[x][y][z - 1] = self.board_size[x][y][z]
                            self.board_size[x][y][z] = 0
            self.current_piece[0][2] -= 1
            self.current_piece[1][2] -= 1

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
        if not self.is_falling_piece:
            return

        collision = False
        for x in range(self.current_piece[0][0], self.current_piece[1][0] + 1):
            for y in range(self.current_piece[0][1], self.current_piece[1][1] + 1):
                for z in range(self.current_piece[0][2], self.current_piece[1][2] + 1):
                    if y < 24 and 0 <= z <= 9 and 0 <= x <= 9:
                        if self.board_size[x][y][z] <= 0:
                            continue
                        elif y == 23 or self.board_size[x][y + 1][z] < 0:
                            collision = True
        if collision:
            for x in range(self.current_piece[0][0], self.current_piece[1][0] + 1):
                for y in range(self.current_piece[0][1], self.current_piece[1][1] + 1):
                    for z in range(self.current_piece[0][2], self.current_piece[1][2] + 1):
                        if y < 24 and 0 <= z <= 9 and 0 <= x <= 9 and self.board_size[x][y][z] > 0:
                            self.board_size[x][y][z] *= -1
            self.is_falling_piece = False
        else:
            for x in range(self.current_piece[0][0], self.current_piece[1][0] + 1):
                for y in range(self.current_piece[1][1], self.current_piece[0][1] - 1, -1):
                    for z in range(self.current_piece[0][2], self.current_piece[1][2] + 1):
                        if y < 23 and 0 <= z <= 9 and 9 >= x >= 0 and self.board_size[x][y][z] > 0:
                            self.board_size[x][y + 1][z] = self.board_size[x][y][z]
                            self.board_size[x][y][z] = 0
            self.current_piece[0][1] += 1
            self.current_piece[1][1] += 1


