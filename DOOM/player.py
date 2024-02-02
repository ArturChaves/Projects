from settings import *
import pygame as pg
from math import *

class player:
    def __init__(self, Game):
        self.game = Game
        self.x, self.y = player_position
        self.angle = player_angle
        self.shot = False
        self.health = player_max_life
        self.rel = 0
        self.health_recovery_delay = 1200
        self.time_prev = pg.time.get_ticks()



    def recover_health(self):
        if self.check_health_recovery_delay() and self.health < player_max_life:
            self.health += 5
            if self.health > 100:
                self.health = 100
    def check_health_recovery_delay(self):
        time_now = pg.time.get_ticks()
        if time_now - self.time_prev > self.health_recovery_delay:
            self.time_prev = time_now
            return True


    def check_game_over(self):
        if self.health < 1:
            self.game.ObjectRender.game_over()
            pg.display.flip()
            pg.time.delay(1500)
            self.game.start_game()

    def get_damage(self, damage):
        self.health -= damage
        self.game.ObjectRender.player_damage()           
        self.game.sound.player_pain.play()
        self.check_game_over()

    def single_fire_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 and not self.shot and not self.game.weapon.reloading:
                self.game.sound.shotgun.play()
                self.shot = True
                self.game.weapon.reloading = True

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

        # if keys[pg.K_LEFT]:
        #     self.angle -= player_rot_speed * self.game.delta_time
        # if keys[pg.K_RIGHT]:
        #     self.angle += player_rot_speed * self.game.delta_time
        self.angle %= tau
    
    def check_wall(self, x , y):
        return(x , y) not in self.game.map.world_map
    
    def check_wall_collision(self, dx, dy):
        scale = player_size_scale / self.game.delta_time
        if self.check_wall(int(self.x+dx * scale), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy * scale)):
            self.y += dy

    def draw(self):
        #pg.draw.line(self.game.screen, 'yellow', (self.x * 100, self.y * 100),
        #             (self.x * 100 + width * cos(self.angle),
        #              self.y * 100 + width * sin(self.angle)), 2)
        pg.draw.circle(self.game.screen, 'green', (self.x* 100, self.y * 100), 15)

    def mouse_control(self):
        mx, my = pg.mouse.get_pos()
        if mx < mouse_border_left or mx > mouse_border_right:
            pg.mouse.set_pos([half_width, half_height])
        self.rel = pg.mouse.get_rel()[0]
        self.rel = max(-mouse_max_rel, min(mouse_max_rel, self.rel))
        self.angle += self.rel * mouse_sensitivity * self.game.delta_time
    
    def update(self):
        self.movment()
        self.mouse_control()
        self.recover_health()

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)