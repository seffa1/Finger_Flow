import pygame as pg
import random
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from .Projectile import Projectile


# Stores information for the projectiles to be passed into the level classes
class Projectile_Manager:
    def __init__(self):
        self.level_data = {
            1: [self.wall_1(SCREEN_WIDTH + 20, -3), self.wall_1(SCREEN_WIDTH + 520, -3)],
            2: []
        }

    def get_level_data(self, n: int):
        return self.level_data[n]


    def wall_1(self, x, speed):
        wall_data = {
            'width': 50,
            'height': 400,
            'vel': speed,
            'pos_x': x,
            'pos_y': SCREEN_HEIGHT - 400,
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
            num_y = random.randint(300, bottom - 400)

            projectile_spawn_cords = (num_x, num_y)

            cords.append(projectile_spawn_cords)

        for cord in cords:
            projectile = Projectile(cord[0], cord[1], speed)
            self.projectile_group.add(projectile)








