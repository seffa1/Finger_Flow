import pygame as pg
import sys
from .Level_Manager import Level_Manager


class Game:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()
        self.level_manager = Level_Manager(screen)


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

    def update(self):
        # Update the columns
        self.level_manager.get_level().update_columns()

        # Update the ball
        # Ball.update() #TODO

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.level_manager.get_level().draw_columns()

        pg.display.flip()