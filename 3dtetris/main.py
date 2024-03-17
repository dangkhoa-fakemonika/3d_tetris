import random

import pygame

from all_assets import *
import blocks
import board

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
view = 0

game_clock = pygame.time.Clock()
frames = 1
falling = False
x_spin = 0
y_spin = 0
z_spin = 0

new_board = board.Board()
p = 0

run = True
pressed = False
while run:
    game_clock.tick(FPS)
    frames += 1

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run = False
            break
        if events.type == pygame.KEYDOWN and not pressed:
            # Manually spawn pieces
            if events.key == pygame.K_SPACE:
                new_board.insert_piece(SHAPE_ARRAY[p], (3, 8, 3), random.randint(3, 14))
                pressed = True

            # Clear board
            if events.key == pygame.K_EQUALS:
                new_board.clear_board()

            # Move view
            if events.key == pygame.K_LEFT:
                view -= 1
                if view < 0:
                    view = 3
            if events.key == pygame.K_RIGHT:
                view += 1
                if view > 3:
                    view = 0

            if events.key == pygame.K_x:
                if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    new_board.move_piece(-1, 0, 0)
                else:
                    new_board.move_piece(1, 0, 0)
                pressed = True

            if events.key == pygame.K_z:
                if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    new_board.move_piece(0, 0, -1)
                else:
                    new_board.move_piece(0, 0, 1)
                pressed = True

            if events.key == pygame.K_q:
                x_spin += 1
                x_spin %= 4

            if events.key == pygame.K_w:
                y_spin += 1
                y_spin %= 4

            if events.key == pygame.K_e:
                z_spin += 1
                z_spin %= 4

            # Reset view
            if events.key == pygame.K_UP:
                view = 0
        if events.type == pygame.KEYUP and pressed:
            pressed = False

    # Update frames
    if frames == FPS:
        frames = 0
        # new_board.update_board()
        if not new_board.is_falling_piece:
            new_board.insert_piece(SHAPE_ARRAY[p], (3, 4, 3), random.randint(3, 14))
        # p += 1
        # p %= 7
        print(x_spin + 1, y_spin + 1, z_spin + 1)

    new_board.spin_piece(x_spin, y_spin, z_spin)
    screen.fill(COLORS.BLACK.value)
    board.draw_border(screen)
    new_board.print_board_data(screen, view)
    new_board.print_x_view(screen)
    new_board.print_y_view(screen)
    new_board.print_z_view(screen)

    pygame.display.flip()

pygame.quit()

