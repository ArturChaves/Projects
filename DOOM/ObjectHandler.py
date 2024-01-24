from sprite_objects import *

class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.static_sprite_path= 'DOOM/resources/sprites/static_sprites/'
        self.animated_sprite_path= 'DOOM/resources/sprites/animated_sprites/'
        add_sprite = self.add_sprites

        #Sprite map

        add_sprite(SpriteObject(game))
        add_sprite(AnimatedSprite(game))
    


    def update(self):
        [sprite.update() for sprite in self.sprite_list]



    def add_sprites(self, sprite):
        self.sprite_list.append(sprite)