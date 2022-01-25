import pygame as pg


class Music_Manager:
    def __init__(self):
        self.sounds = {}
        self.music = {}
        self.create_sounds()

    def create_sounds(self):
        self.music['background'] = 'assets/sounds/water_ambiance.wav'
        self.sounds['rock_pour1'] = 'assets/sounds/BRS_Dust_Fall_Rocks_Gritty_Med.wav'
        self.sounds['rock_pour2'] = 'assets/sounds/BRS_Dust_Fall_Rocks_Sandy_2.wav'
        self.sounds['rock_hit1'] = 'assets/sounds/LL_Foley_Rock_1.wav'
        self.sounds['rock_hit2'] = 'assets/sounds/LL_Foley_Rock_2.wav'
        self.sounds['rock_hit3'] = 'assets/sounds/OS_AET_Rocks_Pinecones_5.wav'
        self.sounds['rock_hit4'] = 'assets/sounds/OS_BBL_Rock_Hit_4.wav'
        self.sounds['rock_hit5'] = 'assets/sounds/RockDropSmall_S08FO.2166.wav'

    def load_sound(self, name, volume):
        sound_effect = pg.mixer.Sound(self.sounds[name])
        sound_effect.set_volume(volume)
        sound_effect.play()
        # Only one music track can be playing at a time
        # Volume ranges from 0 to 1. Use decimal values

    def load_music(self, name, volume=1, num=-1):
        pg.mixer.music.set_volume(volume)
        pg.mixer.music.load(self.music[name])
        # num determines how long the music plays, -1 means the music will loop indefinetly
        # 0 = play once, 1 = plays twice, ...
        pg.mixer.music.play(num)

    def stop(self):
        pg.mixer.music.stop()
