import pygame
from .constants import *
from .men import *


class Board:
    def __init__(self):
        self.board = []

        self.remainingRed = 12
        self.remainingWhite = 12
        self.redKings = 0
        self.blueKings = 0
        self.initialseBoard()

    def drawSquare(self, window):
        window.fill(BLACK)
        for i in range(TOTAL_ROWS):
            for j in range(i % 2, TOTAL_COLUMNS, 2):
                pygame.draw.rect(window, WHITE,
                                 (i * BOARD_SQUARE_SIZE, j * BOARD_SQUARE_SIZE, BOARD_SQUARE_SIZE, BOARD_SQUARE_SIZE))

    def initialseBoard(self):
        for i in range(TOTAL_ROWS):
            self.board.append([])
            for j in range(TOTAL_COLUMNS):
                if j % 2 == (i + 1) % 2:
                    if i < 3:
                        self.board[i].append(Men(i, j, BLUE))
                    elif i > 4:
                        self.board[i].append(Men(i, j, RED))
                    else:
                        self.board[i].append(0)
                else:
                    self.board[i].append(0)

    def drawBoard(self, window):
        self.drawSquare(window)
        for i in range(TOTAL_ROWS):
            for j in range(TOTAL_COLUMNS):
                man = self.board[i][j]
                if man != 0: man.draw(window)

    def makeMove(self, man, row, column):
        self.board[man.row][man.column], self.board[row][column] = self.board[row][column], self.board[man.row][
            man.column]
        man.move(row, column)

        if row == TOTAL_ROWS-1 or row == 0:
            man.changeToKing()
            if man.colour == RED:
                self.redKings += 1
            else:
                self.blueKings += 1

    def getMan(self, row, column):
        return self.board[row][column]

    def removeManFromBoard(self,men):
        for man in men:
            self.board[man.row][man.column]=0

    def getPotentialNextMoves(self, man):
        validNextMoves = {}
        west = man.column-1
        east = man.column+1
        row = man.row

        if man.colour == RED or man.isKing:
            validNextMoves.update(self.moveWest(row - 1, max(row - 3, -1), -1, man.colour, west))
            validNextMoves.update(self.moveEast(row - 1, max(row - 3, -1), -1, man.colour, east))
        if man.colour == BLUE or man.isKing:
            validNextMoves.update(self.moveWest(row + 1, min(row + 3, TOTAL_ROWS), 1, man.colour, west))
            validNextMoves.update(self.moveEast(row + 1, max(row + 3, TOTAL_ROWS), 1, man.colour, east))

        return validNextMoves

    def moveWest(self, initial, final, step, colour, west, skippedMen=[]):
        validNextMoves = {}
        last = []
        for i in range(initial, final, step):
            if west < 0:
                break

            cur = self.board[i][west]
            if cur == 0:
                if skippedMen and not last:
                    break
                elif skippedMen:
                    validNextMoves[(i, west)] = last + skippedMen
                else:
                    validNextMoves[(i, west)] = last

                if last:
                    if step == -1:
                        row = max(i - 3, 0)
                    else:
                        row = min(i + 3, TOTAL_ROWS)

                    validNextMoves.update(self.moveWest(i + step, row, step, colour, west - 1, skippedMen=last))
                    validNextMoves.update(self.moveEast(i + step, row, step, colour, west + 1, skippedMen=last))
                break
            elif cur.colour == colour:
                break
            else:
                last = [cur]
            west -= 1

        return validNextMoves

    def moveEast(self, initial, final, step, colour, east, skippedMen=[]):
        validNextMoves = {}
        last = []
        for i in range(initial, final, step):
            if east >= TOTAL_COLUMNS:
                break

            cur = self.board[i][east]
            if cur == 0:
                if skippedMen and not last:
                    break
                elif skippedMen:
                    validNextMoves[(i, east)] = last + skippedMen
                else:
                    validNextMoves[(i, east)] = last

                if last:
                    if step == -1:
                        row = max(i - 3, 0)
                    else:
                        row = min(i + 3, TOTAL_ROWS)

                    validNextMoves.update(self.moveWest(i + step, row, step, colour, east - 1, skippedMen=last))
                    validNextMoves.update(self.moveEast(i + step, row, step, colour, east + 1, skippedMen=last))
                break
            elif cur.colour == colour:
                break
            else:
                last = [cur]
            east += 1

        return validNextMoves

