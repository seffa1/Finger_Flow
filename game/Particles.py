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
        # print(f'scaler: {scaler}, qty: {qty}')
        for i in range(0, 10 + 10 * scaler):
            pos = (ball_pos.x + 50, ball_pos.y + 100)
            vel_x = random.randint(-4, 4)
            vel_y = random.randint(2, 6) * -1 + scaler * -1
            vel = vec(vel_x, vel_y)
            diameter = random.randint(3, 4)
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
        self.GRAVITY = random.randint(15, 25) / 100

        # Used to keep track of time
        self.delta_tick = 0
        # How many ticks until we change the diameter
        self.diameter_time = 30
        # How much the diameter will change
        self.diameter_delta = 1

    def update(self):
        self.vel.y += self.GRAVITY
        self.pos += self.vel

        self.delta_tick += 1
        if self.delta_tick % self.diameter_time == 0:
            self.diameter -= self.diameter_delta
            if self.delta_tick > 120 * (random.randint(5, 90) / 10) + self.vel.y * 3:
                self.kill()

    def draw(self, screen):
        pg.draw.circle(screen, (124, 112, 112), self.pos, self.diameter)
