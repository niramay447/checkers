import pygame
from .constants import *
class Board:
  def __init__(self):
    self.board = []
    self.selectedPiece=NotImplemented
    self.remainingRed = 12
    self.remainingWhite = 12
    self.redKings = 0
    self.whiteKings = 0

  def drawSquare(self,window):
    window.fill(BLACK)
    for i in range(ROWS):
      for j in range(i%2,ROWS,2):
        pygame.draw.rect(window,WHITE,(i*BOARD_SQUARE_SIZE,j*BOARD_SQUARE_SIZE,BOARD_SQUARE_SIZE,BOARD_SQUARE_SIZE))

  def drawBoard(self):
    pass