from all_assets import *


def cast_to_2d(pos):
    return (pos[2] - pos[0]) * 13, (pos[2] + pos[0]) * 7.5 + pos[1] * 16


def print_cube(pos, screen, color):
    new_pos = cast_to_2d(pos)

    pygame.draw.polygon(screen, color, [
        (new_pos[0] + 217, new_pos[1] + 68.5),
        (new_pos[0] + 230, new_pos[1] + 61),
        (new_pos[0] + 243, new_pos[1] + 68.5),
        (new_pos[0] + 243, new_pos[1] + 84.5),
        (new_pos[0] + 230, new_pos[1] + 92),
        (new_pos[0] + 217, new_pos[1] + 84.5)
    ])

    pygame.draw.aalines(screen, (255, 255, 255), False, [
        (new_pos[0] + 217, new_pos[1] + 68.5),
        (new_pos[0] + 230, new_pos[1] + 61),
        (new_pos[0] + 243, new_pos[1] + 68.5),
        (new_pos[0] + 243, new_pos[1] + 84.5),
        (new_pos[0] + 230, new_pos[1] + 92),
        (new_pos[0] + 217, new_pos[1] + 84.5),
        (new_pos[0] + 217, new_pos[1] + 68.5),
        (new_pos[0] + 230, new_pos[1] + 76),
        (new_pos[0] + 230, new_pos[1] + 92),
        (new_pos[0] + 230, new_pos[1] + 76),
        (new_pos[0] + 243, new_pos[1] + 68.5)
    ])


def print_shadow(pos, screen):
    x_pos = (pos[2]) * 13, (pos[2]) * 7.5 + pos[1] * 16
    y_pos = (pos[2] - pos[0]) * 13, (pos[2] + pos[0]) * 7.5 + 304
    z_pos = (- pos[0]) * 13, (pos[0]) * 7.5 + pos[1] * 16

    pygame.draw.aalines(screen, (150, 150, 150), True, [
        (x_pos[0] + 230, x_pos[1] + 61),
        (x_pos[0] + 243, x_pos[1] + 68.5),
        (x_pos[0] + 243, x_pos[1] + 84.5),
        (x_pos[0] + 230, x_pos[1] + 76),
    ])

    pygame.draw.aalines(screen, (150, 150, 150), True, [
        (y_pos[0] + 230, y_pos[1] + 76),
        (y_pos[0] + 243, y_pos[1] + 84.5),
        (y_pos[0] + 230, y_pos[1] + 92),
        (y_pos[0] + 217, y_pos[1] + 84.5)
    ])

    pygame.draw.aalines(screen, (150, 150, 150), True, [
        (z_pos[0] + 230, z_pos[1] + 61),
        (z_pos[0] + 217, z_pos[1] + 68.5),
        (z_pos[0] + 217, z_pos[1] + 84.5),
        (z_pos[0] + 230, z_pos[1] + 76)
    ])


class TestPiece:
    def __init__(self, center, color, block_type):
        self.pos_center = center
        self.block_type = block_type
        self.name = "example name"
        self.color = color
        self.states = 0
        self.valid_move = [True, True, True, True]

    def __str__(self):
        return self.name

    def insert_piece(self, new_board):
        pass

    def update_center(self, new_pos):
        self.pos_center = new_pos

    def print_blocks(self, surface):
        for block in self.pos_blocks:
            map_pos = (self.pos_center[0] + block[0], self.pos_center[1] + block[1], self.pos_center[2] + block[2])
            print_shadow(map_pos, surface)
            print_cube(map_pos, surface, self.color)

    def check_collision(self):
        self.valid_move = [True, True, True, True]
        for block in self.pos_blocks:
            map_pos = (self.pos_center[0] + block[0], self.pos_center[1] + block[1], self.pos_center[2] + block[2])
            if self.valid_move[0] and map_pos[0] == 0:
                self.valid_move[0] = False
            if self.valid_move[1] and map_pos[0] == 9:
                self.valid_move[1] = False
            if self.valid_move[2] and map_pos[2] == 0:
                self.valid_move[2] = False
            if self.valid_move[3] and map_pos[2] == 9:
                self.valid_move[3] = False

    def spin(self, spin_pos):
        pass




