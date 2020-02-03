from TicTacToeBoard import TicTacToeBoard

class TicTacToeInterpreter():
	"""docstring for TicTacToeInterpreter"""
	def __init__(self):
		pass

	prevTttBoard = TicTacToeBoard()
	currTttBoard = TicTacToeBoard()
	
	def LoadPrevTttBoard(self, tttBoard):
		self.prevTttBoard = tttBoard

	def LoadCurrTttBoard(self, tttBoard):
		self.currTttBoard = tttBoard

	def CalculatePlay(self):
		if self.currTttBoard.GetBox(0, 0) == 'X' and self.currTttBoard.GetBox(0, 1) == 'X' and self.currTttBoard.GetBox(0, 2) == 'X':
			print("Agent win! 1")
			return 'X'
		if self.currTttBoard.GetBox(1, 0) == 'X' and self.currTttBoard.GetBox(1, 1) == 'X' and self.currTttBoard.GetBox(1, 2) == 'X':
			print("Agent win! 2")
			return 'X'
		if self.currTttBoard.GetBox(2, 0) == 'X' and self.currTttBoard.GetBox(2, 1) == 'X' and self.currTttBoard.GetBox(2, 2) == 'X':
			print("Agent win! 3")
			return 'X'
		if self.currTttBoard.GetBox(0, 0) == 'X' and self.currTttBoard.GetBox(1, 0) == 'X' and self.currTttBoard.GetBox(2, 0) == 'X':
			print("Agent win! 4")
			return 'X'
		if self.currTttBoard.GetBox(0, 1) == 'X' and self.currTttBoard.GetBox(1, 1) == 'X' and self.currTttBoard.GetBox(2, 1) == 'X':
			print("Agent win! 5")
			return 'X'
		if self.currTttBoard.GetBox(0, 2) == 'X' and self.currTttBoard.GetBox(1, 2) == 'X' and self.currTttBoard.GetBox(2, 2) == 'X':
			print("Agent win! 6")
			return 'X'
		if self.currTttBoard.GetBox(0, 0) == 'X' and self.currTttBoard.GetBox(1, 1) == 'X' and self.currTttBoard.GetBox(2, 2) == 'X':
			print("Agent win! 7")
			return 'X'
		if self.currTttBoard.GetBox(0, 2) == 'X' and self.currTttBoard.GetBox(1, 1) == 'X' and self.currTttBoard.GetBox(2, 0) == 'X':
			print("Agent win! 8")
			return 'X'

		if self.currTttBoard.GetBox(0, 0) == 'O' and self.currTttBoard.GetBox(0, 1) == 'O' and self.currTttBoard.GetBox(0, 2) == 'O':
			print("Player win! 1")
			return 'O'
		if self.currTttBoard.GetBox(1, 0) == 'O' and self.currTttBoard.GetBox(1, 1) == 'O' and self.currTttBoard.GetBox(1, 2) == 'O':
			print("Player win! 2")
			return 'O'
		if self.currTttBoard.GetBox(2, 0) == 'O' and self.currTttBoard.GetBox(2, 1) == 'O' and self.currTttBoard.GetBox(2, 2) == 'O':
			print("Player win! 3")
			return 'O'
		if self.currTttBoard.GetBox(0, 0) == 'O' and self.currTttBoard.GetBox(1, 0) == 'O' and self.currTttBoard.GetBox(2, 0) == 'O':
			print("Player win! 4")
			return 'O'
		if self.currTttBoard.GetBox(0, 1) == 'O' and self.currTttBoard.GetBox(1, 1) == 'O' and self.currTttBoard.GetBox(2, 1) == 'O':
			print("Player win! 5")
			return 'O'
		if self.currTttBoard.GetBox(0, 2) == 'O' and self.currTttBoard.GetBox(1, 2) == 'O' and self.currTttBoard.GetBox(2, 2) == 'O':
			print("Player win! 6")
			return 'O'
		if self.currTttBoard.GetBox(0, 0) == 'O' and self.currTttBoard.GetBox(1, 1) == 'O' and self.currTttBoard.GetBox(2, 2) == 'O':
			print("Player win! 7")
			return 'O'
		if self.currTttBoard.GetBox(0, 2) == 'O' and self.currTttBoard.GetBox(1, 1) == 'O' and self.currTttBoard.GetBox(2, 0) == 'O':
			print("Player win! 8")
			return 'O'