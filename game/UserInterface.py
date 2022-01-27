import pygame as pg
import math
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, UI


class UserInterface:
    def __init__(self):
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.TITLE = (212, 255, 233)

        self.titlefont = pg.font.Font('assets/fonts/PixeloidMono-1G8ae.ttf', 100)
        self.regularfont = pg.font.Font('assets/fonts/PixeloidMono-1G8ae.ttf', 20)
        self.largefont = pg.font.Font('assets/fonts/PixeloidMono-1G8ae.ttf', 25)

        # Dev tools UI
        self.FPS_text = self.regularfont.render("0", True, self.GREEN)

        # Score UI
        self.show_score = False
        self.score = 0
        self.score_text = self.regularfont.render('0', True, self.BLACK)
        self.multiplier = 2
        self.multiplier_text = self.largefont.render('02', True, self.BLACK)

        # Start Screen UI
        self.show_start_screen = True
        self.start_text = self.titlefont.render(f'Press Space', True, self.TITLE)

        # End Screen UI

    def add_point(self, ball_group):
        for ball in ball_group.sprites():
            self.score += 1

    def update(self, fps, ball_group, columns):
        if not UI:
            return
        if len(ball_group.sprites()) == 1:
            self.multiplier = 1

        # FPS
        fps_str = f'FPS: {str(round(fps, 2))}'
        self.FPS_text = self.largefont.render(fps_str, True, self.BLACK)

        # Score
        score_string = f'Score: {str(self.score)}'
        self.score_text = self.largefont.render(score_string, True, self.BLACK)

        # Multiplier
        multiplier_string = f'Multiplier: {str(self.multiplier)}'
        self.multiplier_text = self.largefont.render(multiplier_string, True, self.BLACK)

    def draw(self, screen, laptop=False):
        x1 = SCREEN_WIDTH - 200
        x2 = 10
        y1 = 10
        y2 = 10
        offset1 = 30
        if laptop:
            x1 = SCREEN_WIDTH - 400
            x2 = 180
            y1 = 100
            y2 = 100

        # UI for troubleshooting
        if UI:
            screen.blit(self.FPS_text, (x1, y1))

        if self.show_start_screen:
            screen.blit(self.start_text, (SCREEN_WIDTH / 2 - self.start_text.get_width() / 2, SCREEN_HEIGHT / 2 - 50))

        if self.show_score:
            screen.blit(self.score_text, (x2, y2))
            screen.blit(self.multiplier_text, (x2, y2 + 40))



