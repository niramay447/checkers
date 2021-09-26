import pygame
from .board import *
from .constants import *
class PlayGame:
    def __init__(self,window):
        self.selectedPiece = None
        self.checkerBoard = Board()
        self.whoseTurn=RED
        self.moveChoices ={}
        self.window=window

    def refresh(self):
        self.checkerBoard.drawBoard(self.window)
        pygame.display.update()
