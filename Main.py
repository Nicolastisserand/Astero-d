import pygame
import core
from player import Player
from asteroid import Asteroid

def setup():
    print("Setup START----------")

    core.fps = 60
    core.WINDOW_SIZE = [1200, 1000]
    core.memory("p", Player())
    core.memory("a", Asteroid())
    core.memory("listAsteroid", [])
    core.memory("nbrAsteroid", 10)


    for i in range(0, core.memory("nbrAsteroid")):
        core.memory("listAsteroid").append(Asteroid())




    print("Setup END----------")


def run ():
    core.cleanScreen()
    print(core.getkeyPressValue())



    core.memory("p").show()
    core.memory("a").bordure(core.WINDOW_SIZE)
    core.memory("p").moov(core.getMouseLeftClick())

    for monasteroid in core.memory("listAsteroid"):
        monasteroid.show(core.screen)
        monasteroid.deplacement()
        monasteroid.bordure(core.WINDOW_SIZE)






core.main(setup, run)