from sprite_objects import *
from npc import *
class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = 'DOOM/resources/sprites/npc/'
        self.static_sprite_path= 'DOOM/resources/sprites/static_sprites/'
        self.animated_sprite_path= 'DOOM/resources/sprites/animated_sprites/'
        add_sprite = self.add_sprites
        add_npc = self.AddNPC
        self.npc_positions = {}
        

        #Sprite map

        add_sprite(AnimatedSprite(game))
        add_sprite(AnimatedSprite(game, pos=(1.5, 1.5)))
        add_sprite(AnimatedSprite(game, pos=(1.5, 7.5)))
        add_sprite(AnimatedSprite(game, pos=(5.5, 3.25)))
        add_sprite(AnimatedSprite(game, pos=(5.5, 4.75)))
        add_sprite(AnimatedSprite(game, pos=(7.5, 2.5)))
        add_sprite(AnimatedSprite(game, pos=(7.5, 5.5)))
        add_sprite(AnimatedSprite(game, pos=(14.5, 1.5)))
        add_sprite(AnimatedSprite(game, pos=(14.5, 4.5)))
        add_sprite(AnimatedSprite(game, path=self.animated_sprite_path + 'red_light/0.png', pos=(14.5, 5.5)))
        add_sprite(AnimatedSprite(game, path=self.animated_sprite_path + 'red_light/0.png', pos=(14.5, 7.5)))
        add_sprite(AnimatedSprite(game, path=self.animated_sprite_path + 'red_light/0.png', pos=(12.5, 7.5)))
    
        #npc map

        add_npc(NPC(game))
        add_npc(NPC(game, pos= (11.5, 4.5)))
        add_npc(NPC(game, pos= (13, 7)))


    def update(self):
        self.npc_positions = {npc.map_pos for npc in self.npc_list if npc.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]



    def AddNPC(self, npc):
        self.npc_list.append(npc)


    def add_sprites(self, sprite):
        self.sprite_list.append(sprite)