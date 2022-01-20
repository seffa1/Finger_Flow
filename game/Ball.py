import pygame as pg

vec = pg.math.Vector2

class Ball(pg.sprite.Sprite):
    def __init__(self, ball_data):
        super().__init__()

        # Info for rotational physics
        # https://www.khanacademy.org/science/physics/torque-angular-momentum/torque-tutorial/v/rotational-kinetic-energy

        # Ball constants
        self.IMAGE = ball_data['image']
        self.DIAMETER = ball_data['diameter']
        self.MASS = ball_data['mass']
        self.FRICTION = ball_data['friction']
        self.GRAVITY = ball_data['gravity']

        # Moment of intertia for a sphere
        self.MOMENT_OF_INERTIA = (2/5) * self.MASS * ((self.DIAMETER/2) ** 2)

        # Ball info
        self.pos = vec(ball_data['pos_x'], ball_data['pos_y'])
        self.vel = vec(ball_data['vel_x'], ball_data['vel_y'])
        self.acc = vec(0 , self.GRAVITY)

        # Rect
        self.rect = self.IMAGE.get_rect()
        self.rect.center = self.pos

    def update(self):
        self.acc = vec(0 , self.GRAVITY)
        self.vel += self.acc

        # Move the ball in the x direction
        self.pos.x += self.vel.x

        # Check for collisions # TODO

        # Move the ball in the y direction
        self.pos.y += self.vel.y
        # Check for collisions

        # Move the rect with the image
        self.rect.topleft = self.pos

    def draw(self, screen, show_hitboxes=True):
        if show_hitboxes:
            pg.draw.rect(screen, (0, 255, 0), self.rect)

        screen.blit(self.IMAGE, (self.pos.x, self.pos.y))



