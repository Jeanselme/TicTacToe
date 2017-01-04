import numpy as np

def threeAlign(board):
	"""
	Returns True if the last move allows the player to win
			False otherwise
	"""
	# Diagonals
	if abs(board.trace()) == 3:
		return True
	if abs(np.fliplr(board).trace()) == 3:
		return True

	# Rows
	if 3 in abs(np.sum(board, axis=1)):
		return True

	# Columns
	if 3 in abs(np.sum(board, axis=0)):
		return True

	return False

def mapPosition(choice):
	"""
	Transforms the choice into a position tuple
	"""
	return (int((choice-1)/3), (choice-1)%3)

def acceptableChoice(board, choice):
	"""
	Returns True iif the choice is possible
	"""
	if choice < 1 or choice > 9 or board[mapPosition(choice)] != 0:
		return False
	else:
		return True

def play(display):
	"""
	Asks the player to give a number between 1 and 9
	"""
	if display:
		print("\nChoose a position as follow : \n{}".format(np.arange(1,10).reshape((3,3))))
	else:
		print("Bad move, try another one!")
	try:
		return int(input())
	except Exception as e:
		return -1

def ticTacToe():
	player = 1
	board = np.zeros((3,3))
	while(not threeAlign(board) and np.sum(abs(board)) != 9):
		player *= -1
		choice = -1
		display = True
		while not acceptableChoice(board, choice):
			choice = play(display)
			display = False
		board[mapPosition(choice)] = player
		print(board)

	if threeAlign(board):
		print("Player {} wins the game !".format(player))
		return player
	else :
		print("Draw")
		return 0

if __name__ == '__main__':
	ticTacToe()
