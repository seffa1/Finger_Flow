import pygame as pg
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, GRAVITIES
from .Level import Level


# The level manager stores columns and ball data for each level, loads and swithces beteween levels
class Level_Manager:
    def __init__(self, screen, projectile_manager):
        # Level manager events
        self.level_ended = pg.USEREVENT + 1
        self.game_complete = pg.USEREVENT + 2

        # A list of level objects
        self.levels = []
        self.level = 1

        # Level 1
        L1 = Level(self.generate_level_1_column_data(), screen, self.level_1_ball_data(), projectile_manager.get_level_data(1))
        L1.add_background(pg.image.load('assets/images/background_1.jpg').convert_alpha())
        self.levels.append(L1)

        # Level 2
        L2 = Level(self.generate_level_1_column_data(), screen, self.level_1_ball_data(), projectile_manager.get_level_data(2))
        L2.add_background(pg.image.load('assets/images/background_1.jpg').convert_alpha())
        self.levels.append(L2)

    def check_level_state(self):
        # If all the levels projectile are gone (made it to the left side of the screen)
        level = self.get_level()
        sprite_group = level.projectile_group

        # Group.sprites returns a list of contained sprites
        # If theres no more projectiles in tqhe group
        if len(sprite_group.sprites()) == 0:
            # If theres no more levels after this
            if len(self.levels) < self.level + 1:
                pg.time.set_timer(self.game_complete, 10)
            # There are more levels to go to
            else:
                # Calls the event after 10 ms
                pg.time.set_timer(self.level_ended, 10)

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
                'pos_y': SCREEN_HEIGHT - 200,
                'mass': 100,
                'image': '',
                'sound_up': '',
                'sound_down': '',
                'spring_constant': 0,
                'friction': .8,
                'force_up': -80,
                'max_y': SCREEN_HEIGHT - 200,
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




