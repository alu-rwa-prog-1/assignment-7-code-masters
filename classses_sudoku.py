#Authors: Marthely237 and Sammyiel

# Importing unittest to help in the class Test
import unittest


class Sudoku:
    """method init:
        initialize the game with n x n number of spaces in grid"""
## Instance variables
    # self.value = 0
    # self.row = row
    # self.column = column
    # self.block = (row // 3) * 3 + column // 3
    # self.permitted_values = set([])


class Board:
    """Sudoku board consisting of
           an ordered list of field objects
           dictionaries which link row/column/block number to the associated ordered list of field objects
           a filled attributed which tracks how many fields are already filled, later used for breaking the solve loop"""

## Instance variables
    # self.fields = []
    # self.rows = {i: [] for i in range(9)}
    # self.columns = {i: [] for i in range(9)}
    # self.blocks = {i: [] for i in range(9)}
    # self.filled = 0


# To test the using assertions in unittest
class TestSudoku(unittest.TestCase):

## Instance variables
    # self.assertEqual(no_rows + no_columns, 18)
    # self.assertEqual(no_rows, 9)
    # self.assertEqual(no_rows + no_columns, 81)

    """Apply assertNotEqual so that a number is not repeated in a row or column

        Apply assertRaisesValueError when the value input is out of range

        Test whether the input is a number and nothing else

        Testing that the input is just one digit"""
