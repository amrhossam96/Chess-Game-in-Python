from Board import *
from Player import *
from Piece import *
import os

firstNumber = 1
isInvalidInput = False
PROMT = "select a piece to move\n"
def main():
    firstName = input("enter the name of the first player\n")
    secondName = input("enter the name of the second player\n")
    os.system("cls")
    first = Player(firstName,"white") #initializing first player
    second = Player(secondName,"black") #initializing second player
    board = Board(first,second) #initizaling board
    first.setPlayingBoard(board) #set the table for the first player
    second.setPlayingBoard(board) #set the table for the second player
    first.setOpponent(second)
    second.setOpponent(first)
    playerToPlay = first #specify which player to begin first
    otherPlayer = second #specify which player to play second (reverts each round)

    def play():

        global firstNumber
        global playerToPlay
        global otherPlayer
        if(firstNumber == 1):
            playerToPlay = first
            otherPlayer = second
        else:
            playerToPlay = second
            otherPlayer = first
        userInput = input("\n{} {}".format(playerToPlay.getPlayerName(),PROMT))
        playerToPlay.movePiece(userInput)
        firstNumber = firstNumber * -1

    while True:
        board.show()
        play()
        os.system("cls")
if __name__ == "__main__":
    main()
