import pygame
from .constants import *
from .men import *
class Board:
  def __init__(self):
    self.board = []
    self.selectedPiece=NotImplemented
    self.remainingRed = 12
    self.remainingWhite = 12
    self.redKings = 0
    self.whiteKings = 0
    self.initialseBoard()

  def drawSquare(self,window):
    window.fill(BLACK)
    for i in range(TOTAL_ROWS):
      for j in range(i%2,TOTAL_COLUMNS,2):
        pygame.draw.rect(window,WHITE,(i*BOARD_SQUARE_SIZE,j*BOARD_SQUARE_SIZE,BOARD_SQUARE_SIZE,BOARD_SQUARE_SIZE))

  def initialseBoard(self):
    for i in range(TOTAL_ROWS):
      self.board.append([])
      for j in range(TOTAL_COLUMNS):
        if j%2==(i+1)%2:
          if i<3:
            self.board[i].append(Men(i,j,BLUE))
          elif i>4:
            self.board[i].append(Men(i,j,RED))
          else:
            self.board[i].append(0)
        else:
          self.board[i].append(0)

  def drawBoard(self,window):
    self.drawSquare(window)
    for i in range(TOTAL_ROWS):
      for j in range(TOTAL_COLUMNS):
        man = self.board[i][j]
        if man!= 0: man.draw(window)
