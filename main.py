from random import randrange
from tkinter import Tk
import chess
from GUI import GUI
from tkinter import messagebox

class Game:

    ROOT = Tk()
    ROOT.title("SearchRed")
    BOARD = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    MYCOLLOR = None
    MACHINECOLLOR = None
    #luot choi
    SLOT = [True]

    #khoi tao giao dien, luot choi
    def __init__(self):
        self.chooseCollor()
        self.display = GUI(self.ROOT, self.BOARD, self.SLOT, self.MYCOLLOR)
        self.display.pack()

    def chooseCollor(self):
        #chon mau quan
        rad = randrange(1, 3)
        #messagebox.showinfo("random", str(rad))
        if rad == 1:
            self.MACHINECOLLOR = chess.WHITE
            self.MYCOLLOR = chess.BLACK
            self.SLOT[0] = False
        else:
            self.MACHINECOLLOR = chess.BLACK
            self.MYCOLLOR = chess.WHITE
            self.SLOT[0] = True
    def start(self):
        self.ROOT.mainloop()

game = Game()
game.start()