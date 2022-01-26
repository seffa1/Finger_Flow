import pygame as pg
import sys
from .Level_Manager import Level_Manager
from .UserInterface import UserInterface
from .Projectile_Manager import Projectile_Manager
from .Particles import Particle_Manager
from .Music_Manager import Music_Manager

# IDEA:
# score per level = (level_number + collectibles) * balls left

class Game:
    def __init__(self, screen, clock):
        self.playing = False

        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()

        self.user_interface = UserInterface()
        self.projectile_manager = Projectile_Manager()
        self.particle_manager = Particle_Manager(screen)

        self.music_manager = Music_Manager()
        self.music_manager.load_music('background')
        self.level_manager = Level_Manager(screen, self.projectile_manager, self.particle_manager, self.music_manager)

    def run(self):
        self.playing = True

        # Game loop
        while self.playing:
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.USEREVENT + 3:
                self.user_interface.add_point(self.level_manager.get_level().ball_group)

            if event.type == self.level_manager.level_ended:
                print("LEVEL COMPLETE")
                self.level_manager.next_level()

            if event.type == self.level_manager.game_complete:
                # Eventually well queue a game over screen with our score #TODO
                print("GAME COMPLETED!")
                # For the remaining projectiles...
                for projectile in self.level_manager.get_level().projectile_group.sprites():
                    # stop them from moving, so the level never ends
                    projectile.vel.x = -0.05


            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
                # If you are pressing the control key and the level start animation is not playing
                # if event.key == pg.K_q and not self.level_manager.get_level().level_start:
                #     self.level_manager.get_level().get_column(1).accelerate()
                # if event.key == pg.K_w and not self.level_manager.get_level().level_start:
                #     self.level_manager.get_level().get_column(2).accelerate()
                # if event.key == pg.K_e and not self.level_manager.get_level().level_start:
                #     self.level_manager.get_level().get_column(3).accelerate()
                if event.key == pg.K_r and not self.level_manager.get_level().level_start:
                    self.level_manager.get_level().get_column(4).accelerate()
                # if event.key == pg.K_c and not self.level_manager.get_level().level_start:
                #     self.level_manager.get_level().get_column(5).accelerate()
                if event.key == pg.K_u and not self.level_manager.get_level().level_start:
                    self.level_manager.get_level().get_column(6).accelerate()
                # if event.key == pg.K_u and not self.level_manager.get_level().level_start:
                #     self.level_manager.get_level().get_column(7).accelerate()
                # if event.key == pg.K_i and not self.level_manager.get_level().level_start:
                #     self.level_manager.get_level().get_column(8).accelerate()
                # if event.key == pg.K_o and not self.level_manager.get_level().level_start:
                #     self.level_manager.get_level().get_column(9).accelerate()
                # if event.key == pg.K_p and not self.level_manager.get_level().level_start:
                #     self.level_manager.get_level().get_column(10).accelerate()

            if event.type == pg.KEYUP:
                if event.key == pg.K_q and not self.level_manager.get_level().level_start:
                    self.level_manager.get_level().get_column(1).deccelerate()
                if event.key == pg.K_w and not self.level_manager.get_level().level_start:
                    self.level_manager.get_level().get_column(2).deccelerate()
                if event.key == pg.K_e and not self.level_manager.get_level().level_start:
                    self.level_manager.get_level().get_column(3).deccelerate()
                if event.key == pg.K_r and not self.level_manager.get_level().level_start:
                    self.level_manager.get_level().get_column(4).deccelerate()
                if event.key == pg.K_c and not self.level_manager.get_level().level_start:
                    self.level_manager.get_level().get_column(5).deccelerate()
                if event.key == pg.K_u and not self.level_manager.get_level().level_start:
                    self.level_manager.get_level().get_column(6).deccelerate()
                if event.key == pg.K_u and not self.level_manager.get_level().level_start:
                    self.level_manager.get_level().get_column(7).deccelerate()
                if event.key == pg.K_i and not self.level_manager.get_level().level_start:
                    self.level_manager.get_level().get_column(8).deccelerate()
                if event.key == pg.K_o and not self.level_manager.get_level().level_start:
                    self.level_manager.get_level().get_column(9).deccelerate()
                if event.key == pg.K_p and not self.level_manager.get_level().level_start:
                    self.level_manager.get_level().get_column(10).deccelerate()

    def update(self):
        # Check if the level has ended
        self.level_manager.check_level_state()

        # Update the columns
        self.level_manager.get_level().update_columns()

        # Update the ball
        self.level_manager.get_level().update_balls()

        # Update the projectiles
        self.level_manager.get_level().update_projectiles()

        # Update the particles
        self.particle_manager.update_particles()

        # Update the UI
        self.user_interface.update(self.clock.get_fps(),
                                   self.level_manager.get_level().ball_group,
                                   self.level_manager.get_level().columns
                                   )

    def draw(self):
        # Draw the background, if you dont do this each frame the images you draw
        # to the screen will stack up as copies over one another
        self.screen.fill((0, 0, 0))

        # Draw the background
        self.level_manager.get_level().draw_background()

        # Draw the columns
        self.level_manager.get_level().draw_columns()

        # Draw the projectiles
        self.level_manager.get_level().draw_projectiles()

        # Draw the balls
        self.level_manager.get_level().draw_balls()

        # Draw the particles
        self.particle_manager.draw_particles()

        # Draw the interface
        self.user_interface.draw(self.screen)

        # Updates the entire display at once
        # This is no different than display.update() with no arguments passed in
        pg.display.flip()