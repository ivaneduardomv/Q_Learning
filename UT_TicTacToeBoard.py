import unittest

from TicTacToeBoard import TicTacToeBoard

class UT_TestTicTacToeBoard(unittest.TestCase):
	"""docstring for UT_TestTicTacToeBoard"""
	def test_ThrowX(self):
		tttBoard = TicTacToeBoard()

		tttBoard.ThrowX(0, 0)
		self.assertEqual(tttBoard.boardArray[0], 'X')

		tttBoard.ThrowX(0, 1)
		self.assertEqual(tttBoard.boardArray[1], 'X')

		tttBoard.ThrowX(0, 2)
		self.assertEqual(tttBoard.boardArray[2], 'X')

		tttBoard.ThrowX(1, 0)
		self.assertEqual(tttBoard.boardArray[3], 'X')

		tttBoard.ThrowX(1, 1)
		self.assertEqual(tttBoard.boardArray[4], 'X')

		tttBoard.ThrowX(1, 2)
		self.assertEqual(tttBoard.boardArray[5], 'X')

		tttBoard.ThrowX(2, 0)
		self.assertEqual(tttBoard.boardArray[6], 'X')

		tttBoard.ThrowX(2, 1)
		self.assertEqual(tttBoard.boardArray[7], 'X')

		tttBoard.ThrowX(2, 2)
		self.assertEqual(tttBoard.boardArray[8], 'X')

	def test_ThrowO(self):
		tttBoard = TicTacToeBoard()

		tttBoard.ThrowO(0, 0)
		self.assertEqual(tttBoard.boardArray[0], 'O')

		tttBoard.ThrowO(0, 1)
		self.assertEqual(tttBoard.boardArray[1], 'O')

		tttBoard.ThrowO(0, 2)
		self.assertEqual(tttBoard.boardArray[2], 'O')

		tttBoard.ThrowO(1, 0)
		self.assertEqual(tttBoard.boardArray[3], 'O')

		tttBoard.ThrowO(1, 1)
		self.assertEqual(tttBoard.boardArray[4], 'O')

		tttBoard.ThrowO(1, 2)
		self.assertEqual(tttBoard.boardArray[5], 'O')

		tttBoard.ThrowO(2, 0)
		self.assertEqual(tttBoard.boardArray[6], 'O')

		tttBoard.ThrowO(2, 1)
		self.assertEqual(tttBoard.boardArray[7], 'O')

		tttBoard.ThrowO(2, 2)
		self.assertEqual(tttBoard.boardArray[8], 'O')

	def test_GetBox(self):
		tttBoard = TicTacToeBoard()

		self.assertEqual(tttBoard.GetBox(0,0), 'E')
		tttBoard.boardArray[0] = 'X'
		self.assertEqual(tttBoard.GetBox(0,0), 'X')

		self.assertEqual(tttBoard.GetBox(0,1), 'E')
		tttBoard.boardArray[1] = 'O'
		self.assertEqual(tttBoard.GetBox(0,1), 'O')

		self.assertEqual(tttBoard.GetBox(0,2), 'E')
		tttBoard.boardArray[2] = 'X'
		self.assertEqual(tttBoard.GetBox(0,2), 'X')


		self.assertEqual(tttBoard.GetBox(1,0), 'E')
		tttBoard.boardArray[3] = 'X'
		self.assertEqual(tttBoard.GetBox(1,0), 'X')

		self.assertEqual(tttBoard.GetBox(1,1), 'E')
		tttBoard.boardArray[4] = 'O'
		self.assertEqual(tttBoard.GetBox(1,1), 'O')

		self.assertEqual(tttBoard.GetBox(1,2), 'E')
		tttBoard.boardArray[5] = 'X'
		self.assertEqual(tttBoard.GetBox(1,2), 'X')


		self.assertEqual(tttBoard.GetBox(2,0), 'E')
		tttBoard.boardArray[6] = 'X'
		self.assertEqual(tttBoard.GetBox(2,0), 'X')

		self.assertEqual(tttBoard.GetBox(2,1), 'E')
		tttBoard.boardArray[7] = 'O'
		self.assertEqual(tttBoard.GetBox(2,1), 'O')

		self.assertEqual(tttBoard.GetBox(2,2), 'E')
		tttBoard.boardArray[8] = 'X'
		self.assertEqual(tttBoard.GetBox(2,2), 'X')

if __name__ == '__main__':
	unittest.main()
