import pygame as pg


vec = pg.math.Vector2

class Column(pg.sprite.Sprite):
    def __init__(self, column_data):
        super().__init__()

        # Level data
        self.number = column_data['number']
        # self.image = pg.image.load(column_data['image']).convert_alpha() # TODO
        # self.sound_up = column_data['sound_up'] # TODO
        # self.sound_down = column_data['sound_down'] # TODO

        # Column Constants
        self.MAX_Y = column_data['max_y']
        self.MIN_Y = column_data['min_y']
        self.WIDTH = column_data['width']
        self.HEIGHT = column_data['height']
        self.MASS = column_data['mass']
        self.SPRING_CONSTANT = column_data['spring_constant']
        self.FRICTION = column_data['friction']
        self.FORCE_UP = column_data['force_up']
        self.GRAVITY = column_data['gravity']

        # Column movement
        self.pos = vec(column_data['pos_x'], column_data['pos_y'])
        self.acc = vec(0, self.GRAVITY)
        self.vel = vec(0, 0)

        # Column hitbox: eventually needs to be different shapes # TODO
        self.rect = pg.Rect(self.pos.x, self.pos.y, self.WIDTH, self.HEIGHT)

        # Column States
        self.at_top = False
        self.at_bottom = False

    def accelerate(self):
        """ Gets called from the Game's event loop if we are pressing the control for this column """
        # Use force up to calc the net acceleration between the column and gravity
        # Set the acceleration to that
        # FORCE_UP = -int,     MASS = +ing,      acceleration = -int,     Gravity = +int
        # acceleration_up = self.FORCE_UP / self.MASS
        # self.acc.y += acceleration_up
        if not self.at_top:
            self.acc.y = -1.2

    def deccelerate(self):
        if self.at_top:
            self.vel.y = .1
        self.acc = vec(0, self.GRAVITY)

    def move(self):
        # Implement movement based on acceleration, velocity, and friction here #TODO
        self.vel.y += self.acc.y
        self.pos.y += self.vel.y

        # Controls the columns when at bottom
        # At bottom
        if self.pos.y >= self.MAX_Y:
            self.pos.y = self.MAX_Y
            self.at_bottom = True
            self.vel.y = 0
        else:
            self.at_bottom = False

        # Controls the columns when at top
        # At top
        if self.pos.y <= self.MIN_Y:
            self.pos.y = self.MIN_Y
            self.vel.y = 0
            self.at_top = True
        else:
            # print('should not be at top')
            self.at_top = False


        self.rect.topleft = self.pos

    def update(self):
        self.move()
        # self.collisions()

    def draw(self, screen, show_hitboxes=True):
        # screen.blit(self.image, (self.pos_x, self.pos_y))
        if show_hitboxes:
            pg.draw.rect(screen, (255, 0, 0), self.rect)