import random
from  ...app.src.Tile import Tile

class Path:
    def __init__(self):
        self.path = self.__generateNewPath()

    def __generateNewPath(self):
        newPath = []
        for i in range(8):
            tile = Tile(1, random.randint(0, 3))
            newPath.append(tile)
        for i in range(8):
            tile = Tile(2, random.randint(4, 7))
            newPath.append(tile)
        for i in range(8):
            tile = Tile(3, random.randint(8, 11))
            newPath.append(tile)
        for i in range(8):
            tile = Tile(4, random.randint(12, 15))
            newPath.append(tile)
        return newPath

    def setPath(self, path):
        self.path = path

    def getPath(self):
        return self.path

    def getTile(self, location):
        return self.path[location]

    def replaceTile(self, location, tile):
        oldTile = self.path[location]
        self.path[location] = tile
        return oldTile

    def getPathSize(self):
        return len(self.path)