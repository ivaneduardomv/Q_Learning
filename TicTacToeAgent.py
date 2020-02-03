import random

class TicTacToeAgent():
	"""docstring for TicTacToeAgent"""
	def __init__(self, agentToken):
		if agentToken == 'X' or agentToken == 'O':
			self.token = agentToken

	token = 'E'
	tokenCoordX = 0
	tokenCoordY = 0

	def ThrowToken(self, tttBoard):
		if self.token == 'X':
			tttBoard.ThrowX(self.tokenCoordX, self.tokenCoordY)
		elif self.token == 'O':
			tttBoard.ThrowO(self.tokenCoordX, self.tokenCoordY)
		else:
			print("agentToken not initialized!")

	def Decide(self, tttBoard):
		self.tokenCoordX = random.randint(0,2)
		self.tokenCoordY = random.randint(0,2)
		while '-' != tttBoard.GetBox(self.tokenCoordX, self.tokenCoordY):
			self.tokenCoordX = random.randint(0,2)
			self.tokenCoordY = random.randint(0,2)


	def ExecuteAction(self, tttBoard):
		self.Decide(tttBoard)
		self.ThrowToken(tttBoard)