import pygame as pg
from .Column import Column


class Level:
    def __init__(self, level_data, screen):
        self.screen = screen
        self.level_data = level_data
        # Dictionary of column objects. {1: column1, 2: column2}
        self.columns = {}
        self.column_group = pg.sprite.Group()
        self._create_columns(self.level_data)

    def _create_columns(self, level_data):
        """ Creates column objects from column information passed in """
        # Level data is a list of dictionaries for each column [{}, {}, {}, {}... {}]
        for column_data in level_data:
            column = Column(column_data)
            self.columns[column.number] = column
            self.column_group.add(column)

    def get_column(self, n: int):
        return self.columns[n]

    def add_background(self, image):
        # TODO
        pass

    def update_columns(self):
        for column in self.columns.values():
            column.update()


    def draw_columns(self):
        for column in self.columns.values():
            column.draw(self.screen)