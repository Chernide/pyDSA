from time import sleep
from tkinter import Y
from tracemalloc import start
import pygame
from pygame.locals import *
from app.resources.colors import colors 
import random

class App:
    def __init__(self):
        self._running = True
        self.size = self.w, self.h = 800, 800
        self.roll = False
        self.roll_count = 0
        self.startdie1, self.startdie2 = random.randint(0, 2), random.randint(0, 2)
        pygame.init()
        self._display_surface = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._display_surface.fill((colors["background"]))
        self.loadTextures()

    def loadTextures(self):
        self.tileImg = pygame.image.load("./app/resources/tilesScaled.png")
        self.tileOneImg = self.tileImg.subsurface(pygame.Rect(0, 0, 64, 64))
        self.tileTwoImg = self.tileImg.subsurface(pygame.Rect(64, 0, 64, 64))
        self.tileThreeImg = self.tileImg.subsurface(pygame.Rect(0, 64, 64, 64))
        self.tileFourImg = self.tileImg.subsurface(pygame.Rect(64, 64, 64, 64))
        self.dieOneImg = pygame.image.load("./app/resources/dieOne.png")
        self.dieTwoImg = pygame.image.load("./app/resources/dieTwo.png")
        self.dieThreeImg = pygame.image.load("./app/resources/dieThree.png")
        self.subImg = pygame.image.load("./app/resources/submarine.png")

    def onEvent(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.roll = True
            self.roll_count += 1
        elif event.type == pygame.MOUSEBUTTONUP:
            self.roll = False

    def onLoop(self):
        pass

    def onRender(self):
        self._display_surface.blit(self.subImg, (0, 0))
        
        starting_map = [[0,0,0,1,1,1,1],\
                        [0,0,0,0,0,0,1],\
                        [2,2,2,2,1,1,1],\
                        [2,0,0,0,0,0,0],\
                        [2,2,2,3,3,3,3],\
                        [0,0,0,0,0,0,3],\
                        [4,4,4,4,3,3,3],\
                        [4,0,0,0,0,0,0],\
                        [4,4,4,0,0,0,0]]
       
        x, y = 32, 200
        for i in range(0, 9):
            for j in range(0, 7):
                if starting_map[i][j] == 1:
                    self._display_surface.blit(self.tileOneImg, (x, y))
                elif starting_map[i][j] == 2:
                    self._display_surface.blit(self.tileTwoImg, (x, y))
                elif starting_map[i][j] == 3:
                    self._display_surface.blit(self.tileThreeImg, (x, y))
                elif starting_map[i][j] == 4:
                    self._display_surface.blit(self.tileFourImg, (x, y))
                x = (x + 64) % 800
            x = 32
            y = (y + 64) % 800

        dieImgs = [self.dieOneImg, self.dieTwoImg, self.dieThreeImg]
        if self.roll_count == 0:
            self._display_surface.blit(dieImgs[self.startdie1], (750, 10))
            self._display_surface.blit(dieImgs[self.startdie2], (750, 48))
        if self.roll:
            for i in range(0, 10):
                idx1 = random.randint(0, 2)
                idx2 = random.randint(0, 2)
                self._display_surface.blit(dieImgs[idx1], (750, 10))
                self._display_surface.blit(dieImgs[idx2], (750, 48))
                sleep(0.1)
                pygame.display.update()
            roll1 = random.randint(0, 2)
            roll2 = random.randint(0, 2)
            self._display_surface.blit(dieImgs[roll1], (750, 10))
            self._display_surface.blit(dieImgs[roll2], (750, 48))
        pygame.display.update()

    def onCleanup(self):
        pygame.quit()

    def onExecute(self):
        while self._running:
            for event in pygame.event.get():
                self.onEvent(event)
            self.onLoop()
            self.onRender()
        self.onCleanup()

if __name__ == "__main__":
    pyDSA = App()
    pyDSA.onExecute()