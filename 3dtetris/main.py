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

new_board = board.Board()

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
            if events.key == pygame.K_SPACE:
                # new_board.insert_block((0, 0, 0), random.randint(3, 14))
                new_board.insert_piece(SHAPE_ARRAY[random.randint(0, 7)], (random.randint(2, 8), 1, random.randint(2, 8)), random.randint(3, 14))
                pressed = True
            if events.key == pygame.K_EQUALS:
                new_board.clear_board()
            if events.key == pygame.K_LEFT:
                view -= 1
                if view < 0:
                    view = 3
            if events.key == pygame.K_RIGHT:
                view += 1
                if view > 3:
                    view = 0
            if events.key == pygame.K_UP:
                view = 0
        if events.type == pygame.KEYUP and pressed:
            pressed = False

    if frames == FPS//8:
        frames = 0
        new_board.update_board()

    screen.fill(COLORS.BLACK.value)
    board.draw_border(screen)
    new_board.print_board_data(screen, view)
    new_board.print_x_view(screen)
    new_board.print_y_view(screen)
    new_board.print_z_view(screen)

    pygame.display.flip()

pygame.quit()

