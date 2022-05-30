from enum import Enum, auto
import pathlib

import pygame

SPRITES_FOLDER = pathlib.Path(__file__).parent / "sprites"


# Colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SCREEN_WIDTH = 320
SCREEN_HEIGHT = 320

SQUARE_SIZE = 32

# Each square will be identified by one a Square instance,
# with a `pygame.image` associated with it.`
class Square(Enum):
    UNKNOWN = pygame.image.load(SPRITES_FOLDER.joinpath("grid.png"))
    EMPTY = pygame.image.load(SPRITES_FOLDER.joinpath("empty.png"))
    MINE = pygame.image.load(SPRITES_FOLDER.joinpath("mineClicked.png"))
    ONE = pygame.image.load(SPRITES_FOLDER.joinpath("grid1.png"))
    TWO = pygame.image.load(SPRITES_FOLDER.joinpath("grid2.png"))
    THREE = pygame.image.load(SPRITES_FOLDER.joinpath("grid3.png"))
    FOUR = pygame.image.load(SPRITES_FOLDER.joinpath("grid4.png"))
    FIVE = pygame.image.load(SPRITES_FOLDER.joinpath("grid5.png"))
    SIX = pygame.image.load(SPRITES_FOLDER.joinpath("grid6.png"))
    SEVEN = pygame.image.load(SPRITES_FOLDER.joinpath("grid7.png"))
    EIGHT = pygame.image.load(SPRITES_FOLDER.joinpath("grid8.png"))
    FLAG = pygame.image.load(SPRITES_FOLDER.joinpath("flag.png"))


SQUARE_CORRESPONDENCE = {
    0: Square.EMPTY,
    1: Square.ONE,
    2: Square.TWO,
    3: Square.THREE,
    4: Square.FOUR,
    5: Square.FIVE,
    6: Square.SIX,
    7: Square.SEVEN,
    8: Square.EIGHT,
}