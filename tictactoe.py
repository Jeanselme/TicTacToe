import numpy as np

class ticTacToe:
	"""
		Represents the game tic tac toe
	"""

	def __init__(self, size = 3):
		"""
			Size of the board is the square
		"""
		self.size = size
		self.board = np.zeros((size,size))

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
		try:
			return int(input())
		except Exception as e:
			return -1

	def printBoard(self):
		"""
			Prints the boards
		"""
		print(self.board)

	def play(self):
		"""
			Create the full game until victory of a player
		"""
		player = 1
		while(not self.alignment() and np.sum(abs(self.board)) != self.size**2):
			player *= -1
			choice = -1
			display = True
			while not self.acceptableChoice(choice):
				choice = self.askMove(display)
				display = False
			self.board[self.mapPosition(choice)] = player
			self.printBoard()

		if self.alignment():
			print("Player {} wins the game !".format(player))
			return player
		else :
			print("Draw")
			return 0

if __name__ == '__main__':
	game = ticTacToe(5)
	game.play()
