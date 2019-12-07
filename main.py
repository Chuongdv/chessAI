from random import randrange
from tkinter import Tk
import chess
from GUI import GUI

class Game:

    ROOT = Tk()
    ROOT.title("SearchRed")
    BOARD = chess.Board("rnbqkbnr/1ppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    MYCOLLOR = None
    MACHINECOLLOR = None
    #luot choi
    SLOT = [True]

    #khoi tao giao dien, luot choi
    def __init__(self):

        self.display = GUI(self.ROOT, self.BOARD, self.SLOT, self.MYCOLLOR)
        self.display.pack()

    def chooseCollor(self):
        #chon mau quan
        rad = randrange(1, 2)
        if rad == 1:
            self.MACHINECOLLOR = True
            self.MYCOLLOR = False
            self.SLOT[0] = False
        else:
            self.MACHINECOLLOR = True
            self.MACHINECOLLOR =False
            self.SLOT[0] = True
    def start(self):
        self.ROOT.mainloop()

game = Game()
game.start()