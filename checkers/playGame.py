import pygame
from .board import *
from .constants import *
class PlayGame:
    def __init__(self,window):
        self.selectedMan = None
        self.checkerBoard = Board()
        self.whoseTurn=RED
        self.moveChoices ={}
        self.window=window

    def refresh(self):
        self.checkerBoard.drawBoard(self.window)
        self.highlightPotentialNextMoves(self.moveChoices)
        pygame.display.update()

    def selectMan(self,row,column):
        if self.selectedMan:
            nextPotentialMove = self._moveSelectedMan(row,column)
            if not nextPotentialMove:
                self.selectedMan=None
                self.selectMan(row,column)
        man=self.checkerBoard.getMan(row,column)
        if man!=0 and man.colour == self.whoseTurn:
            self.selectedMan=man
            self.moveChoices=self.checkerBoard.getPotentialNextMoves(man)
            return True

        return False

    def _moveSelectedMan(self,row,column):
        man = self.checkerBoard.getMan(row,column)
        if self.selectedMan and man==0 and (row,column)in self.moveChoices:
            self.checkerBoard.makeMove(self.selectedMan,row,column)
            skippedMan = self.moveChoices[(row,column)]
            if skippedMan:
                self.checkerBoard.removeManFromBoard(skippedMan)
            self.switchTurn()
        else:
            return False
        return True

    def switchTurn(self):
        self.moveChoices={}
        if self.whoseTurn==BLUE:
            self.whoseTurn=RED
        else:
            self.whoseTurn=BLUE

    def highlightPotentialNextMoves(self,potentialMoves):
        for _ in  potentialMoves:
            row,column= _
            x=column*BOARD_SQUARE_SIZE+BOARD_SQUARE_SIZE//2
            y=row*BOARD_SQUARE_SIZE+BOARD_SQUARE_SIZE//2
            pygame.draw.circle(self.window,REDHIGHLIGHT,(x,y),20)