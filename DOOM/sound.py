import pygame as pg

class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'DOOM/resources/Sounds/'
        self.shotgun = pg.mixer.Sound(self.path + 'shotgun.wav')
        self.npc_pain= pg.mixer.Sound(self.path + 'npc_pain.wav')
        self.npc_death = pg.mixer.Sound(self.path + 'npc_death.wav')
        self.npc_attack = pg.mixer.Sound(self.path + 'npc_attack.wav')
        self.player_pain = pg.mixer.Sound(self.path + 'player_pain.wav')
        self.theme = pg.mixer.Sound(self.path + 'theme.mp3')
        self.theme = pg.mixer.music.load(self.path + 'theme.mp3')
        pg.mixer.music.set_volume(0.1)
        self.shotgun.set_volume(0.1)
        self.npc_pain.set_volume(0.2)
        self.npc_attack.set_volume(0.102)
        self.npc_pain.set_volume(0.2)
