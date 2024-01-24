import pygame as pg
from settings import *
from math import *
import os
from collections import deque


class SpriteObject:
    def __init__(self, game, path='DOOM/resources/sprites/static_sprites/candlebra.png', pos= (10.5, 3.5),
                 scale= 0.7, shift= 0.27):
        self.game = game
        self.player = game.player
        self.x, self.y = pos
        self.image = pg.image.load(path).convert_alpha()
        self.image_width = self.image.get_width()
        self.image_half_width = self.image.get_width() // 2
        self.image_ratio = self.image_width / self.image.get_height()
        self.dx, self.dy, self.theta, self.screen_x, self.dist, self.norm_dist = 0, 0, 0, 0, 1, 1
        self.sprite_half_width = 0
        self.sprite_scale = scale
        self.sprite_height_shift = shift

    def GetSpriteProjeciton(self):
        projection = screen_distance / self.norm_dist * self.sprite_scale
        projection_width, projection_height = projection * self.image_ratio, projection

        image = pg.transform.scale(self.image, (projection_width, projection_height))

        self.sprite_half_width = projection_width // 2
        height_shift = projection_height * self.sprite_height_shift
        pos = self.screen_x - self.sprite_half_width, half_height - projection_height // 2 + height_shift

        self.game.raycasting.objects_to_render.append((self.norm_dist, image, pos))

    def get_sprite(self):
        dx = self.x - self.player.x
        dy = self.y - self.player.y
        self.dx, self.dy = dx, dy
        self.theta = atan2(dy, dx)

        delta = self.theta - self.player.angle
        if (dx > 0 and self.player.angle > pi) or (dx < 0 and dy < 0):
            delta += tau

        delta_rays = delta / delta_angle
        self.screen_x = (half_num_rays + delta_rays) * scale

        self.dist = hypot(dx, dy)
        self.norm_dist = self.dist * cos(delta)
        if -self.image_half_width < self.screen_x < (width + self.image_half_width) and self.norm_dist > 0.5:
            self.GetSpriteProjeciton()


    def update(self):
        self.get_sprite()






class AnimatedSprite(SpriteObject):
    def __init__(self, game, path='DOOM/resources/sprites/animated_sprites/green_light/0.png',
                 pos=(11.5, 3.5), scale=0.8, shift=0.15, animation_time=120):
        super().__init__(game, path, pos, scale, shift)
        self.animation_time = animation_time
        self.path = path.rsplit('/', 1)[0]
        self.images = self.get_images(self.path)
        self.animation_time_prev = pg.time.get_ticks()
        self.animation_trigger = False



    def Animate(self, images):
        if self.animation_trigger:
            images.rotate(-1)
            self.image = images[0]

    def update(self):
        super().update()
        self.check_animations_time()
        self.Animate(self.images)


    def check_animations_time(self):
        self.animation_trigger = False
        time_now = pg.time.get_ticks()
        if time_now - self.animation_time_prev > self.animation_time:
            self.animation_time_prev = time_now
            self.animation_trigger = True


    def get_images(self, path):
        images = deque()
        for file_name in os.listdir(path):
            if os.path.isfile(os.path.join(path, file_name)):
                img = pg.image.load(path + '/' + file_name).convert_alpha()
                images.append(img)
        return images

