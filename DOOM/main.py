from settings import *
import pygame as pg
import sys
from map import *

class game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(res)
        self.clock = pg.time.Clock()
        self.start_game()

    def start_game(self):
        self.map = map(self)

    def update(self):
        pg.display.flip()
        self.clock.tick(fps)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')
    
    def draw(self):
        self.screen.fill('black')
        self.map.draw()
    
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