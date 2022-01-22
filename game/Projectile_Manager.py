import pygame as pg
import random
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from .Projectile import Projectile


# Stores information for the projectiles to be passed into the level classes
class Projectile_Manager:
    def __init__(self):
        self.level_data = {
            1: self.level_1_data(),
            2: self.level_2_data()
        }

    def get_level_data(self, n: int):
        return self.level_data[n]

    def level_1_data(self):
        level_data = []
        level_data.append(self.low_wall(SCREEN_WIDTH, 700, -5))
        level_data.append(self.high_wall(SCREEN_WIDTH + 400, 400, -5))
        level_data.append(self.low_wall(SCREEN_WIDTH + 800, 700, -5))
        level_data.append(self.high_wall(SCREEN_WIDTH + 1200, 400, -5))
        level_data.append(self.low_wall(SCREEN_WIDTH + 1600, 700, -5))
        return level_data

    def level_2_data(self):
        level_data = []
        # Low walls
        level_data.append(self.low_wall(SCREEN_WIDTH, height=800, speed=-5))
        level_data.append(self.low_wall(SCREEN_WIDTH + 500, height=600, speed=-5))
        level_data.append(self.low_wall(SCREEN_WIDTH + 1000, height=400, speed=-5))

        # High walls
        level_data.append(self.high_wall(SCREEN_WIDTH, height=200, speed=-5))
        level_data.append(self.high_wall(SCREEN_WIDTH + 500, height=400, speed=-5))
        level_data.append(self.high_wall(SCREEN_WIDTH + 1000, height=600, speed=-5))
        return level_data

    # Low wall
    def low_wall(self, x, height, speed):
        wall_data = {
            'width': 50,
            'height': 800,
            'vel': speed,
            'pos_x': x,
            'pos_y': SCREEN_HEIGHT - height,
        }
        return wall_data

    # High wall
    def high_wall(self, x, height, speed):
        wall_data = {
            'width': 50,
            'height': height,
            'vel': speed,
            'pos_x': x,
            'pos_y': 0,
        }
        return wall_data



    # Currently not being used
    def _gen_projectiles(self, qty, speed):
        right = SCREEN_WIDTH
        bottom = SCREEN_HEIGHT

        # A list of coordinate tuples for the initial position of the projectiles
        cords = []
        for i in range(0, qty):

            num_x = random.randint(right + 50, right + 5000)
            num_y = random.randint(10, bottom - 40)

            projectile_spawn_cords = (num_x, num_y)

            cords.append(projectile_spawn_cords)

        for cord in cords:
            projectile = Projectile(cord[0], cord[1], speed)
            self.projectile_group.add(projectile)








