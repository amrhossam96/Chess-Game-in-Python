class Cell(object):

    def __init__(self,row,col,isEmpty,piece):
        self.row = row
        self.col = col
        self.isEmpty = isEmpty
        self.piece = piece

    def get_piece(self):
        return self.piece

    def add_piece(self,piece):
        self.piece = piece
        self.isEmpty = False

    def remove_piece(self):
        self.piece = None
        self.isEmpty = True
