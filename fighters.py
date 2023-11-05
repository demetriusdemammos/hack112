from cmu_graphics import *

class Fighter():
    def __init__(self, x, name, health):
        self.name = name
        self.health = health
        self.x = x
        self.alive = True
    