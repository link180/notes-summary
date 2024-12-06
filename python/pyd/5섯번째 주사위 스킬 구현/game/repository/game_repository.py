from abc import ABC, abstractmethod


class GameRepository(ABC):

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def setPlayerIndexListToMap(self, playerIndexList, diceIdList):
        pass

    @abstractmethod
    def updatePlayerDiceGameMap(self, skillAppliedPlayerIndexList, secondDiceIdList):
        pass

    @abstractmethod
    def deletePlayer(self, tagetPlayerId):
        pass
