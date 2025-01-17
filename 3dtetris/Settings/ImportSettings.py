from json import load
import pygame


def get_settings() -> dict[str : pygame.key]:
    # get_keys = {
    #     "a": pygame.K_a,
    #     "b": pygame.K_b,
    #     "c": pygame.K_c,
    #     "d": pygame.K_d,
    #     "e": pygame.K_e,
    #     "f": pygame.K_f,
    #     "g": pygame.K_g,
    #     "h": pygame.K_h,
    #     "i": pygame.K_i,
    #     "j": pygame.K_j,
    #     "k": pygame.K_k,
    #     "l": pygame.K_l,
    #     "m": pygame.K_m,
    #     "n": pygame.K_n,
    #     "o": pygame.K_o,
    #     "p": pygame.K_p,
    #     "q": pygame.K_q,
    #     "r": pygame.K_r,
    #     "s": pygame.K_s,
    #     "t": pygame.K_t,
    #     "u": pygame.K_u,
    #     "v": pygame.K_v,
    #     "w": pygame.K_w,
    #     "x": pygame.K_x,
    #     "y": pygame.K_y,
    #     "z": pygame.K_z,
    #     "left": pygame.K_LEFT,
    #     "right": pygame.K_RIGHT,
    #     "up": pygame.K_UP,
    #     "down": pygame.K_DOWN,
    #     "space": pygame.K_SPACE
    # }

    file = open("controls.json", "r")
    controls = load(file)
    my_controls: dict = {}

    for keys in controls:
        my_controls[keys] = ord(controls[keys][0])

    return my_controls


if __name__ == "__main__":
    get_settings()