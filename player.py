import numpy as np

class Player:
    """
        Represents a player
    """

    def getMove(self, board):
        """
            Returns the next move for this player
        """
        raise Exception("Astract function")

class Human(Player):
    """
        Represents an interactive player
    """

    def getMove(self, board):
        """
            Returns the input of the player
        """
        try:
            return int(input())
        except:
            return -1
            
class Random(Player):
    """
        Represents a random player
    """

    def getMove(self, board):
        """
            Returns a random number in the board
        """
        return np.random.randint(np.prod(board.shape))
