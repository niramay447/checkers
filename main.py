import pygame
from checkers.constants import *
from checkers.board import *
from checkers.playGame import *
WINDOW  = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("CHECKERS")
FPS = 60

def getPositionFromClick(clickedPosition):
  x,y=clickedPosition
  row = y//BOARD_SQUARE_SIZE
  column = x//BOARD_SQUARE_SIZE
  return row,column


def main():
  run = True
  frameRate = pygame.time.Clock()
  checkerGame= PlayGame(WINDOW)

  while run:
    frameRate.tick(FPS)

    for _ in pygame.event.get():

      if _.type == pygame.QUIT:
        run = False

      if _.type == pygame.MOUSEBUTTONDOWN:
        position=pygame.mouse.get_pos()
        xVal,yVal=getPositionFromClick(position)

    checkerGame.refresh()
  pygame.quit()

main()