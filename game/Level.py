import pygame as pg
from .Column import Column
from .Ball import Ball
from .Projectile import Projectile


class Level:
    def __init__(self, level_data, screen, ball_data, projectile_data):
        self.screen = screen
        self.level_data = level_data
        self.BACKGROUND = None

        # Dictionary of column objects. {1: column1, 2: column2}
        self.columns = {}
        self.column_group = pg.sprite.Group()
        self._create_columns(self.level_data)

        # Generate the ball for the level
        self.balls = []
        self.ball_group = pg.sprite.Group()
        self._create_balls(ball_data)

        # Storage for the projectiles
        self.projectiles = []
        self.projectile_group = pg.sprite.Group()
        self._create_projectiles(projectile_data)

    def _create_columns(self, level_data):
        """ Creates column objects from column information passed in """
        # Level data is a list of dictionaries for each column [{}, {}, {}, {}... {}]
        for column_data in level_data:
            column = Column(column_data)
            self.columns[column.number] = column
            self.column_group.add(column)

    def _create_balls(self, ball_data):
        for ball_info in ball_data:
            ball = Ball(ball_info)
            self.balls.append(ball)
            self.ball_group.add(ball)

    def _create_projectiles(self, projectile_data):
        # Projectile data = [{}, {}, {}, ... {}]
        # List of data needed to create a projectile
        for projectile_info in projectile_data:
            projectile = Projectile(projectile_info)
            self.projectiles.append(projectile)
            self.projectile_group.add(projectile)

    def get_column(self, n: int):
        return self.columns[n]

    def add_background(self, image):
        self.BACKGROUND = image

    def draw_background(self):
        self.screen.blit(self.BACKGROUND, (0, 0))

    def update_columns(self):
        for column in self.columns.values():
            column.update()

    def draw_columns(self):
        for column in self.columns.values():
            column.draw(self.screen)

    def update_balls(self):
        for ball in self.balls:
            ball.update(self.column_group)

    def draw_balls(self):
        for ball in self.balls:
            ball.draw(self.screen)

    def update_projectiles(self):
        for projectile in self.projectiles:
            projectile.update(self.ball_group)

    def draw_projectiles(self):
        for projectile in self.projectile_group:
            projectile.draw(self.screen)






