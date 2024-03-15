import pygame
from enum import Enum
import blocks


WIDTH = 1280
HEIGHT = 720


class COLORS(Enum):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    YELLOW = (255, 255, 0)
    VIOLET = (255, 0, 255)
    AQUA = (0, 255, 255)

    ORANGE = (255, 128, 0)
    LIME = (128, 255, 0)
    PINK = (255, 0, 128)
    PURPLE = (128, 0, 255)
    SKY = (0, 128, 255)
    EMERALD = (0, 255, 128)
    KAFKA = (int("99", 16), int("0F", 16), int("48", 16))


COLOR_ARRAY = [
    COLORS.BLACK.value,
    COLORS.WHITE.value,
    COLORS.RED.value,
    COLORS.BLUE.value,

    COLORS.GREEN.value,
    COLORS.YELLOW.value,
    COLORS.VIOLET.value,
    COLORS.AQUA.value,

    COLORS.ORANGE.value,
    COLORS.LIME.value,
    COLORS.PINK.value,
    COLORS.PURPLE.value,

    COLORS.SKY.value,
    COLORS.EMERALD.value,
    COLORS.KAFKA.value
]


class Shape(Enum):
    SHAPE_I_BASE = [
        [(0, 3, 0), (0, 2, 0), (0, 1, 0), (0, 0, 0)],
        [(0, 1, 0), (0, 1, 1), (0, 1, 2), (0, 1, 3)],
        [(0, 1, 0), (1, 0, 1), (2, 1, 0), (3, 1, 0)]
    ]
    SHAPE_O_BASE = [
        [(0, 0, 0), (1, 0, 0), (0, 0, 1), (1, 0, 1)]
    ]
    SHAPE_Z_BASE = [(0, 2, -1), (0, 1, -1), (0, 1, 0), (0, 0, 0)]
    SHAPE_L_BASE = [(-1, 2, 0), (0, 2, 0), (0, 1, 0), (0, 0, 0)]
    SHAPE_T_BASE = [(0, 2, 0), (0, 1, 0), (0, 0, 0), (1, 1, 0)]
    SHAPE_Y_BASE = [(0, 0, -1), (1, 0, -1), (0, -1, -1), (0, 0, 0)]
    SHAPE_S_BASE = [(0, 1, 0), (0, 0, 0), (1, 1, 0), (1, 1, 1)]
    SHAPE_EMPTY = []


def display_amongus(screen):

    among = blocks.TestPiece((3, 0, 3), COLORS['RED'].value)
    among.pos_blocks = (
            [(-1, y + 1, z + 1) for z in range(3) for y in range(4, -1, -1)] +
            [(x, y + 6, z) for z in range(2) for y in range(2, -1, -1) for x in range(3)] +
            [(x, y + 6, z + 3) for z in range(2) for y in range(2, -1, -1) for x in range(3)] +
            [(x, y + 1, z) for z in range(5) for y in range(4, -1, -1) for x in range(3)] +
            [(x, 0, z + 1) for z in range(3) for x in range(3)]
    )

    us = blocks.TestPiece((6, 1, 3), COLORS['WHITE'].value)
    us.pos_blocks = [(0, 0, 3), (0, 0, 2), (0, 0, 1), (0, 0, 0)]

    us_2 = blocks.TestPiece((6, 1, 3), COLORS['WHITE'].value)
    us_2.pos_blocks = [(0, 1, 0)]

    sus = blocks.TestPiece((6, 1, 3), COLORS['SKY'].value)
    sus.pos_blocks = [(0, 2, z) for z in range(5)]

    sus_2 = blocks.TestPiece((6, 1, 3), COLORS['SKY'].value)
    sus_2.pos_blocks = [(0, 1, z + 1) for z in range(4)]

    sus_3 = blocks.TestPiece((6, 1, 3), COLORS['SKY'].value)
    sus_3.pos_blocks = [(0, 0, 4)]

    among.print_blocks(screen)
    sus.print_blocks(screen)
    us_2.print_blocks(screen)
    sus_2.print_blocks(screen)
    us.print_blocks(screen)
    sus_3.print_blocks(screen)

