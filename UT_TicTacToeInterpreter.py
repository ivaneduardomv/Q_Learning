import unittest

from TicTacToeBoard import TicTacToeBoard
from TicTacToeInterpreter import TicTacToeInterpreter

class UT_TestTicTacToeInterpreter(unittest.TestCase):
	"""docstring for UT_TestTicTacToeBoard"""
	def test_PrintTttBoar(self):
		tttBoard = TicTacToeBoard()
		tttInterpreter = TicTacToeInterpreter()
		tttInterpreter.PrintTttBoard(tttBoard)

if __name__ == '__main__':
	unittest.main()
