import pygame as pg


vec = pg.math.Vector2

class Projectile(pg.sprite.Sprite):
    def __init__(self, projectile_data):
        super().__init__()
        self.WIDTH = projectile_data['width']
        self.HEIGHT = projectile_data['height']
        self.pos = vec(projectile_data['pos_x'], projectile_data['pos_y'])
        self.vel = vec(projectile_data['vel'], 0)

        self.rect = pg.Rect(self.pos.x, self.pos.y, self.WIDTH, self.HEIGHT)

    def update(self, ball_group):
        self.pos.x += self.vel.x
        self.rect.topleft = self.pos

    def draw(self, screen, show_hitboxes=True):
        if show_hitboxes:
            pg.draw.rect(screen, (0, 255, 255), self.rect)

        # screen.blit(self.IMAGE, (self.pos.x, self.pos.y))


