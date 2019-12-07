from random import randrange
from tkinter import Tk
import chess
from GUI import GUI

class Game:

    #luot choi
    PEOPLE = 1
    MACHINE = 2
    SLOT = randrange(1, 2)
    ROOT = Tk()
    BOARD = chess.Board()

    #khoi tao giao dien, luot choi
    def __init__(self):
        self.display = GUI(self.ROOT, self.BOARD, self.SLOT)
    def start(self):
        self.ROOT.mainloop()

game = Game()
game.start()