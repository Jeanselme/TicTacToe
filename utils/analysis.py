import numpy as np

class Node:
    """
        Represents a node in the game tree
    """
    def __init__(self, parent, board, probability):
        self.parent = parent
        self.board = board
        self.probability = probability

    def __eq__(self, other):
        """
            Verify if the new configuration is a rotation or reflexion of the
            current node
        """
        sym1 = np.rot90(other.board)
        sym2 = np.rot90(sym1)
        sym3 = np.rot90(sym2)
        ref01 = np.flip(other.board, 0)
        ref02 = np.flip(other.board, 1)
        ref11 = np.flip(sym1, 0)
        ref12 = np.flip(sym1, 1)
        ref21 = np.flip(sym2, 0)
        ref22 = np.flip(sym2, 1)
        ref31 = np.flip(sym3, 0)
        ref32 = np.flip(sym3, 1)
        return np.array_equal(self.board, other.board) or \
            np.array_equal(self.board, sym1) or \
            np.array_equal(self.board, sym2) or \
            np.array_equal(self.board, sym3) or \
            np.array_equal(self.board, ref01) or \
            np.array_equal(self.board, ref02) or \
            np.array_equal(self.board, ref11) or \
            np.array_equal(self.board, ref12) or \
            np.array_equal(self.board, ref21) or \
            np.array_equal(self.board, ref22) or \
            np.array_equal(self.board, ref31) or \
            np.array_equal(self.board, ref32)
