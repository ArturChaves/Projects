from settings import *
import pygame as pg
import sys
from player import *
from map import *
from raycasting import *
from ObjectRender import *
from sprite_objects import *
from ObjectHandler import *
from weapon import *
from sound import *
from pathFinder import *
class game:
    def __init__(self):
        pg.mixer.init()
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(res)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.global_trigger = False
        self.global_event = pg.USEREVENT + 0
        pg.time.set_timer(self.global_event, 40)
        self.start_game()

    def start_game(self):
        self.map = map(self)
        self.player = player(self)
        self.ObjectRender = object_render(self)
        self.raycasting = RayCasting(self)
        self.object_handler = ObjectHandler(self)
        self.weapon = Weapon(self)
        self.sound = Sound(self)
        self.pathfinding = PathFinding(self)
        pg.mixer.music.play()

    def update(self):
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        self.weapon.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(fps)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    
    def draw(self):
        #self.screen.fill('black')
        self.ObjectRender.draw()
        self.weapon.draw()
        #self.map.draw()
        #self.player.draw()
    
    def check_events(self):
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == self.global_event:
                self.global_trigger = True
                
        
            self.player.single_fire_event(event)
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = game()
    game.run()