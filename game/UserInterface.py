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

        self.smallfont = pg.font.SysFont("Verdana", 10)
        self.regularfont = pg.font.SysFont("Verdana", 20)
        self.largefont = pg.font.SysFont("Verdana", 40)

        self.FPS_text = self.regularfont.render("0", True, self.WHITE)
        self.ball_vel = self.regularfont.render("0", True, self.WHITE)
        self.ball_bottom_y = self.regularfont.render("0", True, self.WHITE)
        self.col1_vel = self.regularfont.render("0", True, self.WHITE)
        self.col1_top = self.regularfont.render("0", True, self.WHITE)
        self.collision_check = self.regularfont.render("0", True, self.WHITE)
        self.ball_collisions = self.regularfont.render("0", True, self.WHITE)
        self.column_collisions = self.regularfont.render("0", True, self.WHITE)

    def update(self, fps, balls, columns):
        if not UI:
            return

        # FPS
        fps_str = f'FPS: {str(round(fps, 2))}'
        self.FPS_text = self.regularfont.render(fps_str, True, self.WHITE)

        # Ball Y Velocity
        # try:
        #     ball = balls[0]
        #     ball_vel_str = f'Ball_y_vel: {str(round(ball.vel.y, 2))}'
        #     self.ball_vel = self.regularfont.render(ball_vel_str, True, self.WHITE)
        # except IndexError:
        #       print("Ball 0 was destroyed")

        # Ball bottom pos
        ball_bottom = f'Ball_pos.y: {str(round(ball.rect.bottom, 2))}'
        self.ball_bottom_y = self.regularfont.render(ball_bottom, True, self.WHITE)

        # Ball Collisions
        ball_collisions = f'CollisionTypes: {str(ball.collision_types)}'
        self.ball_collisions = self.regularfont.render(ball_collisions, True, self.WHITE)

        # Column 1 collisions
        column_collisions = f'ColumnsCollidedWith: {str(ball.collisions)}'
        self.column_collisions = self.regularfont.render(column_collisions, True, self.WHITE)

        # Column 1 vel
        column_1 = columns[1]
        col_vel_str = f'Col1_vel.y: {str(round(column_1.vel.y, 2))}'
        self.col1_vel = self.regularfont.render(col_vel_str, True, self.WHITE)

        # Column 1 top
        col_top_str = f'Col1_top: {str(round(column_1.rect.top, 2))}'
        self.col1_top = self.regularfont.render(col_top_str, True, self.WHITE)

        # Collisions check
        collisions__check = f'Bottom_1=top: {ball.rect.bottom == column_1.rect.top}'
        self.collision_check = self.regularfont.render(collisions__check, True, self.WHITE)

    def draw(self, screen, laptop=False):
        x1 = SCREEN_WIDTH - 200
        x2 = 10
        y1 = 10
        y2 = 10
        offset1 = 30
        if laptop:
            x1 = SCREEN_WIDTH - 400
            x2 = 200
            y1 = 100
            y2 = 100

        # UI for troubleshooting
        if UI:
            screen.blit(self.FPS_text, (x1, y1))
            # screen.blit(self.ball_vel, (x1, y1 + offset1))
            screen.blit(self.col1_vel, (x1, y1 + offset1 * 2))
            screen.blit(self.ball_bottom_y, (x1, y1 + offset1 * 3))
            screen.blit(self.col1_top, (x1, y1 + offset1 * 4))
            screen.blit(self.collision_check, (x1, y1 + offset1 * 5))

            screen.blit(self.ball_collisions, (x2, y2))
            screen.blit(self.column_collisions, (x2, y2 + offset1))
