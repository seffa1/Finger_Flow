import pygame as pg

vec = pg.math.Vector2

class Ball(pg.sprite.Sprite):
    def __init__(self, ball_data):
        super().__init__()

        # Info for rotational physics
        # https://www.khanacademy.org/science/physics/torque-angular-momentum/torque-tutorial/v/rotational-kinetic-energy

        # Ball constants
        self.IMAGE = pg.transform.scale(ball_data['image'], ball_data['image_scale'])
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

    # def apply_force(self, magnitude, )

    def move(self, column_group):
        # Calc the movement
        self.acc = vec(0, self.GRAVITY)
        self.vel += self.acc

        # Track the collisions types
        collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}

        # Move the ball in the x direction
        self.pos.x += self.vel.x

        # Check for collisions in x direction
        # Returns a list of columns the ball is colliding with
        collisions = pg.sprite.spritecollide(self, column_group, False)
        for column in collisions:
            # If ball is moving right and collided
            if self.vel.x > 0:
                # Set right side of ball to left side of column
                self.pos.x = column.rect.left - self.IMAGE.get_width()
                self.vel.x = 0
                collision_types['right'] = True
            # If ball is moving left and collided
            elif self.vel.x < 0:
                # Set left side of ball to right side of column
                self.pos.x = column.rect.right
                self.vel.x = 0
                collision_types['left']= True

        # Move the ball in the y direction
        self.pos.y += self.vel.y

        # Check for collisions
        collisions = pg.sprite.spritecollide(self, column_group, False)
        for column in collisions:
            # If ball is falling down and collided
            if self.vel.y > 0:
                # Set bottom of ball to top of column
                self.pos.y = column.rect.top - self.IMAGE.get_height()
                self.vel.y = 0
                collision_types['bottom'] = True
            # If ball is moving up and collided
            elif self.vel.y < 0:
                # Set top of ball to bottom of column
                self.pos.y = column.rect.bottom
                self.vel.y = 0
                collision_types['top'] = True

        # Move the rect with the image
        self.rect.topleft = self.pos
        print(self.pos.y)

    def update(self, column_group):
        self.move(column_group)


    def draw(self, screen, show_hitboxes=True):
        if show_hitboxes:
            pg.draw.rect(screen, (0, 255, 0), self.rect)

        screen.blit(self.IMAGE, (self.pos.x, self.pos.y))



