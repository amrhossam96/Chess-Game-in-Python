class Piece(object):

    
    def __init__(self,color,suit,row,col,nom,owner,dNom):
        self.color = color
        self.suit = suit
        self.stateAlive = True
        self.row = row
        self.col = col
        self.nom = nom
        self.dNom = dNom
        self.owner = owner
        self.applicableMove = []


    def getPieceOwner(self):
        return self.owner

    def getNom(self):
        return self.nom
    def getdNom(self):
        return self.dNom

    def showInfo(self):
        state = ""
        if(self.stateAlive == True):
            state = "Alive"
        else:
            state = "Dead"
        print("{} of color {}, its nom is:\"{}\" and it is {}".format(self.suit,self.color,self.nom,state))
    #Getters for rows and cols
    def getRow(self):
        return self.row
    def getCol(self):
        return self.col
    #Setters for rows and cols
    def setRow(self,row):
        self.row = row
    def setCol(self,col):
        self.col = col
