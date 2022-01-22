import pygame as pg


vec = pg.math.Vector2

class Projectile(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y, speed):
        super().__init__()

        self.IMAGE = pg.image.load('assets/images/ball_D20.png').convert_alpha()
        self.pos = vec(pos_x, pos_y)
        self.vel = vec(speed, 0)

        self.rect = self.IMAGE.get_rect()

    def update(self):
        self.pos.x += self.vel.x
        self.rect.topleft = self.pos

    def draw(self, screen, show_hitboxes=True):
        if show_hitboxes:
            pg.draw.rect(screen, (0, 255, 255), self.rect)

        screen.blit(self.IMAGE, (self.pos.x, self.pos.y))


