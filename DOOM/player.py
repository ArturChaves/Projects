from settings import *
import pygame as pg
from math import *

class player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = player_position
        self.angle = player_angle

    def movment(self):
        sin_a = sin(self.angle)
        cos_a = cos(self.angle)
        dx, dy = 0, 0
        speed = player_speed * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dx +=  speed_cos
            dy +=  speed_sin
        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_a]:
            dx +=  speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            dx += -speed_sin
            dy +=  speed_cos
        
        self.check_wall_collision(dx, dy)  

        if keys[pg.K_LEFT]:
            self.angle -= player_rot_speed * self.game.delta_time
        if keys[pg.K_RIGHT]:
            self.angle += player_rot_speed * self.game.delta_time
        self.angle %= tau
    
    def check_wall(self, x , y):
        return(x , y) not in self.game.map.world_map
    
    def check_wall_collision(self, dx, dy):
        if self.check_wall(int(self.x+dx), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy)):
            self.y += dy

    def draw(self):
        #pg.draw.line(self.game.screen, 'yellow', (self.x * 100, self.y * 100),
        #             (self.x * 100 + width * cos(self.angle),
        #              self.y * 100 + width * sin(self.angle)), 2)
        pg.draw.circle(self.game.screen, 'green', (self.x* 100, self.y * 100), 15)
    
    def update(self):
        self.movment()

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)