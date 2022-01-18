import pygame as pg
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from .Level import Level

# The level manager stores data for each level, loads and swithces beteween levels
class Level_Manager:
    def __init__(self, screen):
        # A list of level objects
        self.levels = []
        self.level = 1


        # Level 1
        L1 = Level(self.generate_level_1_data(), screen)
        self.levels.append(L1)
        # L1.add_background #TODO
        # L1.add_obsticle_spikes #TODO
        # L1.etc.etc.etc #TODO

    def get_level(self):
        return self.levels[self.level - 1]

    def set_level(self, n):
        level = self.levels[n-1]

    def next_level(self):
        self.level += 1




    # Maybe all this data eventually gets moved to a JSON file #TODO
    def generate_level_1_data(self):
        # Level 1 Data: [{column1_data}, {column2_data}, {...}, {...}... {column10_data}]
        level1_data = []
        i = 0
        for column in range(1, 11):
            column = {
                'number': i + 1,
                'width': SCREEN_WIDTH / 10,
                'height': SCREEN_HEIGHT,
                'pos_x': (SCREEN_WIDTH / 10) * i,
                'pos_y': (SCREEN_HEIGHT / 3) * 2,
                'mass': 10,
                'image': '',
                'sound_up': '',
                'sound_down': '',
                'spring_constant': 0,
                'friction': -0.1,
                'force_up': -0.5,
                'max_y': (SCREEN_HEIGHT / 3) * 2,
                'gravity': 0.5
            }
            level1_data.append(column)
            i += 1
        return level1_data


