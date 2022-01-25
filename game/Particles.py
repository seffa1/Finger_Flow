import pygame as pg
import random
import math
vec = pg.math.Vector2


# Spawns multiple particles when they are needed
class Particle_Manager:
    def __init__(self, screen):
        self.particles = pg.sprite.Group()
        self.screen = screen

    def emmit(self, ball_pos: vec, ball_vel):
        """ Generates particles based on ball info and adds them to a sprite group """
        # ball_vel is from 0 to 22 on average
        scaler = int(round(ball_vel / 10))
        qty = scaler
        print(f'scaler: {scaler}, qty: {qty}')
        for i in range(0, 20):
            pos = (ball_pos.x + 50, ball_pos.y + 100)
            vel_x = random.randint(-4, 4)
            vel_y = random.randint(2, 4 + scaler) * -1
            vel = vec(vel_x, vel_y)
            diameter = random.randint(4, 4)
            particle = Particle(pos, vel, diameter)
            self.particles.add(particle)

    def update_particles(self):
        for particle in self.particles:
            particle.update()

    def draw_particles(self):
        for particle in self.particles:
            particle.draw(self.screen)


class Particle(pg.sprite.Sprite):
    def __init__(self, pos: vec, vel: vec, diameter: int):
        super().__init__()
        self.pos = vec(pos)
        self.vel = vec(vel)
        self.rect = pg.Rect(self.pos.x, self.pos.y, 3, 10)
        self.diameter = diameter
        self.GRAVITY = .2

        # Used to keep track of time
        self.delta_tick = 0
        # How many ticks until we change the diameter
        self.diameter_time = 60
        # How much the diameter will change
        self.diameter_delta = self.diameter - (self.diameter * .1)

    def update(self):
        self.vel.y += self.GRAVITY
        self.pos += self.vel

        self.delta_tick += 1
        if self.delta_tick % self.diameter_time == 0:
            self.diameter -= self.diameter_delta
            if self.diameter <= .1:
                self.kill()

    def draw(self, screen):
        pg.draw.circle(screen, (255, 255, 255), self.pos, self.diameter)
