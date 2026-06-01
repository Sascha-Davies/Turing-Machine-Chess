from Chess_Classes import *
Window.title("Awesome Chess")
BoardDimensions = 8 #Largest Size without Tile And button being same == 20
NewBoard = Board(BoardDimensions,BoardDimensions,Option)
#KNIGHT MOVES 6 TILES - 9 TILES, 10 TILES - 7 TILES
#NewBoard.Generate()
Check = False
Colour = "white"
count = 0
#Object = {}
def Generate(z):
    global Pieces
    NewBoard.Generate()
    Check = False
    for i in range(1,BoardDimensions-1,BoardDimensions-3):
        Colour = "white"
        if i == BoardDimensions-2:
            Colour = "black"
        for x in range(0,BoardDimensions):
            Pawn = Piece("Pawn",[i,x],True,[i,x],[i,x],Colour,z,0,BoardDimensions,0)
            Pawn.Generate()
            z += 1
    for i in range(0,BoardDimensions,BoardDimensions-1):
        Colour = "white"
        if i == BoardDimensions-1:
            Colour = "black"
        for x in range(0,BoardDimensions,7):
            Rook = Piece("Rook",[i,x],True,[i,x],[i,x],Colour,z,0,BoardDimensions,1)
            Rook.Generate()
            z += 1
    for i in range(0,BoardDimensions,BoardDimensions-1):
        Colour = "white"
        if i == BoardDimensions-1:
            Colour = "black"
        for x in range(1,BoardDimensions,5):
            Knight = Piece("Knight",[i,x],True,[i,x],[i,x],Colour,z,0,BoardDimensions,0)
            Knight.Generate()
            z += 1
    for i in range(0,BoardDimensions,BoardDimensions-1):
        Colour = "white"
        if i == BoardDimensions-1:
            Colour = "black"
        for x in range(2,BoardDimensions,3):
            Bishop = Piece("Bishop",[i,x],True,[i,x],[i,x],Colour,z,0,BoardDimensions,0)
            Bishop.Generate()
            z += 1
    for i in range(0,BoardDimensions,BoardDimensions-1):
        Colour = "white"
        x = BoardDimensions//2-1
        y = x + 1
        if i == BoardDimensions-1:
            Colour = "black"
            x = BoardDimensions//2-1
        King = Piece("King",[i,x],True,[i,x],[i,x],Colour,z,0,BoardDimensions,1)
        King.Generate()
        z += 1
        Queen = Piece("Queen",[i,y],True,[i,y],[i,x],Colour,z,0,BoardDimensions,0)
        Queen.Generate()
        z += 1
    ChessTurn(Pieces)
    if AI == True:
        #print(Pieces)
        Pieces = {}
        #print(Object)
        ChessAI(Pieces,"Select")
    #print(SelectedPiece.Type)
if Played == 0:
    Generate(0)
#print(turn)
#position 1,0 6,0 glitch. doesnt effect black/black tile bishop for odd reasons
#depending on what pawn moves first it can either take or not take in a diagonal situation
