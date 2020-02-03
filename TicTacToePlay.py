from TicTacToeAgent import TicTacToeAgent
from TicTacToeBoard import TicTacToeBoard
from TicTacToeInterpreter import TicTacToeInterpreter

class TicTacToePlay():
	"""docstring for TicTacToePlay"""
	def __init__(self):
		pass

	tttBoard = TicTacToeBoard()
	tttAgentX = TicTacToeAgent('X')
	tttInterpreter = TicTacToeInterpreter()

	def Play(self):
		print("Write a coordinate pair (x,y) or type \"quit\" to finish.")
		while True:
			command = input("x,y = ")
			if ',' in command:
				coords = command.split(',')
				x = int(coords[0])
				y = int(coords[1])
				self.tttBoard.ThrowO(x, y)
				self.tttBoard.PrintTttBoard()
				winnerToken = self.tttInterpreter.CalculatePlay()
				if winnerToken == 'O':
					break

				self.tttAgentX.ExecuteAction(self.tttBoard)
				self.tttBoard.PrintTttBoard()
				self.tttInterpreter.LoadCurrTttBoard(self.tttBoard)
				winnerToken = self.tttInterpreter.CalculatePlay()
				if winnerToken == 'X':
					break
			elif command == "quit":
				break
		quit()


