import pygame as pg

class Puck:
    def __init__(self):
        self._x = 0
        self._y = 0
        self._vel = 0
        self._x_vel = 0
        self._y_vel = 0
        
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def y_vel(self):
        return self._y_vel

    @y_vel.setter
    def y_vel(self, value):
        self._y_vel = value

    @property
    def x_vel(self):
        return self._x_vel

    @x_vel.setter
    def x_vel(self, value):
        self._x_vel = value

    @property
    def vel(self):
        return self._vel

    @vel.setter
    def vel(self, value):
        self._vel = value
        
    def in_rink(self, width, height):
        return (self.x > 0 and self.x < width) and (self.y > 0 and self.y < height)

    def draw_puck(self, window):
        self.hitbox = pg.Rect(self.x-25, self.y-25, 50, 50)
        
        pg.draw.circle(window, "black", [self.x, self.y], 25)
        pg.draw.circle(window, "dark gray", [self.x, self.y], 20, 1)
    
    def set_pos(self, x, y):
        self._x = x
        self._y = y
        
    def get_hitbox(self):
        return self.hitbox
