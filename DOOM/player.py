from settings import *
import pygame as pd
from math import *

class player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = player_position
        self.angle = self.player_angle

    def movment(self):
        sin_a = sin(self.angle)
        cos_a = cos(self.angle)
    
    def update(self):
        self.movment()

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)