from tkinter import Button, Label
import chess
import tkinter
import time

turns=0 #tracks amount of turns (even number means its whites turn)
gameend = False
class square(Button): #just an expansion of the tkinter button class
    def setinfo(self,ide,color):
        self.ide = ide
        self.color = color

start=time.time() #start time used to elapsed time
selection = [] #the selected squares (used for moves)
selstr ="" #string representation of move
def sel(event):
    global turns
    if not gameend:
        if event.widget.cget("text")=="" and len(selection)==0:
            return
        selection.append(event.widget)
        if len(selection)==1:
            selection[0].config(background="#b30000")
        elif len(selection)==2:
            selection[0].config(background=selection[0].color)
            selstr = "".join(map(lambda x: x.ide,selection))
            selection.clear()
            b1 = getBoard()

            move2(selstr)
            b2=getBoard()
            if b1!=b2:
                turns+=1
            info.config(text=f"{("Santa","The Grinch")[turns%2]}'s Turn  -   Seconds Elapsed: {round(time.time()-start)}s") #updates info


def getBoard():#returns a 2d list that represents the current board
    #each list in the lists represent different rows
    #each item in the lists represent different spacecs in the row
    b = str(board).split('\n')
    for ii,i in enumerate(b):
        b[ii]=i.split()
    return b

def updateScreen():
    #updates the game screen
    global gameend
    for r in range(8):
        for c in range(8):
            piece = getBoard()[r][c]
            pieceInfo = {".":("","black"),
                         "r": ("♜", "#003d00"),
                         "n": ("♞", "#003d00"),
                         "b": ("♝", "#003d00"),
                         "q": ("♛", "#003d00"),
                         "k": ("♚", "#003d00"),
                         "p": ("♟", "#003d00"),
                         "R": ("♜", "#ff4f4f"),
                         "N": ("♞", "#ff4f4f"),
                         "B": ("♝", "#ff4f4f"),
                         "Q": ("♛", "#ff4f4f"),
                         "K": ("♚", "#ff4f4f"),
                         "P": ("♟", "#ff4f4f")
                         }.get(piece)
            bd[r][c].config(text=pieceInfo[0])
            bd[r][c].config(foreground=pieceInfo[1])
    if board.is_checkmate():
        print(f"\nCheckmate - {("Santa","The Grinch")[(turns)%2]} Won")
        w.quit()
        gameend=True
    if board.is_stalemate():
        print("Stalemate")
        w.quit()
        gameend = True


def move2(move): #second version of movement function (old one delted)
    for i in board.legal_moves:
        if move==str(i):
            board.push_san(move)
            updateScreen()
            break

w = tkinter.Tk()
w.geometry('536x530')


bd = []
for i in range(8):
    row = []
    for ii in range(8):
        col = "#a6322e" if (i+ii)%2==0 else "#64b066"
        tex =""
        if i in (0,7):
            tex = ("♜","♞","♝","♛","♚","♝","♞","♜")[ii]
        elif i in (1,6):
            tex = "♟"

        sq = square(width = 3,
                    height=1,
                    background=col,
                    foreground=("#003d00" if i<=1 else "#ff4f4f"),
                    text=tex,
                    font=("Arial",24),
                    relief="sunken")
        sq.setinfo(("a","b","c","d","e","f","g","h")[ii]+str(8-i),col)
        sq.bind('<Button-1>',sel)
        row.append(sq)

    bd.append(row)

for i in range(8):
    for ii in range(8):
        bd[i][ii].grid(column=ii,
                       row=i)
board = chess.Board() #defines board
info =Label(w,text="Santa's turn  -   Seconds Elapsed: 0s",font=("Courier",15),foreground="#003d00")
info.grid(row=8,
          column=0,
          columnspan=8,
          rowspan=3)
w.resizable(width=False,
            height=False)
w.iconbitmap("horsey.ico")
w.title("Christmas Chess: The Siege of Whoville")#defines title




w.mainloop()