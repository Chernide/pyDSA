class Tile:
    def __init__(self, dots = -1, value = -1):
        self.dots = dots
        self.value = value

    def setDots(self, dots):
        self.dots = dots

    def getDots(self):
        return self.dots

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value