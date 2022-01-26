import random
import pygame as pg
vec = pg.math.Vector2


class Ball(pg.sprite.Sprite):
    def __init__(self, ball_data, music_manager, level_manager):
        super().__init__()



        # Info for rotational physics
        # https://www.khanacademy.org/science/physics/torque-angular-momentum/torque-tutorial/v/rotational-kinetic-energy

        # Ball constants
        self.IMAGE = pg.transform.scale(ball_data['image'], ball_data['image_scale'])
        self.DIAMETER = ball_data['diameter']
        self.MASS = ball_data['mass']
        self.FRICTION = ball_data['friction']
        self.GRAVITY = ball_data['gravity']
        self.NUM = ball_data['num']
        self.music_manager = music_manager
        self.level_manager = level_manager


        # Moment of intertia for a sphere
        self.MOMENT_OF_INERTIA = (2/5) * self.MASS * ((self.DIAMETER/2) ** 2)

        # Ball info
        self.pos = vec(ball_data['pos_x'], ball_data['pos_y'])
        self.vel = vec(ball_data['vel_x'], ball_data['vel_y'])
        self.acc = vec(0, self.GRAVITY)
        self.collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False, 'moving_up': False}
        self.collisions = None

        # Rect
        self.rect = self.IMAGE.get_rect()
        self.rect.center = self.pos

    # def apply_force(self, magnitude, )

    def move(self, column_group, projectile_group, max_y):
        """ Move calculates the intended velocity of the ball and moves the ball in the x-direction, checks for collisions
        and updates the x-velocity and position. Then it moves the ball in the y-direction, checks for collisions in the y
        direction, and updates the y position and velocity accordingly. The rect is moved with the ball position each time."""

        # Move the ball and rect in the x direction
        # We are no longer moving the ball in the x direction, ever !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # self.pos.x += self.vel.x
        # self.rect.topleft = self.pos

        # Check for collisions in x direction
        # Returns a list of columns the ball is colliding with
        # self.collisions = pg.sprite.spritecollide(self, column_group, False)
        # for column in self.collisions:
        #     # If ball is moving right and collided
        #     if self.vel.x > 0:
        #         # Set right side of ball to left side of column
        #         self.pos.x = column.rect.left - self.IMAGE.get_width()
        #         # Equal and opposite vel to bounce the ball
        #         # self.vel.x = self.vel.x * -1 * self.FRICTION
        #         self.vel.x = 0
        #         self.collision_types['right'] = True
        #         # Move the rect with the ball image
        #         self.rect.topleft = self.pos
        #     # If ball is moving left and collided
        #     elif self.vel.x < 0:
        #         # Set left side of ball to right side of column
        #         self.pos.x = column.rect.right
        #         # Equal and opposite vel to bounce the ball
        #         # self.vel.x = self.vel.x * -1 * self.FRICTION
        #         self.vel.x = 0
        #         # Move the rect with the ball image
        #         self.rect.topleft = self.pos
        #         self.collision_types['left'] = True


        # Move the ball and rect in the y direction
        self.vel.y += self.acc.y
        self.pos.y += self.vel.y
        self.rect.topleft = self.pos

        # Check for collisions with the columns
        self.collisions = pg.sprite.spritecollide(self, column_group, False)

        # If not collisions, update the collision types for the particle checking
        if len(self.collisions) == 0:
            # If the ball is not at the columns ground level
            if self.pos.y + self.IMAGE.get_height() < max_y:
                # print("no collisions")
                self.collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False, 'moving_up': False}
            else:
                # print("collisions happening")
                self.collision_types = {'top': False, 'bottom': True, 'right': False, 'left': False, 'moving_up': False}

        for column in self.collisions:
            # If ball is falling down or not moving and is collided
            if self.vel.y >= 0:
                # Check if the column is moving upwards
                if column.vel.y < 0:
                    # if so, add the column's acc to the ball's velocity
                    self.vel.y = column.vel.y
                    # Set bottom of ball to top of column
                    # self.pos.y = column.rect.top - self.IMAGE.get_height()
                    # Move the rect with the ball image
                    self.rect.topleft = self.pos

                else:
                    # If the column is not moving upwards, set the balls y vel to 0.
                    # Eventually this will be an elastic collisions to make the ball bounce
                    self.vel.y = 0
                    # Set bottom of ball to top of column
                    self.pos.y = column.rect.top - self.IMAGE.get_height()
                    # Move the rect with the ball image
                    self.rect.topleft = self.pos

            # The ball is moving upward with the column colliding beneath it
            else:
                # If the column is not at the min_y since its vel.y gets set to 0
                if column.pos.y != column.MIN_Y:
                    # Then the balls vel.y equals the column
                    self.vel.y = column.vel.y
                    # Set bottom of ball to top of column
                    self.pos.y = column.rect.top - self.IMAGE.get_height()
                    # Move the rect with the ball image
                    self.rect.topleft = self.pos

            # # If ball is moving up and collided
            # We don't check if the ball collided with the column above because
            # It will never happen

        # Check for collisions with the projectiles
        # Returns a list of collided projectile
        projectile_collisions = pg.sprite.spritecollide(self, projectile_group, False)
        if len(projectile_collisions) > 0:
            self.kill()
            # Play one of two sounds
            num = random.randint(1, 2)
            if num == 1:
                self.music_manager.load_sound('rock_pour1', .7)
            else:
                self.music_manager.load_sound('rock_pour2', .7)

            self.level_manager.particle_manager.emmit(self.pos, 37)

        # Move the rect with the image
        self.rect.topleft = self.pos


    def update(self, column_group, projectile_group, max_y):
        self.move(column_group, projectile_group, max_y)


    def draw(self, screen, show_hitboxes=False):
        if show_hitboxes:
            pg.draw.rect(screen, (0, 255, 0), self.rect)

        screen.blit(self.IMAGE, (self.pos.x, self.pos.y))



