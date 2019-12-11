from random import randrange
from tkinter import Tk
import chess
from source.GUI import GUI
from tkinter import messagebox
import  source.AI

class Game:

    ROOT = Tk()
    ROOT.title("SearchRed")
    BOARD = chess.Board()
    #luot choi
    #true la luot nguoi choi, false là lượt máy chơi
    SLOT = [True]

    #khoi tao giao dien, luot choi
    def __init__(self):
        self.display = GUI(self, self.ROOT, self.BOARD, self.SLOT)
        self.display.pack()
    #bắt đầu game
    def start(self):
        if(self.SLOT[0] == False):
            self.AIplay()
        self.ROOT.mainloop()

    #máy chơi
    def AIplay(self):
        #kiểm tra kết thuc ván đấu bao gồm thắng, thua, hòa
        if(self.BOARD.is_checkmate()):
            #cap nhat trạng thái ván đấu
            messagebox.showwarning("End game", "You win")
            self.display.canvas.delete("status")
            self.display.canvas.create_text(20, 220, anchor='w', font="VNI-Dom 14",
                                            text="Status board: Your win", tag="status")
        elif(self.BOARD.is_stalemate() or self.BOARD.can_claim_threefold_repetition() or self.BOARD.is_insufficient_material() or self.BOARD.is_fivefold_repetition()):
            messagebox.showwarning("End game", "Draw")
            self.display.canvas.delete("status")
            self.display.canvas.create_text(20, 220, anchor='w', font="VNI-Dom 14",
                                            text="Status board: Draw", tag="status")
        else:
            #kiem tra co phai luot di cua may
            if(self.SLOT[0] == False):
            #sinh nuoc di vói modul AI với độ sâu 3
                machineMove = source.AI.makeBestMove(3, self.BOARD, True)
                move = chess.Move.from_uci(machineMove)
                self.BOARD.push(move)
                self.display.canvas.delete("move")
                self.display.canvas.create_text(20, 150, anchor='w', font="VNI-Dom 14",
                                        text="Black move: " + str(move), tag="move")
            #print(self.BOARD)
            self.display.draw()

            #kiem tra ket qua van dau sau khi move
            if (self.BOARD.is_checkmate()):
                messagebox.showwarning("End game", "Machine win")
                self.display.canvas.delete("status")
                self.display.canvas.create_text(20, 220, anchor='w', font="VNI-Dom 14",
                                        text="Status board: Machine win", tag="status")
            elif (self.BOARD.is_stalemate() or self.BOARD.can_claim_threefold_repetition() or self.BOARD.is_insufficient_material() or self.BOARD.is_fivefold_repetition()):
                messagebox.showwarning("End game", "Draw")
                self.display.canvas.delete("status")
                self.display.canvas.create_text(20, 220, anchor='w', font="VNI-Dom 14",
                                        text="Status board: Draw", tag="status")
            else:
                self.SLOT[0] = True
                self.display.canvas.delete("status")
                self.display.canvas.create_text(20, 220, anchor='w', font="VNI-Dom 14",
                                        text="Status board: Your turn", tag="status")


#bat dau game
game = Game()
game.start()