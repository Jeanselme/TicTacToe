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
        return np.random.randint(1, np.prod(board.shape)+1)

class RandomAdvanced(Player):
    """
        Represents a random player which does not try non empty cell
    """

    def getMove(self, board):
        """
            Returns a random number in the board
        """
        indexes = np.array(list(range(np.prod(board.shape))))
        indexes = indexes[[board.flatten() == 0]]
        indexes += 1
        return np.random.choice(indexes)
