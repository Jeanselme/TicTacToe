import numpy as np

class ticTacToe:
	"""
		Represents the game tic tac toe
	"""

	def __init__(self, player1, player2, size = 3):
		"""
			Size of the board is the square
		"""
		self.size = size
		self.board = np.zeros((size,size))

		# Take the two players which can be
		self.players = {-1:player1, 1:player2}
		# Player which have to play
		self.playerId = -1

	def copy(self):
		"""
			Creates the copy of the current game
		"""
		copy = ticTacToe(None, None, self.size)
		copy.board = self.board.copy()
		copy.players = self.players
		copy.playerId = self.playerId
		return copy

	def alignment(self):
		"""
			Returns if there is size of the same player is aligned
		"""
		# Diagonals
		if abs(self.board.trace()) == self.size:
			return True
		if abs(np.fliplr(self.board).trace()) == self.size:
			return True

		# Rows
		if self.size in abs(np.sum(self.board, axis=1)):
			return True

		# Columns
		if self.size in abs(np.sum(self.board, axis=0)):
			return True

		return False

	def endGame(self):
		"""
			Returns True if the game is ended
		"""
		return self.alignment() or np.sum(abs(self.board)) == self.size**2

	def mapPosition(self, choice):
		"""
			Transforms the choice into a position tuple
		"""
		return (int((choice-1)/self.size), (choice-1)%self.size)

	def acceptableChoice(self, choice):
		"""
			Returns True iif the choice is possible
		"""
		if choice < 1 or choice > self.size**2 or self.board[self.mapPosition(choice)] != 0:
			return False
		else:
			return True

	def askMove(self, display):
		"""
			Asks the player to give a number between 1 and 9
		"""
		if display:
			print("\nChoose a position as follow : \n{}".format(np.arange(1,self.size**2 + 1).reshape((self.size,self.size))))
		else:
			print("Bad move, try another one!")

	def printBoard(self):
		"""
			Prints the boards
		"""
		print(self.board)

	def play(self, position):
		"""
			Apply the move of the current player at the given position
			Change the current player
			The move has to be verified with acceptable choice
		"""
		self.board[self.mapPosition(position)] = self.playerId
		self.playerId *= -1

	def playGame(self):
		"""
			Create the full game until victory of a player
		"""
		while not(self.endGame()):
			choice = -1
			display = True
			while not self.acceptableChoice(choice):
				self.askMove(display)
				choice = self.players[self.playerId].getMove(self.board)
				display = False
			self.play(choice)
			self.printBoard()

		if self.alignment():
			# Minus the current player because of self.play
			print("Player {} wins the game !".format(-self.playerId))
			return -self.playerId
		else :
			print("Draw")
			return 0
