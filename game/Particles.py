import pygame as pg

vec = pg.math.Vector2


# Spawns multiple particles when they are needed
class Particle_Manager:
    def __init__(self, screen):
        self.particles = pg.sprite.Group()


class Particle(pg.sprite.Sprite):
    def __init__(self, pos, vel, diameter):
        self.pos = vec(pos)
        self.vel = vec(vel)
        self.rect = pg.Rect(self.pos.x, self.pos.y, 3, 10)
        self.diameter = diameter
        self.GRAVITY = 1

        # Used to keep track of time
        self.delta_tick = 0
        self.diameter_time = 20
        self.diameter_delta = self.diameter / 10

    def update(self):
        self.vel.y += self.GRAVITY
        self.pos += self.vel

        self.delta_tick += 1
        if self.delta_tick % self.diameter_time == 0:
            self.diameter -= self.diameter_delta
            if self.diameter <= 1:
                self.kill()

    def draw(self, screen):
        pass
