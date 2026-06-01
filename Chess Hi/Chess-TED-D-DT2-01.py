import sys
sys.path.append("C:/Users/XxGho/OneDrive/Chess/Chess_Classes.py")
from Chess_Classes import *
Window.title("Awesome Chess")
NewBoard = Board(8,8)
NewBoard.Generate()
Colour = "white"
z = 0
for i in range(1,7,5):
    Colour = "white"
    if i == 6:
        Colour = "black"
    for x in range(0,8):
        Pawn = Piece("Pawn",[i,x],True,[i,x],[i,x],Colour,z)
        Pawn.Generate()
        z += 1
for i in range(0,8,7):
    Colour = "white"
    if i == 7:
        Colour = "black"
    for x in range(0,8,7):
        Rook = Piece("Rook",[i,x],True,[i,x],[i,x],Colour,z)
        Rook.Generate()
        z += 1
for i in range(0,8,7):
    Colour = "white"
    if i == 7:
        Colour = "black"
    for x in range(1,8,5):
        Knight = Piece("Knight",[i,x],True,[i,x],[i,x],Colour,z)
        Knight.Generate()
        z += 1
for i in range(0,8,7):
    Colour = "white"
    if i == 7:
        Colour = "black"
    for x in range(2,8,3):
        Bishop = Piece("Bishop",[i,x],True,[i,x],[i,x],Colour,z)
        Bishop.Generate()
        z += 1
for i in range(0,8,7):
    Colour = "white"
    x = 3
    y = x + 1
    if i == 7:
        Colour = "black"
        x = 4
        y = x - 1
    King = Piece("King",[i,x],True,[i,x],[i,x],Colour,z)
    King.Generate()
    z += 1
    Queen = Piece("Queen",[i,y],True,[i,y],[i,x],Colour,z)
    Queen.Generate()
    z += 1
Window.mainloop()
