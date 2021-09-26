from .constants import *
class Men:
    PADDING=15
    BORDER=5
    def __init__(self,row,column,colour):
        self.row= row
        self.column=column
        self.colour=colour
        self.isKing=False
        self.moveDirection=-1 if self.colour==RED else 1
        self.x=0
        self.y=0
        self.getPosition()
    def getPosition(self):
        self.x=BOARD_SQUARE_SIZE*self.column+BOARD_SQUARE_SIZE//2
        self.y=BOARD_SQUARE_SIZE*self.column+BOARD_SQUARE_SIZE//2
    def changeToKing(self):
        self.isKing=True
    def draw(self,window):
        pieceRadius=BOARD_SQUARE_SIZE//2-self.PADDING
        pygame.draw.circle(window, GREY, (self.x, self.y), pieceRadius + self.OUTLINE)
        pygame.draw.circle(window,self.colour,(self.x,self.y),pieceRadius)


