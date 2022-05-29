from unittest.mock import patch

import pytest

from mines import MinesweeperGame
from constants import Square


TESTING_GRID = [
    [0,0,0,0],
    [0,0,0,0],
    [0,1,0,1],
    [1,0,0,0],
]

@pytest.fixture
def mines():
    with patch('mines.MinesweeperGame.generate_mines', return_value=TESTING_GRID):
        mines = MinesweeperGame(4,4)
    return mines


def test_click_mine(mines: MinesweeperGame):
    mines.click(2,1)
    assert (mines.revealed[2][1] == Square.MINE)

@pytest.mark.parametrize(
    "x,y,result",
    [(0,0,Square.EMPTY), (2,0, Square.TWO), (3,3,Square.ONE)])
def test_click_empty(mines: MinesweeperGame, x: int, y: int, result: Square):
    mines.click(x,y)
    assert (mines.revealed[x][y] == result)


def test_area_revealed(mines: MinesweeperGame):
    revealed = [
        [Square.EMPTY, Square.EMPTY, Square.EMPTY, Square.EMPTY],
        [Square.ONE, Square.ONE, Square.TWO, Square.ONE],
        [Square.UNKNOWN, Square.UNKNOWN, Square.UNKNOWN, Square.UNKNOWN],
        [Square.UNKNOWN, Square.UNKNOWN, Square.UNKNOWN, Square.UNKNOWN],
    ]
    mines.click(0,0)
    assert (mines.revealed == revealed)


