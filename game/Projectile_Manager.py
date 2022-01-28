import pygame as pg
import random
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, LEVEL_SPEEDS
from .Projectile import Projectile


# Stores information for the projectiles to be passed into the level classes
class Projectile_Manager:
    def __init__(self):
        self.level_data = {
            1: self.level_1_data(),
            2: self.level_2_data(),
            3: self.level_3_data(),
            4: self.level_4_data()
        }

    def get_level_data(self, n: int):
        return self.level_data[n]

    def level_1_data(self):
        level_data = []
        speed_ = LEVEL_SPEEDS[1]
        level_data.append(self.low_wall(x=SCREEN_WIDTH + 500, height=700, speed=speed_))
        level_data.append(self.high_wall(x=SCREEN_WIDTH + 900, height=400, speed=speed_))
        level_data.append(self.low_wall(x=SCREEN_WIDTH + 1300, height=700, speed=speed_))
        level_data.append(self.high_wall(x=SCREEN_WIDTH + 1700, height=400, speed=speed_))
        level_data.append(self.low_wall(x=SCREEN_WIDTH + 2100, height=700, speed=speed_))
        return level_data

    def level_2_data(self):
        level_data = []
        speed_ = LEVEL_SPEEDS[2]
        # Low walls
        level_data.append(self.low_wall(x=SCREEN_WIDTH + 1000, height=500, speed=speed_))
        level_data.append(self.low_wall(x=SCREEN_WIDTH + 1800, height=400, speed=speed_))
        level_data.append(self.low_wall(x=SCREEN_WIDTH + 2600, height=250, speed=speed_))
        level_data.append(self.low_wall(x=SCREEN_WIDTH + 3400, height=400, speed=speed_))
        level_data.append(self.low_wall(x=SCREEN_WIDTH + 4200, height=500, speed=speed_))

        # High walls
        level_data.append(self.high_wall(x=SCREEN_WIDTH + 1000, height=150, speed=speed_))
        level_data.append(self.high_wall(x=SCREEN_WIDTH + 1800, height=300, speed=speed_))
        level_data.append(self.high_wall(x=SCREEN_WIDTH + 2600, height=450, speed=speed_))
        level_data.append(self.high_wall(x=SCREEN_WIDTH + 3400, height=300, speed=speed_))
        level_data.append(self.high_wall(x=SCREEN_WIDTH + 4200, height=150, speed=speed_))
        return level_data

    def level_3_data(self):
        level_data = []
        speed_ = LEVEL_SPEEDS[2]
        # Low walls
        level_data.append(self.low_wall(x=SCREEN_WIDTH + 1000, height=650, speed=speed_))
        level_data.append(self.low_wall(x=SCREEN_WIDTH + 1800, height=250, speed=speed_))
        level_data.append(self.low_wall(x=SCREEN_WIDTH + 2600, height=650, speed=speed_))
        level_data.append(self.low_wall(x=SCREEN_WIDTH + 3400, height=250, speed=speed_))
        level_data.append(self.low_wall(x=SCREEN_WIDTH + 4200, height=650, speed=speed_))
        level_data.append(self.low_wall(x=SCREEN_WIDTH + 5000, height=250, speed=speed_))

        # High walls
        level_data.append(self.high_wall(x=SCREEN_WIDTH + 1000, height=150, speed=speed_))
        level_data.append(self.high_wall(x=SCREEN_WIDTH + 1800, height=450, speed=speed_))
        level_data.append(self.high_wall(x=SCREEN_WIDTH + 2600, height=150, speed=speed_))
        level_data.append(self.high_wall(x=SCREEN_WIDTH + 3400, height=450, speed=speed_))
        level_data.append(self.high_wall(x=SCREEN_WIDTH + 4200, height=150, speed=speed_))
        level_data.append(self.high_wall(x=SCREEN_WIDTH + 5000, height=450, speed=speed_))
        return level_data

    def level_4_data(self):
        level_data = []
        speed_ = LEVEL_SPEEDS[2]
        low_height1 = 250
        low_height2 = 350
        low_height3 = 500
        low_height4 = 650
        high_height1 = 600
        high_height2 = 450
        high_height3 = 300
        high_height4 = 150
        # Low walls
        level_data.append(self.low_wall(x=SCREEN_WIDTH + 1000, height=low_height1, speed=speed_))
        level_data.append(self.low_wall(x=SCREEN_WIDTH + 1800, height=low_height4, speed=speed_))
        level_data.append(self.low_wall(x=SCREEN_WIDTH + 2600, height=low_height1, speed=speed_))
        level_data.append(self.low_wall(x=SCREEN_WIDTH + 3400, height=low_height2, speed=speed_))
        level_data.append(self.low_wall(x=SCREEN_WIDTH + 4200, height=low_height1, speed=speed_))
        level_data.append(self.low_wall(x=SCREEN_WIDTH + 5000, height=low_height3, speed=speed_))
        level_data.append(self.low_wall(x=SCREEN_WIDTH + 5800, height=low_height1, speed=speed_))
        level_data.append(self.low_wall(x=SCREEN_WIDTH + 6600, height=low_height4, speed=speed_))
        level_data.append(self.low_wall(x=SCREEN_WIDTH + 7400, height=low_height3, speed=speed_))
        level_data.append(self.low_wall(x=SCREEN_WIDTH + 8200, height=low_height2, speed=speed_))
        level_data.append(self.low_wall(x=SCREEN_WIDTH + 9000, height=low_height1, speed=speed_))
        level_data.append(self.low_wall(x=SCREEN_WIDTH + 9800, height=low_height4, speed=speed_))

        # High walls
        level_data.append(self.high_wall(x=SCREEN_WIDTH + 1000, height=high_height1, speed=speed_))
        level_data.append(self.high_wall(x=SCREEN_WIDTH + 1800, height=high_height4, speed=speed_))
        level_data.append(self.high_wall(x=SCREEN_WIDTH + 2600, height=high_height1, speed=speed_))
        level_data.append(self.high_wall(x=SCREEN_WIDTH + 3400, height=high_height2, speed=speed_))
        level_data.append(self.high_wall(x=SCREEN_WIDTH + 4200, height=high_height1, speed=speed_))
        level_data.append(self.high_wall(x=SCREEN_WIDTH + 5000, height=high_height3, speed=speed_))
        level_data.append(self.high_wall(x=SCREEN_WIDTH + 5800, height=high_height1, speed=speed_))
        level_data.append(self.high_wall(x=SCREEN_WIDTH + 6600, height=high_height4, speed=speed_))
        level_data.append(self.high_wall(x=SCREEN_WIDTH + 7400, height=high_height3, speed=speed_))
        level_data.append(self.high_wall(x=SCREEN_WIDTH + 8200, height=high_height2, speed=speed_))
        level_data.append(self.high_wall(x=SCREEN_WIDTH + 9000, height=high_height1, speed=speed_))
        level_data.append(self.high_wall(x=SCREEN_WIDTH + 9800, height=high_height4, speed=speed_))
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








