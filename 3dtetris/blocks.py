from all_assets import *


# Cast 3d to 2d
def cast_to_2d(pos):
    return (pos[2] - pos[0]) * 13, (pos[2] + pos[0]) * 7.5 + pos[1] * 16


# Print individual cubes
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


# Print on_going pieces shadows
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




