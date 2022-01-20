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
        # Returns a list of columns the ball is colliding with
        collisions = pg.sprite.spritecollide(self, column_group, False)

        self.acc = vec(0, self.GRAVITY)
        self.vel += self.acc

        # Move the ball in the x direction
        self.pos.x += self.vel.x

        # Check for collisions in x direction
        for column in collisions:

            # If a column collides and is to the left
            if column.pos.x <= self.pos.x:

                # Set the balls left to equal the column's right
                self.pos.x = column.pos.x + column.WIDTH

        # Move the ball in the y direction
        self.pos.y += self.vel.y

        # Check for collisions
        for column in collisions:

            # If the column collides and is below the ball
            if column.pos.y >= self.pos.y:

                # Set the balls bottom to equal the columns top
                self.pos.y = column.pos.y


        # Move the rect with the image
        self.rect.topleft = self.pos

    def update(self, column_group):
        self.move(column_group)


    def draw(self, screen, show_hitboxes=True):
        if show_hitboxes:
            pg.draw.rect(screen, (0, 255, 0), self.rect)

        screen.blit(self.IMAGE, (self.pos.x, self.pos.y))



