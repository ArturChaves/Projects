from settings import *
import pygame as pg
import sys
from player import *
from map import *
from raycasting import *
class game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(res)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.start_game()

    def start_game(self):
        self.map = map(self)
        self.player = player(self)
        self.raycasting = RayCasting(self)

    def update(self):
        self.player.update()
        self.raycasting.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(fps)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')
    
    def draw(self):
        self.screen.fill('black')
        #self.map.draw()
        #self.player.draw()
    
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = game()
    game.run()