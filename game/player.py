import pygame as pg

class Player:
    def __init__(self, initial_x, initial_y):
        self._score = 0
        self._x = initial_x
        self._y = initial_y

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value

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

    def draw_striker(self, window, oppenent, color, upper_y, lower_y):
        if(oppenent == False):
            mouse_x, mouse_y = pg.mouse.get_pos()
            self._x = mouse_x
        
            if (mouse_y > upper_y+15 and mouse_y < lower_y-15):
                self._y = mouse_y

        self.hitbox = pg.Rect(self._x-30, self._y-30, 60, 60)
            
        pg.draw.circle(window, color, [self._x, self._y], 30)
        pg.draw.circle(window, "white", [self._x, self._y], 25, 5)

    def set_pos(self, x, y):
        self._x = x
        self._y = y

    def get_hitbox(self):
        return self.hitbox
