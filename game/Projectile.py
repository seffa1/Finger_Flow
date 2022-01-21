import pygame as pg


vec = pg.math.Vector2

class Projectile(pg.sprite.Sprite):
    def __init__(self, projectile_data):
        super().__init__()

        self.image = projectile_data['image']
        self.pos = vec(projectile_data['pos_x'], projectile_data['pos_y'])
        self.vel = vec(projectile_data['speed'], 0)

        self.rect = self.image.get_rect()

    def update(self):


