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
        self.WIDTH = column_data['width']
        self.HEIGHT = column_data['height']
        self.MASS = column_data['mass']
        self.SPRING_CONSTANT = column_data['spring_constant']
        self.FRICTION = column_data['friction']
        self.FORCE_UP = column_data['force_up']
        self.GRAVITY = column_data['gravity']

        # Column hitbox: eventually needs to be different shapes # TODO
        self.rect = pg.Rect(self.pos_x, self.pos_y, self.WIDTH, self.HEIGHT)

        # Column movement
        self.pos = vec(column_data['pos_x'], column_data['pos_y'])
        self.acc = vec(0, self.GRAVITY)
        self.vel = vec(0, 0)

        # Column States
        self.moving_up = False
        self.moving_down = False

    def accelerate(self):
        """ Gets called from the Game's event loop if we are pressing the control for this column """
        # Use force up to calc the net acceleration between the column and gravity
        # Set the acceleration to that

    def move(self):
        # Implement movemenet based on acceleration, velocity, and friction here #TODO



        if self.rect.top >= self.MAX_Y:
            self.pos.y = self.MAX_Y

    def update(self):
        self.move()
        # self.collisions()

    def draw(self, screen, show_hitboxes=True):
        # screen.blit(self.image, (self.pos_x, self.pos_y))
        if show_hitboxes:
            pg.draw.rect(screen, (255, 0, 0), self.rect)