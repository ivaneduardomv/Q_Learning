class TicTacToeBoard():
	"""docstring for TicTacToeBoard"""
	def __init__(self):
		for x in range(9):
			self.boardArray.append('-')

	M = 3
	N = 3
	boardArray = []
	
	def ThrowX(self, coordX, coordY):
		self.boardArray[coordX * self.M + coordY] = 'X'

	def ThrowO(self, coordX, coordY):
		self.boardArray[coordX * self.M + coordY] = 'O'

	def GetBox(self, coordX, coordY):
		return self.boardArray[coordX * self.M + coordY]

	def PrintTttBoard(self):
		for x in range(0,3):
			print("")
			for y in range(0, 3):
				print(self.GetBox(x, y), end=' ')
		print("")