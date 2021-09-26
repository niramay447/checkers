import pygame
from checkers.constants import *
from checkers.board import *
WINDOW  = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("CHECKERS")
FPS = 60
def main():
  run = True
  frameRate = pygame.time.Clock()
  checkerBoard = Board()
  while run:
    frameRate.tick(FPS)

    for _ in pygame.event.get():

      if _.type == pygame.QUIT:
        run = False

      if _.type == pygame.MOUSEBUTTONDOWN:
        pass

    checkerBoard.drawBoard(WINDOW)
    pygame.display.update()
  pygame.quit()

main()