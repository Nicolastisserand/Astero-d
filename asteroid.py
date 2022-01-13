import random
import pygame
from pygame.math import Vector2


class Asteroid:
    def __init__(self):
        self.position = Vector2(random.randint(0,1200),random.randint(0,1000))
        self.rayon = 30
        self.couleur = (255, 255, 255)
        self.vivante = True
        self.maxVitesse = 4
        self.maxAcceleration = 0.2
        self.vitesse = Vector2(0, 0)
        self.acceleration = Vector2(0, 0)

    def bordure(self, fenetre):
        if self.position.y < 0:
            self.position.y = fenetre[1]

        if self.position.y > fenetre[1]:
            self.position.y = 0

        if self.position.x < 0:
            self.position.x = fenetre[0]

        if self.position.x > fenetre[0]:
            self.position.x = 0

    def deplacement(self):
        self.acceleration = Vector2(random.uniform(-1, 1), random.uniform(-1, 1))

        if self.acceleration.length() > self.maxAcceleration:
            self.acceleration.scale_to_length(self.maxAcceleration)

        self.vitesse = self.vitesse + self.acceleration

        if self.vitesse.length() > self.maxVitesse:
            self.vitesse.scale_to_length(self.maxVitesse)

        self.position = self.position + self.vitesse

        self.acceleration = Vector2(0, 0)


    def show(self,screen):
        pygame.draw.circle(screen,self.couleur,self.position,self.rayon)

