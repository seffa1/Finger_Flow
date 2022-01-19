import pygame as pg
import math
from settings import SCREEN_WIDTH, SCREEN_HEIGHT


class UserInterface:
    def __init__(self):
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)

        self.smallfont = pg.font.SysFont("Verdana", 10)
        self.regularfont = pg.font.SysFont("Verdana", 20)
        self.largefont = pg.font.SysFont("Verdana", 40)

        self.text = self.regularfont.render("0", True, self.BLACK)

    def update(self, fps):
        fps_str = f'FPS: {str(round(fps, 2))}'
        self.text = self.regularfont.render(fps_str, True, self.WHITE)

    def draw(self, screen, show_fps=True):
        if show_fps:
            screen.blit(self.text, (SCREEN_WIDTH - 130, 10))