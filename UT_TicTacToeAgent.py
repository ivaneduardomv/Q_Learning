import unittest

from TicTacToeAgent import TicTacToeAgent
from TicTacToeBoard import TicTacToeBoard

class UT_TestTicTacToeAgent(unittest.TestCase):
	"""docstring for UT_TestTicTacToeBoard"""
	def test_ThrowToken_X(self):
		tttBoard = TicTacToeBoard()
		tttAgentX = TicTacToeAgent('X')
		tttAgentX.tokenCoordX = 0
		tttAgentX.tokenCoordY = 0
		tttAgentX.ThrowToken(tttBoard)
		self.assertEqual(tttBoard.GetBox(0,0), 'X')

	def test_ThrowToken_O(self):
		tttBoard = TicTacToeBoard()
		tttAgentO = TicTacToeAgent('O')
		tttAgentO.tokenCoordX = 1
		tttAgentO.tokenCoordY = 1
		tttAgentO.ThrowToken(tttBoard)
		self.assertEqual(tttBoard.GetBox(1,1), 'O')

	def test_ExecuteAction(self):
		tttBoard = TicTacToeBoard()
		tttAgent = TicTacToeAgent('X')

		tttAgent.ExecuteAction(tttBoard)
		self.assertEqual(tttBoard.GetBox(tttAgent.tokenCoordX, tttAgent.tokenCoordY), 'X')

		tttAgent.ExecuteAction(tttBoard)
		self.assertEqual(tttBoard.GetBox(tttAgent.tokenCoordX, tttAgent.tokenCoordY), 'X')

		tttAgent.ExecuteAction(tttBoard)
		self.assertEqual(tttBoard.GetBox(tttAgent.tokenCoordX, tttAgent.tokenCoordY), 'X')

if __name__ == '__main__':
	unittest.main()
