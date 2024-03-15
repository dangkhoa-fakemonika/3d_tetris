import random

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

# new_board.insert_blocks([
#     [(0, 0, 0), 1],
#     [(1, 2, 3), 2],
#     [(4, 5, 7), 3],
#     [(9, 10, 2), 4],
#     [(3, 5, 9), 5],
#     [(0, 12, 0), 6],
#     [(7, 7, 7), 7],
#     [(2, 0, 2), 8],
#     [(8, 11, 3), 9],
#     [(5, 5, 5), 10],
#     [(6, 3, 0), 11],
#     [(9, 9, 9), 12],
#     [(5, 14, 5), 13],
#     [(9, 19, 9), 14]
# ])

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
                new_board.insert_block((random.randint(0, 9), 0, random.randint(0, 9)), random.randint(3, 14))
                pressed = True
            if events.key == pygame.K_LEFT:
                view -= 1
                if view < 0:
                    view = 3
            if events.key == pygame.K_RIGHT:
                view += 1
                if view > 3:
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

