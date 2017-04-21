from player.player import *
from game.tictactoe import *
from utils.analysis import *

import numpy as np

def computeProbabilityByExperiment(size = 3, numberOfGame = 100000):
	"""
		Compute the probability of the output game by simulating multiple game
	"""
	result = {-1:0, 0:0, 1:0}
	for i in range(numberOfGame):
	    # Create a new game
		game = ticTacToe(RandomAdvanced(), RandomAdvanced(), size, False)
	    # Update probability
		result[game.playGame()] += 1

	print("Estimation by simulation")
	print("Probability of draws : {} / {} = {}".format(result[0], numberOfGame, result[0]/numberOfGame))
	print("Probability of victory of first player : {} / {} = {}".format(result[-1], numberOfGame, result[-1]/numberOfGame))
	print("Probability of victory of seconde player : {} / {} = {}".format(result[1], numberOfGame, result[1]/numberOfGame))

def computeProbabilityByTree(size = 3):
	"""
		Computes the full tree
	"""
	states = []
	victory = []
	victoryLevel = [0]*(size**2)
	result = {-1:0, 0:0, 1:0}
	possibilities = [0]*(size**2)

	def playAllPossibility(game, level=0):
		"""
			Non optimal way of computing the different possibilities
			Depth first
		"""
		for i in range(1,game.size**2+1):
			if game.acceptableChoice(i):
				possibilities[level] += 1
				gameCopy = game.copy()
				gameCopy.play(i)
				node = Node(game, gameCopy.board, 0)
				if node not in states:
					# Add nodes and continue recursion
					states.append(node)
					if gameCopy.endGame():
						victory.append(node)
						victoryLevel[level] += 1
						if gameCopy.alignment():
							result[-gameCopy.playerId] += 1
						else:
							result[0] += 1
					else:
						playAllPossibility(gameCopy, level+1)


	playAllPossibility(ticTacToe(Human(), Human(), size))
	meanVictoryLevel = np.sum(np.multiply(victoryLevel,list(range(1,len(victoryLevel)+1)))/np.sum(victoryLevel))
	print("Real probabilities")

	print("Number of possible states : {}".format(len(states)))
	print("Number of different ends : {}".format(len(victory)))
	print("Number of victories by level (mean : {})".format(meanVictoryLevel), victoryLevel)
	print("Number of possibilities by level : ", possibilities)

	print("Probability of draws : {} / {} = {}".format(result[0], len(victory), result[0]/len(victory)))
	print("Probability of victory of first player : {} / {} = {}".format(result[-1], len(victory), result[-1]/len(victory)))
	print("Probability of victory of seconde player : {} / {} = {}".format(result[1], len(victory), result[1]/len(victory)))

if __name__ == '__main__':
	computeProbabilityByExperiment(4,100)
	computeProbabilityByTree(4)
