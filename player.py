import random
from turtle import position

import pygame
from pygame.math import Vector2


import core


class Player:
    def __init__(self):
        self.position = Vector2(600,800)
        self.rayon = 20
        self.nourriture = 1
        self.couleur = (250,255,255)
        self.vitesse = Vector2(0, 0)
        self.acceleration = Vector2(0, 0)
        self.maxacc = 100
        self.l0 = 10
        self.k = 0.001
        self.vitessmin = 1
        self.vitessmax = 5
        self.vel = Vector2(random.uniform(-5, 5), random.uniform(-5, 5))

    def bordure(self, fenetre):
        if self.position.y < 0:
            self.position.y = fenetre[1]

        if self.position.y > fenetre[1]:
            self.position.y = 0

        if self.position.x < 0:
            self.position.x = fenetre[0]

        if self.position.x > fenetre[0]:
            self.position.x = 0

    def moov(self, destination):
        if destination is not None:
            # F=uk|l-lo|
            l = self.position.distance_to(destination)
            u = destination - self.position
            u = u.normalize()
            self.acceleration = u * self.k * abs(l - self.l0)

        if self.acceleration.length() > self.maxacc:
            self.acceleration.scale_to_length(self.maxacc)

        self.vitesse = self.vitesse + self.acceleration

        if self.vitesse.length() > self.vitessmax:
            self.vitesse.scale_to_length(self.vitessmax)

        if self.vitesse.length() + 2 < self.vitessmin:
            self.vitesse.scale_to_length(self.vitessmin)

        self.position = self.position + self.vitesse

        self.acceleration = Vector2(0, 0)



    def show(self):
        #core.Draw.circle(self.couleur, self.position, self.rayon)

        a = 0 - self.position.angle_to(Vector2(0, 1))

        p1 = self.position + Vector2(-5, 0).rotate(a)
        p2 = self.position + Vector2(0, 15).rotate(a)
        p3 = self.position + Vector2(5, 0).rotate(a)

        core.Draw.polygon((255, 255, 255), ((p1), (p2), (p3)))
