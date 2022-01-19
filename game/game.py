import pygame as pg
import sys
from .Level_Manager import Level_Manager
from .UserInterface import UserInterface


class Game:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()
        self.level_manager = Level_Manager(screen)
        self.user_interface = UserInterface()


    def run(self):
        self.playing = True
        # load level 1

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
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
                if event.key == pg.K_q:
                    self.level_manager.get_level().get_column(1).accelerate()
                if event.key == pg.K_w:
                    self.level_manager.get_level().get_column(2).accelerate()
                if event.key == pg.K_e:
                    self.level_manager.get_level().get_column(3).accelerate()
                if event.key == pg.K_r:
                    self.level_manager.get_level().get_column(4).accelerate()
                if event.key == pg.K_c:
                    self.level_manager.get_level().get_column(5).accelerate()
                if event.key == pg.K_n:
                    self.level_manager.get_level().get_column(6).accelerate()
                if event.key == pg.K_u:
                    self.level_manager.get_level().get_column(7).accelerate()
                if event.key == pg.K_i:
                    self.level_manager.get_level().get_column(8).accelerate()
                if event.key == pg.K_o:
                    self.level_manager.get_level().get_column(9).accelerate()
                if event.key == pg.K_p:
                    self.level_manager.get_level().get_column(10).accelerate()

            if event.type == pg.KEYUP:
                if event.key == pg.K_q:
                    self.level_manager.get_level().get_column(1).deccelerate()
                if event.key == pg.K_w:
                    self.level_manager.get_level().get_column(2).deccelerate()
                if event.key == pg.K_e:
                    self.level_manager.get_level().get_column(3).deccelerate()
                if event.key == pg.K_r:
                    self.level_manager.get_level().get_column(4).deccelerate()
                if event.key == pg.K_c:
                    self.level_manager.get_level().get_column(5).deccelerate()
                if event.key == pg.K_n:
                    self.level_manager.get_level().get_column(6).deccelerate()
                if event.key == pg.K_u:
                    self.level_manager.get_level().get_column(7).deccelerate()
                if event.key == pg.K_i:
                    self.level_manager.get_level().get_column(8).deccelerate()
                if event.key == pg.K_o:
                    self.level_manager.get_level().get_column(9).deccelerate()
                if event.key == pg.K_p:
                    self.level_manager.get_level().get_column(10).deccelerate()


    def update(self):
        # Update the columns
        self.level_manager.get_level().update_columns()

        # Update the ball
        # Ball.update() #TODO

        # Update the UI
        self.user_interface.update(self.clock.get_fps())

    def draw(self):
        # Draw the background
        self.screen.fill((0, 0, 0))

        # Draw the columns
        self.level_manager.get_level().draw_columns()

        # Draw the interface
        self.user_interface.draw(self.screen)

        pg.display.flip()