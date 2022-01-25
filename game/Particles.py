import pygame as pg
import random

vec = pg.math.Vector2


# Spawns multiple particles when they are needed
class Particle_Manager:
    def __init__(self, screen):
        self.particles = pg.sprite.Group()

    def emmit(self, ball_pos: vec, ball_vel: int):
        """ Generates particles based on ball info and adds them to a sprite group """
        qty = ball_vel * 3
        for i in range(0, qty):
            pos = ball_pos
            vel_x = random.randint(-1, 2)
            vel_y = random.randint(0, ball_vel)
            vel = vec(vel_x, vel_y)
            diameter = random.randint(8, 18)
            particle = Particle(pos, vel, diameter)
            self.particles.add(particle)

    def update_particles(self):
        for particle in self.particles:
            particle.update()

    def draw_particles(self):
        for particle in self.particles:
            particle.draw()


class Particle(pg.sprite.Sprite):
    def __init__(self, pos: vec, vel: vec, diameter: int):
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
        pg.draw.circle(screen, (255, 255, 255), self.pos, self.diameter)
