import pygame as pg


vec = pg.math.Vector2

class Projectile(pg.sprite.Sprite):
    def __init__(self, projectile_data):
        super().__init__()
        self.WIDTH = projectile_data['width']
        self.HEIGHT = projectile_data['height']
        self.pos = vec(projectile_data['pos_x'], projectile_data['pos_y'])
        self.vel = vec(projectile_data['vel'], 0)

        self.color = (0, 0, 0)
        self.collisions = None
        self.collided = False

        self.rect = pg.Rect(self.pos.x, self.pos.y, self.WIDTH, self.HEIGHT)

    def update(self, ball_group):
        self.pos.x += self.vel.x
        self.rect.topleft = self.pos

        self.collisions = pg.sprite.spritecollide(self, ball_group, False)
        if len(self.collisions) > 0:
            self.collided = True
        else:
            self.collided = False

        # If the column makes it to the left side of the screen
        # Remove it
        if self.pos.x < 0 - self.WIDTH - 10:
            self.kill()


    def draw(self, screen, show_hitboxes=True):
        if show_hitboxes:
            if self.collided:
                pg.draw.rect(screen, (0, 255, 0), self.rect)
            else:
                pg.draw.rect(screen, (255, 0, 255), self.rect)

        # screen.blit(self.IMAGE, (self.pos.x, self.pos.y))


