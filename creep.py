import random
import pygame
from pygame.math import Vector2


class Creep:
    def __init__(self):
        self.position = Vector2(random.randint(0,1400),random.randint(0,850))
        self.rayon = 5
        self.couleur = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        self.masse = 10





    def show(self,screen):
        pygame.draw.circle(screen,self.couleur,self.position,self.rayon)


