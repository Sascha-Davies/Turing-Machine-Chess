from tkinter import *
from functools import partial
Window = Tk()
GridPos = {}
Tiles = []
TilesColour = []
EnableGrid = []
Pieces = []
Enable = []
Positions = []
class Board():
    def __init__ (self,Length,Height):
        self.Length = Length
        self.Height = Height
    def Generate(self):
        global GridPos,Tiles,TilesColour
        z = 0
        for i in range (0,self.Height):
            for x in range(0,self.Length):
                z = z+1
                if i%2 == 0:
                    if x%2 == 0:  
                        Colour = "black"
                    else:
                        Colour = "tan"
                else:
                    if x%2 == 0:
                        Colour = "tan"
                    else:
                        Colour = "black"
                GridPos[z] = [i,x]
                Grid = Button(Window,height = 7,width = 14,bg = Colour,state = "disabled")
                Tiles += [Grid]
                TilesColour += [Colour]
                Grid.grid(row = i,column = x)
class Piece():
    def __init__ (self,Type,Start,State,Position,PrevPosition,Colour,ID):
        self.Type = Type
        self.Colour = Colour
        self.Start = Start
        self.State = True
        self.Position = Position
        self.id = ID
        self.PrevPosition = PrevPosition
    def Generate(self):
        global Pieces
        global Positions
        Piece = Button(Window,text = self.Type,bg = self.Colour,fg = "grey",command = partial(Moving,self.Type,self.Position,GridPos,self.Start,self.Colour,self.id),height = 3,width = 9,)
        Pieces += [Piece]
        self.id = len(Pieces)
        Piece.grid(row = self.Start[0],column = self.Start[1])
        Positions.append(self.Start)
    def Move(self):
        global Pieces
        global Positions
        self.id = len(Pieces)
        Piece = Button(Window,text = self.Type,bg = self.Colour,fg = "grey",command = partial(Moving,self.Type,self.Position,GridPos,self.Start,self.Colour,self.id),height = 3,width = 9)
        Pieces += [Piece]
        Piece.grid(row = self.Position[0],column = self.Position[1])
        Positions.append(self.Position)
        Positions.remove(self.PrevPosition)
        #print(self.id)
        return Piece
    def Position(self):
        Id = self.id
        return Id
    def Take(self,P):
        global Positions
        global Pieces
        #print(I)
        self.destroy()
        Positions.remove(P)
def Moving(Type,PiecePosition,GridPositions,Start,Colour,ID):
    global EnableGrid
    EnableGrid = []
    Colour = ""
    z = []
    for i in range(1,len(GridPositions)+1):
        if Type == "Pawn":
            if Start[0] <= 1:
                if GridPositions[i][0] - PiecePosition[0] == 1 and GridPositions[i][1] == PiecePosition[1]:
                    EnableGrid.append(GridPositions[i])
                    z += [i-1]
                    Colour = "white"
            else:
                if PiecePosition[0] - GridPositions[i][0] == 1 and GridPositions[i][1] == PiecePosition[1]: 
                    EnableGrid.append(GridPositions[i])
                    z += [i-1]
                    Colour = "black"
        if Type == "Rook":
            if ((GridPositions[i][0] - PiecePosition[0] == 0) or GridPositions[i][1] == PiecePosition[1]):
                if GridPositions[i] != PiecePosition:
                    EnableGrid.append(GridPositions[i])
                    z += [i-1]
                    if Start[0] <= 1:
                        Colour = "white"
                    else:
                        Colour = "black"
        if Type == "Knight":
            if((PiecePosition[0] - GridPositions[i][0] >= 1 and PiecePosition[0] - GridPositions[i][0] <= 2) or (PiecePosition[0] - GridPositions[i][0] <= -1 and PiecePosition[0] - GridPositions[i][0] >= -2)) and ((PiecePosition[1] - GridPositions[i][1] >= 1 and PiecePosition[1] - GridPositions[i][1] <= 2) or (PiecePosition[1] - GridPositions[i][1] <= -1 and PiecePosition[1] - GridPositions[i][1] >= -2)) and not(PiecePosition[0] - GridPositions[i][0] == PiecePosition[1] - GridPositions[i][1] or -GridPositions[i][0] + PiecePosition[0] == GridPositions[i][1] - PiecePosition[1]):
                if GridPositions[i] != PiecePosition:
                    EnableGrid.append(GridPositions[i])
                    z += [i-1]
                    if Start[0] <= 1:
                        Colour = "white"
                    else:
                        Colour = "black"
        if Type == "Bishop":
            if not((GridPositions[i][0] - PiecePosition[0] == 0) or GridPositions[i][1] == PiecePosition[1]) and (PiecePosition[0] - GridPositions[i][0] == PiecePosition[1] - GridPositions[i][1] or -GridPositions[i][0] + PiecePosition[0] == GridPositions[i][1] - PiecePosition[1]):
                if GridPositions[i] != PiecePosition:
                    EnableGrid.append(GridPositions[i])
                    z += [i-1]
                    if Start[0] <= 1:
                        Colour = "white"
                    else:
                        Colour = "black"
        if Type == "Queen":
            if ((GridPositions[i][0] - PiecePosition[0] == 0) or GridPositions[i][1] == PiecePosition[1]) or (PiecePosition[0] - GridPositions[i][0] == PiecePosition[1] - GridPositions[i][1] or -GridPositions[i][0] + PiecePosition[0] == GridPositions[i][1] - PiecePosition[1]) :
                if GridPositions[i] != PiecePosition:
                    EnableGrid.append(GridPositions[i])
                    z += [i-1]
                    if Start[0] <= 1:
                        Colour = "white"
                    else:
                        Colour = "black"
        if Type == "King":
            if ((GridPositions[i][0] - PiecePosition[0] == 0) or GridPositions[i][1] == PiecePosition[1]) and ((PiecePosition[0] - GridPositions[i][0] == 1 or GridPositions[i][0] - PiecePosition[0] == 1) or (PiecePosition[1] - GridPositions[i][1] == 1 or GridPositions[i][1] - PiecePosition[1] == 1)) or (PiecePosition[0] - GridPositions[i][0] == 1 or GridPositions[i][0] - PiecePosition[0] == 1 or PiecePosition[0] - GridPositions[i][0] == PiecePosition[1] - GridPositions[i][1]) and (PiecePosition[1] - GridPositions[i][1] == 1 or GridPositions[i][1] - PiecePosition[1] == 1 or -GridPositions[i][0] + PiecePosition[0] == GridPositions[i][1] - PiecePosition[1]):
                if GridPositions[i] != PiecePosition:
                    EnableGrid.append(GridPositions[i])
                    z += [i-1]
                    if Start[0] <= 1:
                        Colour = "white"
                    else:
                        Colour = "black"
    #print("Starting Pos",Start)
    Enable(Tiles,z,PiecePosition,Type,Colour,EnableGrid,ID,Start)
def Enable(Tiles,z,PiecePosition,Type,Colour,EnableGrid,ID,Start):
    global GridPos
    global Positions
    Occupation = []
    f = 0
    PositionsT = Positions
    for i in range(0,len(EnableGrid)):
        #print("Enable",EnableGrid[i])
        for x in range(0,len(Positions)):
            #print("Pos",Positions[x])
            if EnableGrid[i] == Positions[x]:
                Occupied = True
                Occupation.append(EnableGrid[i])
                state = "disabled"
                break
            else:
                f = i
                Occupied = False
                state = "normal"
        if Occupied == False:
            Colours = "lime green"
        else:
            Colours = "red"
        Tiles[z[i]].config(state = "normal",bg = Colours,command = partial(Movement,EnableGrid,PiecePosition,Type,Colour,Tiles,z,ID,Start,f))
def Movement(EnableGrid,PiecePosition,Type,Colour,Tiles,z,ID,Start,f):
    global Pieces,GridPos,TilesColour,Positions
    Occupied = False
    for i in range(0,len(Positions)):
        pass
    PieceMove = Piece(Type,Start,True,EnableGrid[f],PiecePosition,Colour,ID)
    for i in range (0,len(Positions)):
        if EnableGrid[f] == Positions[i]:
            print(Positions)
            P = Positions[i]
            j = i
            print(j)
            print(P)
            print(Type.Position(Pieces[j]))
            #print(Id)
            Occupied = True
    PieceMove.Move()
    Pieces[ID].destroy()
    for i in range(0,len(EnableGrid)):
        Tiles[z[i]].config(state = "disabled",bg = TilesColour[z[i]])
    if Occupied == True:
        Piece.Take(Pieces[j],P)
def Take(Type,PiecePosition,EnableGrid,Occupied,ID):
    if Occupied == True:
        print(Pieces)
        Piece.Take(Pieces[j],Positions[i])
    pass
