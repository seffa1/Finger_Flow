import random

import pygame as pg
from .Column import Column
from .Ball import Ball
from .Projectile import Projectile


class Level:
    def __init__(self, level_data, screen, ball_data, projectile_data, particle_manager, music_manager, level_manager):
        self.particle_manager = particle_manager
        self.music_manager = music_manager
        self.level_manager = level_manager
        self.screen = screen
        self.level_data = level_data
        self.BACKGROUND = None

        # Used for the level starting animation
        self.level_start = True
        # Time keeper of the animation
        self.timer = 0
        # Keep track of what column we are accelerating
        self.column_num = 1

        # Dictionary of column objects. {1: column1, 2: column2}
        self.columns = {}
        self.column_group = pg.sprite.Group()
        self._create_columns(self.level_data)
        self.max_y = self.columns[1].MAX_Y

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
            ball = Ball(ball_info, self.music_manager, self.level_manager)
            self.balls.append(ball)
            self.ball_group.add(ball)

    def _create_projectiles(self, projectile_data):
        # Projectile data = [{}, {}, {}, ... {}]
        # List of data needed to create a projectile
        for projectile_info in projectile_data:
            projectile = Projectile(projectile_info)
            self.projectiles.append(projectile)
            self.projectile_group.add(projectile)

    def start_level(self):
        self.level_start = True

    def get_column(self, n: int):
        return self.columns[n]

    def add_background(self, image):
        self.BACKGROUND = image

    def draw_background(self):
        self.screen.blit(self.BACKGROUND, (0, 0))

    def update_columns(self):
        if self.level_start:
            # Level start animation
            # How long to wait before accelerating the next column
            column_duration = 10

            column = self.get_column(self.column_num)
            if self.timer % column_duration == 0:
                column.deccelerate()
                self.column_num += 1

            if self.column_num < 11:
                column = self.get_column(self.column_num)
                column.accelerate()
                self.timer += 1
            else:
                self.level_start = False

        # The actual update for the columns
        for column in self.columns.values():
            column.update()

    def draw_columns(self):
        for column in self.columns.values():
            column.draw(self.screen)

    def update_balls(self):
        for ball in self.ball_group:
            prev_collision = ball.collision_types['bottom']
            prev_vel = ball.vel.y
            # print(f'prev bottom: {prev_collision}')
            ball.update(self.column_group, self.projectile_group, self.max_y)
            curent_collision = ball.collision_types['bottom']
            # If the ball just changed from not being collided on the bottom, to being collided
            # print(f'current bottom: {curent_collision}')
            if not prev_collision and curent_collision:
                self.particle_manager.emmit(ball.pos, prev_vel)

                # Randomly play a sound
                sound_num = random.randint(2, 6)
                sound_key_list = list(self.music_manager.sounds)
                sound = sound_key_list[sound_num]
                self.music_manager.load_sound(sound, .4)

    def draw_balls(self):
        for ball in self.ball_group:
            ball.draw(self.screen)

    def update_projectiles(self):
        for projectile in self.projectile_group:
            projectile.update(self.ball_group)

    def draw_projectiles(self):
        for projectile in self.projectile_group:
            projectile.draw(self.screen)






