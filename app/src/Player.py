from ...app.enums.colorEnums import ColorEnums

class Player:
    def __init__(self, name = "", color = ColorEnums.NONE):
        self.name = name
        self.color = color
        self.treasure = []
        self.vault = []
        self.location = -1
        self.turnBack = False
        self.isSafe = False

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setLocation(self, location):
        self.location = location

    def getLocation(self):
        return self.location

    def setTurnBack(self, turnBack):
        self.turnBack = turnBack

    def getTurnBack(self):
        return self.turnBack

    def setIsSafe(self, isSafe):
        self.isSafe = isSafe

    def getIsSafe(self):
        return self.isSafe

    def getTreasures(self):
        return self.treasure

    def getVaultTreasures(self):
        return self.vault

    def getNumTreasure(self):
        return len(self.treasure)
    
    def addTreasure(self, tile):
        self.treasure.append(tile)

    def addTreasureToVault(self):
        self.vault.extend(self.treasure)
        self.removeAllTreasure()

    def removeTreasure(self, tile):
        idx = -1
        for i, t in enumerate(self.treasure):
            if tile.getDots() == t.getDots() and tile.getValue() == t.getValue():
                idx = i
                break
        if idx != -1:
            del self.treasure[idx]

    def removeAllTreasure(self):
        self.treasure.clear()

    def getLowestTreasure(self):
        self.treasure.sort(key=lambda tile: tile.getDots())
        lowestTreasure = self.treasure[0]
        self.treasure.remove(lowestTreasure)
        return lowestTreasure