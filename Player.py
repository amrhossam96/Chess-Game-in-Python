from Piece import *

import os

class Player(object):


    def __init__(self,name,color):

        self.name = name
        self.color = color
        self.listOfPieces = [] #a list containing all the pieces the player has
        self.pieceKeys = {} # a dict which returns the piece based on it's nom
        self.listOfNoms = ["k","q","r2","r1","k1","b1","k2"
        ,"b2","p1","p2","p3","p4","p5","p6","p7","p8"] #list of the noms of the pieces
        self.addition1 = 0
        self.addition2 = 0
        self.board = None
        self.isBad = True
        self.init = "w"
        self.opponent = None
        self.king = self.queen = self.rook1 = self.rook2 = self.bishop1 = self.bishop2 = self.knight1 = self.knight2 = self.pawn1 = self.pawn2 = self.pawn3 = self.pawn4 = self.pawn5 = self.pawn6 = self.pawn7 = self.pawn8 = None
        self.build_deck()
        self.assignPieceByName()

        #Adding items to player list as objects...
    def build_deck(self):

        if(self.color == "black"):
            self.addition1 = 7
            self.addition2 = 5
            self.init = "b"
        #Initizaling the pieces for each player

        self.king = Piece(self.color,"king",0+self.addition1,4,"k ",self,self.init+"k ")#0
        self.queen = Piece(self.color,"queen",0+self.addition1,3,"q ",self,self.init+"q ")#1
        self.rook2 = Piece(self.color,"rook",0+self.addition1,7,"r2",self,self.init+"r2")#3
        self.rook1 = Piece(self.color,"rook",0+self.addition1,0,"r1",self,self.init+"r1")#2
        self.knight1 = Piece(self.color,"knight",0+self.addition1,1,"k1",self,self.init+"k1")#4
        self.bishop1 = Piece(self.color,"bishop",0+self.addition1,2,"b1",self,self.init+"b1")#6
        self.knight2 = Piece(self.color,"knight",0+self.addition1,6,"k2",self,self.init+"k2")#5
        self.bishop2 = Piece(self.color,"bishop",0+self.addition1,5,"b2",self,self.init+"b2")#7
        self.pawn1 = Piece(self.color,"pawn",1+self.addition2,0,"p1",self,self.init+"p1")#8
        self.pawn2 = Piece(self.color,"pawn",1+self.addition2,1,"p2",self,self.init+"p2")#9
        self.pawn3 = Piece(self.color,"pawn",1+self.addition2,2,"p3",self,self.init+"p3")#10
        self.pawn4 = Piece(self.color,"pawn",1+self.addition2,3,"p4",self,self.init+"p4")#11
        self.pawn5 = Piece(self.color,"pawn",1+self.addition2,4,"p5",self,self.init+"p5")#12
        self.pawn6 = Piece(self.color,"pawn",1+self.addition2,5,"p6",self,self.init+"p6")#13
        self.pawn7 = Piece(self.color,"pawn",1+self.addition2,6,"p7",self,self.init+"p7")#14
        self.pawn8 = Piece(self.color,"pawn",1+self.addition2,7,"p8",self,self.init+"p8")#15
        #Adding items to the list of each player

        self.listOfPieces.extend((self.king,self.queen,self.rook2
        ,self.rook1,self.knight1,self.bishop1
        ,self.knight2,self.bishop2
        ,self.pawn1,self.pawn2,self.pawn3
        ,self.pawn4,self.pawn5,self.pawn6
        ,self.pawn7,self.pawn8))


    def assignPieceByName(self):
        i = 0
        for piece in self.listOfNoms:
            self.pieceKeys[piece] = self.listOfPieces[i]
            i = i+1


    def getmyDict(self):
        return self.pieceKeys

    def getPlayerName(self):
        return self.name

    def getPlayerColor(self):
        return self.color

    def getPieceIndex(self,pieceName):
        return self.item_keys[pieceName]

    def show_list(self):
        for i in range(0,len(self.listOfPieces)):
            self.listOfPieces[i].showInfo()

    def movePiece(self,piece):
        selectedPiece = self.pieceKeys[piece]
        #ph = PieceMovesHelper(self.board)
        #availableMoves = ph.getPieceMoves(selectedPiece,self)
        #print(availableMoves)


        row = int(input("enter Row\n"))-1
        col = self.board.getColIndex(input("enter Col\n").upper())


        celltobeChecked = self.board.listOfCells[row][col]
        if(not celltobeChecked.get_piece() == None):
            if(self.getPlayerName() == celltobeChecked.get_piece().getPieceOwner().getPlayerName()):
                print("Can't eat from your self")
                self.movePiece(piece)
            else:
                self.opponent.listOfPieces.remove(celltobeChecked.get_piece())
                self.board.listOfCells[selectedPiece.getRow()][selectedPiece.getCol()].remove_piece()
                selectedPiece.setRow(row)
                selectedPiece.setCol(col)
                self.board.addItemsToCells()
        else:
            self.board.listOfCells[selectedPiece.getRow()][selectedPiece.getCol()].remove_piece()
            selectedPiece.setRow(row)
            selectedPiece.setCol(col)
            self.board.addItemsToCells()


    def setPlayingBoard(self,board):
        self.board = board

    def setOpponent(self,opponent):
        self.opponent = opponent
