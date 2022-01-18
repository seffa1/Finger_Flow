import pygame as pg


class Column(pg.sprite.Sprite):
    def __init__(self, column_data):
        super().__init__()
        self.number = column_data['number']
        self.width = column_data['width']
        self.height = column_data['height']
        self.pos_x = column_data['pos_x']
        self.pos_y = column_data['pos_y']
        self.mass = column_data['mass']
        # self.image = pg.image.load(column_data['image']).convert_alpha()
        # self.sound_up = column_data['sound_up']
        # self.sound_down = column_data['sound_down']
        self.spring_constant = column_data['spring_constant']


        self.rect = pg.Rect(self.pos_x, self.pos_y, self.width, self.height)

    def move(self):
        pass

    def update(self):
        pass

    def draw(self, screen, show_hitboxes=True):
        # screen.blit(self.image, (self.pos_x, self.pos_y))
        if show_hitboxes:
            pg.draw.rect(screen, (255, 0, 0), self.rect)
