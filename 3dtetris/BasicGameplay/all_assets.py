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
    SHAPE_I_BASE = [(0, 3, 0), (0, 2, 0), (0, 1, 0), (0, 0, 0)]
    SHAPE_O_BASE = [(0, 1, 0), (0, 1, 1), (1, 1, 0), (1, 1, 1)]
    SHAPE_Z_BASE = [(0, 2, -1), (0, 1, -1), (0, 1, 0), (0, 0, 0)]
    SHAPE_L_BASE = [(-1, 2, 0), (0, 2, 0), (0, 1, 0), (0, 0, 0)]
    SHAPE_T_BASE = [(0, 2, 0), (0, 1, 0), (0, 0, 0), (1, 1, 0)]
    SHAPE_Y_BASE = [(0, 2, 0), (1, 2, 0), (0, 1, 0), (0, 2, 1)]
    SHAPE_S_BASE = [(0, 2, 0), (1, 2, 0), (1, 1, 0), (1, 1, 1)]
    SHAPE_EMPTY = []


SHAPE_ARRAY = [
    Shape.SHAPE_I_BASE,
    Shape.SHAPE_O_BASE,
    Shape.SHAPE_Z_BASE,

    Shape.SHAPE_L_BASE,
    Shape.SHAPE_T_BASE,
    Shape.SHAPE_Y_BASE,

    Shape.SHAPE_S_BASE,
    Shape.SHAPE_EMPTY
]


def among_us_init(board_ex):
    board_ex.insert_blocks([
        [(3, 5, 5), 3],
        [(4, 5, 5), 3],
        [(5, 5, 5), 3],
        [(2, 6, 5), 3],
        [(3, 6, 5), 3],
        [(4, 6, 5), 2],
        [(5, 6, 5), 2],
        [(2, 7, 5), 3],
        [(3, 7, 5), 3],
        [(4, 7, 5), 3],
        [(5, 7, 5), 3],
        [(3, 8, 5), 3],
        [(5, 8, 5), 3]
    ])

