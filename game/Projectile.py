import pygame as pg


vec = pg.math.Vector2

class Projectile(pg.sprite.Sprite):
    def __init__(self, projectile_data):
        super().__init__()

        self.IMAGE = projectile_data['image']
        self.pos = vec(projectile_data['pos_x'], projectile_data['pos_y'])
        self.vel = vec(projectile_data['speed'], 0)
        self.number = projectile_data['num']

        self.rect = self.IMAGE.get_rect()

    def update(self):
        self.pos.x += self.vel.x
        self.rect.topleft = self.pos

    def draw(self, screen, show_hitboxes=True):
        if show_hitboxes:
            pg.draw.rect(screen, (0, 255, 255), self.rect)

        screen.blit(self.IMAGE, (self.pos.x, self.pos.y))


