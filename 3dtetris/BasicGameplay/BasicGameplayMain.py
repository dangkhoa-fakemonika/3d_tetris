import random
import pygame
from all_assets import *
import board


def basic_gameplay(fps: int, cur_screen: pygame.Surface):
    view = 0
    game_clock = pygame.time.Clock()
    frames = 1
    run = True
    pressed = False
    pause = False
    new_board = board.Board()

    while run:
        game_clock.tick(fps)
        frames += 1

        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                run = False
                break
            if events.type == pygame.KEYDOWN and not pressed:
                # Manually spawn pieces
                if events.key == pygame.K_p:
                    pause = not pause
                    pressed = True

                # Clear board
                if events.key == pygame.K_EQUALS:
                    new_board.clear_board()
                    pressed = True

                # Move view
                if events.key == pygame.K_LEFT:
                    view -= 1
                    if view < 0:
                        view = 3
                    pressed = True
                if events.key == pygame.K_RIGHT:
                    view += 1
                    if view > 3:
                        view = 0
                    pressed = True

                # Reset view
                if events.key == pygame.K_UP:
                    view = 0

                # Movements
                if not pause:
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

                    if events.key == pygame.K_c:
                        new_board.move_piece(0, 1, 0)

                    if events.key == pygame.K_SPACE:
                        new_board.move_piece(0, 100, 0)

                    # Spin piece
                    if events.key == pygame.K_e:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            new_board.spin_piece(0, 0, -1)
                        else:
                            new_board.spin_piece(0, 0, 1)
                        pressed = True

                    if events.key == pygame.K_w:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            new_board.spin_piece(0, -1, 0)
                        else:
                            new_board.spin_piece(0, 1, 0)
                        pressed = True

                    if events.key == pygame.K_q:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            new_board.spin_piece(-1, 0, 0)
                        else:
                            new_board.spin_piece(1, 0, 0)
                        pressed = True

            if events.type == pygame.KEYUP and pressed:
                pressed = False

        # Update frames
        if frames == fps:
            frames = 0
            if not pause:
                new_board.update_board()
                new_board.update_matches()
                if not new_board.is_falling_piece:
                    new_board.insert_piece(SHAPE_ARRAY[random.randint(0, 6)], (random.randint(3, 7), 0, random.randint(3, 7)), random.randint(3, 14))

        cur_screen.fill(COLORS.BLACK.value)
        board.draw_border(cur_screen)
        new_board.print_board_data(cur_screen, view)
        new_board.print_x_view(cur_screen)
        new_board.print_y_view(cur_screen)
        new_board.print_z_view(cur_screen)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Test mode in gameplay")
    screen = pygame.display.set_mode((1280, 720))
    basic_gameplay(60, screen)
