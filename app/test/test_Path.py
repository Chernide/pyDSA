from unittest import TestProgram
import pytest
from ..src.Path import Path
from ..src.Tile import Tile



class TestPath():
    testPath = Path()

    def test_constructor(self):
        assert 32 == self.testPath.getPathSize()
        for i in range(0, 8):
            assert 1 == self.testPath.getTile(i).getDots()
            assert 0 <= self.testPath.getTile(i).getValue()
            assert 3 >= self.testPath.getTile(i).getValue()

        for i in range(8, 16):
            assert 2 == self.testPath.getTile(i).getDots()
            assert 4 <= self.testPath.getTile(i).getValue()
            assert 7 >= self.testPath.getTile(i).getValue()

        for i in range(16, 24):
            assert 3 == self.testPath.getTile(i).getDots()
            assert 8 <= self.testPath.getTile(i).getValue()
            assert 11 >= self.testPath.getTile(i).getValue()

        for i in range(24, 32):
            assert 4 == self.testPath.getTile(i).getDots()
            assert 12 <= self.testPath.getTile(i).getValue()
            assert 15 >= self.testPath.getTile(i).getValue()

    def test_getTile(self):
        t1 = self.testPath.getTile(4)
        assert 1 == t1.getDots()
        assert 0 <= t1.getValue()
        assert 3 >= t1.getValue()

        t2 = self.testPath.getTile(28)
        assert 4 == t2.getDots()
        assert 12 <= t2.getValue()
        assert 15 >= t2.getValue()

    def test_replaceTile(self):
        replaceTile = Tile(4, 14)
        oldTile = self.testPath.replaceTile(3, replaceTile)
        pathTile = self.testPath.getTile(3)
        assert 4 == pathTile.getDots()
        assert 14 == pathTile.getValue()
        assert 1 == oldTile.getDots()
        assert 0 <= oldTile.getValue()
        assert 3 >= oldTile.getValue()