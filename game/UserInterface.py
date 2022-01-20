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

        self.FPS_text = self.regularfont.render("0", True, self.WHITE)
        self.ball_vel = self.regularfont.render("0", True, self.WHITE)

    def update(self, fps, balls):
        fps_str = f'FPS: {str(round(fps, 2))}'
        self.FPS_text = self.regularfont.render(fps_str, True, self.WHITE)

        ball = balls[0]
        ball_vel_str = f'Ball_y_vel: {str(round(ball.vel.y, 2))}'
        self.ball_vel = self.regularfont.render(ball_vel_str, True, self.WHITE)

    def draw(self, screen, show_UI=True):
        if show_UI:
            screen.blit(self.FPS_text, (SCREEN_WIDTH - 170, 10))
            screen.blit(self.ball_vel, (SCREEN_WIDTH - 170, 40))