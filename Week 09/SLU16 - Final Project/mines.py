"""
Here will be the class with the Minesweeper game Class.

Here are the exercises for this SLU16:
    * Create the method `check_if_mine`
    * Create the method `count_mines_around`
    * Create the method `click_around`

Here are a few hints:
    1. Start by reading the docstring to understand what is required from it.
    2. Check if you can call other methods to help you with the implementation.
    3. You can use the `print` function to debug your code.
"""
from typing import List, Tuple
import random

from constants import Square, SQUARE_CORRESPONDENCE


class MinesweeperGame:
    """
    Class responsible for the Minesweeper game.

    The class responsible for saving the current state of the game.
    It contains the positions of the mines, the positions of the flags,
    and the positions of the squares that have been revealed.

    This class also contains the methods responsible for interacting with the game.

    :attr mines: The posicions of the mines
    :attr flags: The positions of the flags
    :attr revealed: The positions and types of squares that have been revealed
    :attr run: True if the game is running, False otherwise
    """
    mines: List[List[int]]
    flags: List[List[int]]
    revealed: List[List[Square]]
    run = True

    def __init__(self, width, height):
        """
        This method is responsible for initializing the game.

        :param width: The width of the game
        :param height: The height of the game

        :Example:
        >>> game = MinesweeperGame(3, 3)
        >>> game.mines
        [[0, 0, 0], [0, 0, 0], [0, 0, 1]]
        >>> game.flags
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        >>> game.is_running()
        True
        >>> game.right_click(2, 2)
        >>> game.is_running()
        False
        """

        self.mines = self.generate_mines(width, height)
        self.flags = [[0 for _ in range(width)] for _ in range(height)]
        self.revealed = [[Square.UNKNOWN for _ in range(width)] for _ in range(height)]

    def generate_mines(self, width, height) -> List[List[int]]:
        """
        This method generates the mines randomly.

        :param width: The width of the grid
        :param height: The height of the grid
        :return: The mines
        """
        mines = []
        for _ in range(height):
            # Probabilities of mines are set to 1/10
            mines_h = random.choices([0,1], [0.9,0.1], k=width)
            mines.append(mines_h)
        return mines

    def right_click(self, x: int, y: int):
        """
        This method puts a flag in (x,y) or removes it, if it is already there.

        :param x: The x position
        :param y: The y position
        """
        if self.revealed[x][y] == Square.UNKNOWN:
            self.flags[x][y] = 1
            self.revealed[x][y] = Square.FLAG
            if self.found_all_mines():
                self.run = False
        elif self.revealed[x][y] == Square.FLAG:
            # If flag is already there, remove it
            self.flags[x][y] = 0
            self.revealed[x][y] = Square.UNKNOWN

    def found_all_mines(self) -> bool:
        """
        This method checks if all mines have been flagged.

        :return: True if the mines have been identified, False otherwise
        """
        return self.mines == self.flags

    def click(self, x: int, y: int):
        """
        This method is responsible for clicking on the grid.

        :param x: The x position
        :param y: The y position
        """
        if self.revealed[x][y] == Square.UNKNOWN:
            if self.check_if_mine(x,y):
                self.revealed[x][y] = Square.MINE
                self.run = False
            else:
                number_of_mines_around_pos = self.count_mines_around(x, y)
                self.revealed[x][y] = (
                    SQUARE_CORRESPONDENCE[number_of_mines_around_pos])
                if number_of_mines_around_pos == 0:
                    self.click_around(x, y)

    def get_surrounding_cells(self, x: int, y: int) -> List[Tuple[int]]:
        """
        This method gets the positions of the surrounding cells of (x, y).

        :param x: The x position
        :param y: The y position
        :return: The surrounding (x,y) positions

        :Example:
        >>> game = MinesweeperGame(3, 3)
        >>> game.get_surrounding_cells(1, 1)
        [(0, 0), (1, 0), (2, 0), (0, 1), (2, 1), (0, 2), (1, 2), (2, 2)]
        """
        min_x = max(x-1, 0)
        max_x = min(x+1, len(self.mines)-1)
        min_y = max(y-1, 0)
        max_y = min(y+1, len(self.mines[0])-1)
        return [
            (new_x, new_y) for new_y in range(min_y, max_y+1) 
            for new_x in range(min_x, max_x+1) 
            if (new_y != y or new_x != x)
        ]
    
    def check_if_mine(self, x: int, y: int) -> bool:
        """
        This method checks if there is a mine in (x,y) position.

        :param x: The x position
        :param y: The y position

        :return: True if there is a mine, False otherwise

        :Example:
        >>> game = MinesweeperGame(3, 3)
        >>> game.mines
        [[0, 0, 0], [0, 0, 0], [0, 0, 1]]
        >>> game.check_if_mine(2, 2)
        True
        """
        return False # TODO: check if mine is in (x,y) position

    def count_mines_around(self, x: int, y: int) -> int:
        """
        This method counts the mines around (x,y) position.

        :param x: The x position
        :param y: The y position

        :return: The number of mines around (x,y) position

        :Example:
        >>> game = MinesweeperGame(3, 3)
        >>> game.mines
        [[0, 0, 0], [0, 0, 0], [0, 0, 1]]
        >>> game.count_mines_around(1, 1)
        1
        """
        return False # TODO: counts the mines around (x,y) position

    def click_around(self, x: int, y: int):
        """
        This method is responsible for clicking around (x,y) position.

        This method is used for clicking around positions that have no 
        mines around them. This helps speeding up the game.

        :param y: The y position
        :param x: The x position

        :return: None. Should just click on the (x,y) positions.

        :Example:
        >>> game = MinesweeperGame(3, 3)
        >>> game.mines
        [[0, 0, 0], [0, 0, 0], [0, 0, 1]]
        >>> game.revealed
        [
            [Square.UNKNOWN, Square.UNKNOWN, Square.UNKNOWN],
            [Square.UNKNOWN, Square.UNKNOWN, Square.UNKNOWN],
            [Square.UNKNOWN, Square.UNKNOWN, Square.UNKNOWN]
        ]
        >>> game.click_around(1, 1)
        >>> game.revealed
        [
            [Square.EMPTY, Square.EMPTY, Square.EMPTY],
            [Square.EMPTY, Square.UNKNOWN, Square.ONE],
            [Square.EMPTY, Square.ONE, Square.MINE]
        ]
        
        Note that we only click around the position (1,1) and not itself
        Hint: looking at the 'test_area_revealed' method in tests.py might 
        be helpful. 
        """
        for new_x, new_y in self.get_surrounding_cells(x, y):
            pass # TODO: reveal positions that have no mines around them

    def is_running(self) -> bool:
        """
        This method is responsible to check if the game is running.

        :return: True if the game is running, False otherwise
        """
        return self.run