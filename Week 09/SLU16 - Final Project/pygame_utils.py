"""
    YOU ARE NOT SUPPOSED TO DO CHANGES TO THIS FILE.
    DO THE CHANGES AT YOUR OWN RISK. IT WOULD BE HARD TO THE INSTRUCTORS
    TO PROVIDE SUPPORT ON THE CONTENT OF THIS FILE
"""
import pygame

from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    WHITE,
    BLACK,
    SQUARE_SIZE,
)
from mines import MinesweeperGame


def get_event() -> pygame.event:
    return pygame.event.poll()


def set_up_screen(width: int = SCREEN_WIDTH, height: int = SCREEN_HEIGHT) -> pygame.Surface:
    """
    This function is responsable by initiate the screen.
    It creates the window and setup the background.
    :param width: windown width
    :param height: window height
    """
    pygame.init()
    pygame.display.set_caption('Minesweeper')
    pygame.time.Clock()
    screen = pygame.display.set_mode((width, height))
    screen.fill(WHITE)
    pygame.display.flip()
    return screen


def draw_minesweeper_game(screen: pygame.Surface, mines: MinesweeperGame) -> None:
    """
    It draws the game on the screen.
    :param screen: The screen where the game will appear
    :param mines: The minesweeper game object
    """
    screen.fill(WHITE)
    height = 0
    for line_grid in mines.revealed:
        width = 0
        for square in line_grid:
            pos = (width, height)
            screen.blit(
                square.value,
                pygame.Rect(pos, (SQUARE_SIZE, SQUARE_SIZE))
            )
            width += SQUARE_SIZE
        height += SQUARE_SIZE
    pygame.display.flip()


def show_message(screen: pygame.Surface, message: str) -> None:
    """
    It shows the specified message on the screen.
    :param screen: Pygame.Surface where the message will appear
    :param message: String message to show on the screen.
    """
    # Prepare the Text
    font = pygame.font.Font(None, 36)
    text = font.render(message, True, BLACK, WHITE)
    text_rect = text.get_rect()
    # Center the text on the screen
    text_x = screen.get_width() / 2 - text_rect.width / 2
    text_y = screen.get_height() / 2 - text_rect.height / 2
    # Show the text
    screen.blit(text, [text_x, text_y])
    pygame.display.flip()