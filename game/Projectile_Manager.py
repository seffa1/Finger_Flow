import pygame as pg
import random
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from .Projectile import Projectile


# Creates random projectiles
class Projectile_Manager:
    def __init__(self, screen):
        self.projectiles = []
        self.projectile_group = pg.sprite.Group()
        self.start_level_1()
        self.screen = screen

    def start_level_1(self):
        self._gen_projectiles(5, -3)

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

    def update_projectile(self):
        for projectile in self.projectile_group:
            projectile.update()

    def draw_projectiles(self):
        for projectile in self.projectile_group:
            projectile.draw(self.screen)






