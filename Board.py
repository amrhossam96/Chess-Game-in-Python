from Piece import *
from Player import *
from Cell import *

class Board(object):
    def __init__(self,white,black):
        self.white = white
        self.black = black
        self.colIndex = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7}
        self.listOfCells = [["-","-","-","-","-","-","-","-"]
        ,["-","-","-","-","-","-","-","-"],["-","-","-","-","-","-","-","-"]
        ,["-","-","-","-","-","-","-","-"],["-","-","-","-","-","-","-","-"]
        ,["-","-","-","-","-","-","-","-"],["-","-","-","-","-","-","-","-"]
        ,["-","-","-","-","-","-","-","-"]]
        self.addCells()
        self.addItemsToCells()


    def getColIndex(self,colIndex):
        return self.colIndex[colIndex]

    def addCells(self):
        for i in range(0,8):
            for j in range(0,8):
                self.listOfCells[i][j] = Cell(i,j,True,None)


    def addItemsToCells(self):

        #add the white pieces to cells
        for eachPiece in self.white.listOfPieces:
            row,col = eachPiece.getRow(),eachPiece.getCol()
            self.listOfCells[row][col].add_piece(eachPiece)
        #add the black pieces to cells
        for eachPiece in self.black.listOfPieces:
            row,col = eachPiece.getRow(),eachPiece.getCol()
            self.listOfCells[row][col].add_piece(eachPiece)

    def show(self):
        # Printing the board of the game but reversed not by the same sequence of the list of cells
        for r in range(len(self.listOfCells)-1,-1,-1):
            print(str(r+1),end=" ")
            # for c in range(len(self.listOfCells)-1,-1,-1):
            print("|",end="")
            for c in range(0,8):
                if(not(self.listOfCells[r][c].get_piece()) == None):
                    print(self.listOfCells[r][c].get_piece().getdNom()+"  |",end="")

                else:
                    print(" -  ",end=" |")
            if(r == 7):
                print("    p for pawn",end=" ")
            elif(r == 6):
                print("    r for rook",end=" ")
            elif(r == 5):
                print("    k# for knight",end=" ")
            print("")
            print("  _________________________________________________")
        print("    A     B     C     D     E     F     G     H")
