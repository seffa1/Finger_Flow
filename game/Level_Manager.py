import pygame as pg
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, GRAVITIES, COLUMN_FORCE
from .Level import Level


# The level manager stores columns and ball data for each level, loads and swithces beteween levels
class Level_Manager:
    def __init__(self, screen, projectile_manager, particle_manager, music_manager):
        self.projectile_manager = projectile_manager
        self.particle_manager = particle_manager
        self.screen = screen
        self.music_manager = music_manager

        # Level manager events
        self.level_ended = pg.USEREVENT + 1
        self.level_ended_event = pg.event.Event(self.level_ended)
        self.game_complete = pg.USEREVENT + 2
        self.game_complete_event = pg.event.Event(self.game_complete)

        # A list of level objects
        self.levels = []
        self.level = 1
        self.TOTAL_LEVELS = 2

        # Level 1 gets instantiated initially
        L1 = Level(self.generate_level_1_column_data(), self.screen, self.level_1_ball_data(),
                   self.projectile_manager.get_level_data(1), self.particle_manager, self.music_manager, self)
        L1.add_background(pg.image.load('assets/images/background_1.jpg').convert_alpha())
        self.levels.append(L1)

    def clear_levels(self):
        self.levels = []
        self.level = 1

    def check_level_state(self):
        # If all the levels projectile are gone (made it to the left side of the screen)
        level = self.get_level()
        sprite_group = level.projectile_group
        ball_group = level.ball_group

        # Check if all the balls have been destroyed
        if len(ball_group.sprites()) == 0:
            # End the game
            pg.event.post(self.game_complete_event)

        # Group.sprites returns a list of contained sprites
        # If theres no more projectiles in the group
        if len(sprite_group.sprites()) == 0:
            # If theres no more levels after this
            if self.level == self.TOTAL_LEVELS:
                # End the game
                pg.event.post(self.game_complete_event)
            # There are more levels to go to
            else:
                # post the event for the event loop to detect
                pg.event.post(self.level_ended_event)

    def get_level(self):
        return self.levels[self.level - 1]

    def set_level(self, n):
        level = self.levels[n - 1]

    def next_level(self):
        # Before we change levels we need to store the previous level's ball data and transfer that to the next level
        if self.level == 1:
            # Level 2 Instantiation
            L2 = Level(self.generate_level_1_column_data(), self.screen, self.extract_ball_data(),
                       self.projectile_manager.get_level_data(2), self.particle_manager, self.music_manager, self)
            L2.add_background(pg.image.load('assets/images/background_1.jpg').convert_alpha())
            self.levels.append(L2)
            self.level += 1
            return

        elif self.level == 2:
            # Level 3 Instantiation
            L3 = Level(self.generate_level_1_column_data(), self.screen, self.extract_ball_data(),
                       self.projectile_manager.get_level_data(3), self.particle_manager, self.music_manager, self)
            L3.add_background(pg.image.load('assets/images/background_1.jpg').convert_alpha())
            self.levels.append(L3)
            self.level += 1
            return


    # Maybe all this data eventually gets moved to a JSON file #TODO
    def generate_level_1_column_data(self):
        # Level 1 Data: [{column1_data}, {column2_data}, {...}, {...}... {column10_data}]
        level1_column_data = []
        i = 0
        for column in range(1, 11):
            column = {
                'number': i + 1,
                'width': SCREEN_WIDTH / 10,
                'height': SCREEN_HEIGHT,
                'pos_x': (SCREEN_WIDTH / 10) * i,
                'pos_y': SCREEN_HEIGHT - 200,
                'mass': 100,
                'image': '',
                'sound_up': '',
                'sound_down': '',
                'spring_constant': 0,
                'friction': .8,
                'force_up': COLUMN_FORCE,
                'max_y': SCREEN_HEIGHT - 200,
                'gravity': GRAVITIES[1],
                'min_y': 600
            }
            level1_column_data.append(column)
            i += 1
        return level1_column_data

    # The initial balls at the start of the game
    def level_1_ball_data(self):
        balls = []

        ball_1_data = {
            'diameter': 20,
            'mass': 6,
            'friction': 0.5,
            'pos_x': 620,
            'pos_y': 6,
            'vel_x': 0,
            'vel_y': 0,
            'image': pg.image.load('assets/images/boulder.png').convert_alpha(),
            'gravity': GRAVITIES[2],
            'image_scale': (100, 100),
            'num': 1
        }

        ball_2_data = {
            'diameter': 20,
            'mass': 6,
            'friction': 0.5,
            'pos_x': 1005,
            'pos_y': 6,
            'vel_x': 0,
            'vel_y': 0,
            'image': pg.image.load('assets/images/boulder.png').convert_alpha(),
            'gravity': GRAVITIES[2],
            'image_scale': (100, 100),
            'num': 1
        }

        # Generate 10 balls
        for i in range(0, 2):
            ball = {
            'diameter': 20,
            'mass': 6,
            'friction': 0.5,
            'pos_x': SCREEN_WIDTH / 10 * (i),
            'pos_y': 6,
            'vel_x': 0,
            'vel_y': 0,
            'image': pg.image.load('assets/images/ball_D20.png').convert_alpha(),
            'gravity': GRAVITIES[2],
            'image_scale': (100, 100),
            'num': 1
        }

        balls.append(ball_1_data)
        balls.append(ball_2_data)
        return balls

    def extract_ball_data(self):
        # ball_data = [{ball1_data}, {ball2_data}, {ball3_data}]
        ball_data = []
        # Only check the balls left in the sprite group, as they get removed when a ball gets destroyed
        for ball in self.get_level().ball_group:
            ball_info = {
                'diameter': ball.DIAMETER,
                'mass': ball.MASS,
                'friction': ball.FRICTION,
                'pos_x': ball.pos.x,
                'pos_y': ball.pos.y,
                'vel_x': 0,
                'vel_y': 0,
                'image': ball.IMAGE,
                'gravity': ball.GRAVITY,
                'image_scale': (100, 100),
                'num': 1
            }
            ball_data.append(ball_info)
        return ball_data





