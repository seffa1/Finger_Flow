import pygame as pg


class Music_Manager:
    def __init__(self):
        self.sounds = {}
        self.create_sounds()

    def create_sounds(self):
        self.sounds['background'] = 'assets/sounds/water_ambiance.wav'

    def load_sound(self, name, volume):
        sound_effect = pg.mixer.Sound(self.sounds[name])
        sound_effect.set_volume(volume)
        sound_effect.play()

        # Only one music track can be playing at a time
        # Volume ranges from 0 to 1. Use decimal values

    def load_music(self, name, volume=1, num=-1):
        pg.mixer.music.set_volume(volume)
        pg.mixer.music.load(self.sounds[name])
        # num determines how long the music plays, -1 means the music will loop indefinetly
        # 0 = play once, 1 = plays twice, ...
        pg.mixer.music.play(num)

    def stop(self):
        pg.mixer.music.stop()
