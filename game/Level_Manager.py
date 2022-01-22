import pygame as pg
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, GRAVITIES
from .Level import Level



# The level manager stores colum and ball data for each level, loads and swithces beteween levels
class Level_Manager:
    def __init__(self, screen, projectile_manager):

        # A list of level objects
        self.levels = []
        self.level = 1

        # Level 1
        L1 = Level(self.generate_level_1_column_data(), screen, self.level_1_ball_data(), projectile_manager.start_level_1)
        self.levels.append(L1)
        # L1.add_background #TODO
        # L1.add_obsticle_spikes #TODO
        # L1.etc.etc.etc #TODO

    def get_level(self):
        return self.levels[self.level - 1]

    def set_level(self, n):
        level = self.levels[n - 1]

    def next_level(self):
        self.level += 1

    # Maybe all this data eventually gets moved to a JSON file #TODO
    def generate_level_1_column_data(self):
        # Level 1 Data: [{column1_data}, {column2_data}, {...}, {...}... {column10_data}]
        level1_column_data = []
        i = 0
        for column in range(1, 11):
            column = {
                'number': i + 1,
                'width': SCREEN_WIDTH / 10,
                'height': SCREEN_HEIGHT,
                'pos_x': (SCREEN_WIDTH / 10) * i,
                'pos_y': (SCREEN_HEIGHT / 3) * 2,
                'mass': 100,
                'image': '',
                'sound_up': '',
                'sound_down': '',
                'spring_constant': 0,
                'friction': .8,
                'force_up': -80,
                'max_y': (SCREEN_HEIGHT / 3) * 3 - 300,
                'gravity': GRAVITIES[1],
                'min_y': 300
            }
            level1_column_data.append(column)
            i += 1
        return level1_column_data

    def level_1_ball_data(self):
        balls = []

        ball_1_data = {
            'diameter': 20,
            'mass': 6,
            'friction': 0.5,
            'pos_x': 590,
            'pos_y': 6,
            'vel_x': 0,
            'vel_y': 0,
            'image': pg.image.load('assets/images/ball_D20.png').convert_alpha(),
            'gravity': GRAVITIES[2],
            'image_scale': (100, 100),
            'num': 1
        }

        ball_2_data = {
            'diameter': 20,
            'mass': 6,
            'friction': 0.5,
            'pos_x': 1100,
            'pos_y': 6,
            'vel_x': 0,
            'vel_y': 0,
            'image': pg.image.load('assets/images/ball_D20.png').convert_alpha(),
            'gravity': GRAVITIES[2],
            'image_scale': (100, 100),
            'num': 1
        }

        balls.append(ball_1_data)
        balls.append(ball_2_data)
        return balls

    def level_1_projectile_data(self):
        projectile_data = [
            # Projectile 1
            {'pos_x': SCREEN_WIDTH,
             'pos_y': SCREEN_HEIGHT/2,
             'speed': -3,
             'image': pg.image.load('assets/images/ball_D20.png').convert_alpha(),
             'num': 1},

            # Projectile 2
            {'pos_x': -300,
             'pos_y': SCREEN_HEIGHT/2,
             'speed': 3,
             'image': pg.image.load('assets/images/ball_D20.png').convert_alpha(),
             'num': 2},

            # Projectile 3
            {'pos_x': SCREEN_WIDTH + 600,
             'pos_y': SCREEN_HEIGHT/2,
             'speed': -3,
             'image': pg.image.load('assets/images/ball_D20.png').convert_alpha(),
             'num': 3}
        ]
        return projectile_data



