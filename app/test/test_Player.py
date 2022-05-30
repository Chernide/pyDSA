import pytest
from ..enums.colorEnums import ColorEnums
from ..src.Player import Player
from ..src.Tile import Tile

class TestPlayer:
    player = Player("Test Name", ColorEnums.PINK)
    
    @pytest.mark.order(1)
    def test_constructor(self):
        assert "Test Name" == self.player.getName()
        assert ColorEnums.PINK == self.player.getColor()
    
    @pytest.mark.order(2)
    def test_addTreasure(self):
        treasure = Tile(1, 2)
        self.player.addTreasure(treasure)
        assert treasure == self.player.treasure[0]

    @pytest.mark.order(3)
    def test_getNumTreasure(self):
        assert 1 == self.player.getNumTreasure()
        treasure = Tile(2, 4)
        self.player.addTreasure(treasure)
        assert 2 == self.player.getNumTreasure()

    @pytest.mark.order(5)
    def test_addTreasuretoVault(self):
        self.player.addTreasureToVault()
        assert 0 == self.player.getNumTreasure()
        assert 2 == len(self.player.getVaultTreasures())
        self.player.addTreasure(Tile(1, 2))
        self.player.addTreasure(Tile(2, 4))

    @pytest.mark.order(6)
    def test_removeTreasure(self):
        print(self.player.treasure)
        treasureToRemove = Tile(1, 2)
        self.player.removeTreasure(treasureToRemove)
        assert 1 == self.player.getNumTreasure()
        assert 2 == self.player.treasure[0].getDots()
        assert 4 == self.player.treasure[0].getValue()

    @pytest.mark.order(7)
    def test_removeAllTreasure(self):
        self.player.removeAllTreasure()
        assert 0 == self.player.getNumTreasure()

    @pytest.mark.order(4)
    def test_getLowestTreasure(self):
        print(self.player.treasure)
        receivedTreasure = self.player.getLowestTreasure()
        assert 1 == receivedTreasure.getDots()
        assert 2 == receivedTreasure.getValue()
        assert 1 == self.player.getNumTreasure()
        self.player.addTreasure(Tile(1, 2))