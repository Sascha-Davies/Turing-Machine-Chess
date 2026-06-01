from tkinter import *
from functools import partial
from Turing_Machine import *
import random
import sys
#from Chess import Generate
from time import sleep
#MOVEMENT GLITCHES
#fix Obstruction Pieces Should not be able to jump over each other
#Make it so all buttons disable once one is clicked and make turns. Done
#Fix Clone Glitch Fixed
#Fix Invincible glitch for pawn at 1,0 Fixed
#Fix Another Clone Glitch that happens when pawns kill illegally (by killing a piece thats infront of them)
#When pawn reaches end and promotes it can move again even if its the other players go Fixed
#Scale Board and Pieces Done
#Make Turing Machines for Movement Instead of If statements #DONE: ROOK BISHOP Fix Black Bishop and Make sure it doesnt crash, Fix Queen fully at last 2 tiles in a row IF BISHOP AND ASSUMING QUEEN GET BLOCKED BY TEAMATE CANNOT TRAVEL IN THE INVERSE DIAGONAL DIRECTION
# Done: Pawn,Rook,King,Queen,Bishop,Knight
#Queen and Bishop crash if - - and + - directions are blocked Might be something to do with detecting A Fixed
#BISHOP AT TILE 7,5 (LAST BISHOP) CRASHES GAME Fixed
#TRY TO REDUCE STATES BY MAKING LOOP IN THIS SCRIPT
#FIX GLITCH WHERE KNIGHT CAN PHASE TO OTHER SIDE OF BOARD Fixed
#Bottom Corner doesnt work for bishop Fixed
#Movement Complete Can add en passente and Castling
#add K to all Turing Machines
#CHECKMATE
#Identify king for checkmate could be through another character in state machine
#if go this route need to know kings position at all times
#Added Check. CheckMate Comes Later. Check When players in Check and give move suggestions that get out of Check
#Knight Boost Real
# +C
#AbhiBug - Rook Moves when King first moves if available
#if AIhas pawn reach end it needs to trade
#Lots of issues with restarting at the moment - Fix Recursion so it doesnt exceed limit
#sys.setrecursionlimit(999999999)
Object = {}
Window = Tk()
GridPos = {}
Tiles = []
InCheckMoves = []
TilesColour = []
EnableGrid = []
Pieces = {}
Enable = []
MoveSymbols = ["A","Y","F","Q","V"]
BoardSymbols = ["N","X","0","B"]
PieceTypes = {}
EnabledPieces = {}
CastleKeepers = ["~","C","#","A"]
Positions = []
Positionsdict = {}
AI = False
turn = 0 #Actual Turn = turn - 1
ActualTurn = turn - 1
ColourID = {}
KingPositions = {}
Option = "1V1"
Clicked = True
Check = False
z = []
l = []
WhiteWins = 0
BlackWins = 0
Played = 0
#print(Positions,Pieces)
class Board():
    def __init__ (self,Length,Height,Option):
        self.Length = Length
        self.Height = Height
        self.Option = Option
    def Generate(self):
        global GridPos,Tiles,TilesColour
        Tiles = []
        z = 0
        for i in range (0,self.Height):
            for x in range(0,self.Length):
                z = z+1
                if i%2 == 0:
                    if x%2 == 1:
                        Colour = "black" #Colour #950302,Blue
                    else:
                        Colour = "tan"
                else:
                    if x%2 == 1:
                        Colour = "tan"
                    else:
                        Colour = "black"
                GridPos[z] = [i,x]
                #height = 7 width = 14
                if Option == "1V1":
                    Grid = Button(Window,height = 40//self.Height,width = 80//self.Length,bg = Colour,state = "disabled")
                    Tiles += [Grid]
                    TilesColour += [Colour]
                    Grid.grid(row = i,column = x)
        #print(len(Tiles))
        #for x in range(0,self.Height+1):
            #Border = Button(Window,height = 5,width = 10,bg = "brown",state = "disabled")
            #Border.grid(row = self.Height,column = x)
            #Border.grid(row = x, column = self.Height)

                
class Piece():
    def __init__ (self,Type,Start,State,Position,PrevPosition,Colour,ID,Pawnturn,Scale,Castling):
        self.Type = Type
        self.Colour = Colour
        self.Start = Start
        self.State = True
        self.Scale = Scale
        self.Position = Position
        self.id = ID
        self.PrevPosition = PrevPosition
        self.ID = ID
        self.Pawnturn = Pawnturn
        self.Castling = Castling
        #print(self.Castling)
    def Generate(self):
        global Pieces,Positions,GridPos,KingPositions,Option
        #Piece = Button(Window,text = self.Type,bg = self.Colour,fg = "grey",command = partial(Moving,self.Type,self.Position,self.Scale,GridPos,self.Start,self.Colour,self.id,self.ID,self.Pawnturn),height = 24//self.Scale,width = 72//self.Scale,)
        for i in range(1,len(GridPos)+1):
            if self.Position == GridPos[i]:
                self.ID = i
                if self.Type == "King":
                    KingPositions[i] = self.Position
        #print("ID",self.ID)
        #print(KingPositions)
        Piece = Button(Window,text = self.Type,bg = self.Colour,fg = "grey",command = partial(Moving,self.Type,self.Position,self.Scale,GridPos,self.Start,self.Colour,self.ID,self.ID,self.Pawnturn,self.Castling,"",False),height = 24//self.Scale,width = 72//self.Scale,)
        #print(self.ID)
        Object[self.ID] = self
        Pieces[self.ID] = Piece
        #print(Pieces)
        if Option == "1V1":
            Piece.grid(row = self.Start[0],column = self.Start[1])
        Positions.append(self.Start)
        ColourID[self.ID] = self.Colour
        PieceTypes[self.ID] = self.Type
        #print(len(Object))
    def Move(self):
        global Pieces
        global Positions
        self.Pawnturn = 1
        self.id = len(Pieces)
        if self.Type == "King":
            #print(KingPositions)
            #print("Self",self.ID)
            KingPositions.pop(self.ID)
            #print(KingPositions)
        for i in range(1,len(GridPos)+1):
            if self.Position == GridPos[i]:
                self.ID = i
                if self.Type == "King":
                    KingPositions[i] = self.Position
        #print(KingPositions)
        self.Castling -= 1
        #print(self.Type)
        Piece = Button(Window,text = self.Type,bg = self.Colour,fg = "grey",command = partial(Moving,self.Type,self.Position,self.Scale,GridPos,self.Start,self.Colour,self.id,self.ID,self.Pawnturn,self.Castling,"",False),height = 24//self.Scale,width = 72//self.Scale)
        Pieces[self.ID] = Piece
        Object[self.ID] = self
        #print(self.Castling)
        if Option == "1V1":
            Piece.grid(row = self.Position[0],column = self.Position[1])
        Positions.append(self.Position)
        #print(self.PrevPosition)
        #print(self.Position)
        #print(Positions)
        Positions.remove(self.PrevPosition)
        ColourID[self.ID] = self.Colour #Moved ID
        PieceTypes[self.ID] = self.Type
        return Piece
    def PawnTrade(self,Position,Colour,PawnTurn,ID,Scale):
        Types = ["Rook","Knight","Bishop","Queen"]
        TradeButtons = []
        #print(5/137)
        for i in range(Scale//2-2,(Scale//2-2) + 4):
            #print(i-Scale//2)
            Trade = Button(Window,height = 24//Scale,width = 72//Scale,text = Types[i-Scale//2],bg = Colour, fg = "grey",command = partial(Piece.GenerateTrade,self,Types[i-Scale//2],Colour,Position,PawnTurn,TradeButtons,Scale,))
            Trade.grid(row = Scale,column = i)
            TradeButtons.append(Trade)
    def GenerateTrade(self,Types,Colour,Position,PawnTurn,TradeButtons,Scale):
        global turn
        PieceT = Piece(Types,Position,True,Position,Position,Colour,0,0,Scale,0)
        PieceT.Generate()
        for i in range(0,len(TradeButtons)):
            TradeButtons[i].destroy()
        turn = turn - 1
        ChessTurn(Pieces)
def ChessAI(EnableGrid,Step):
    global GridPos,Scale,PiecePosition,turn,ColourID
    if len(EnableGrid) == 0:
        #print("Hi")
        EnableGrid = [""]
        ChessAI(EnableGrid,"Select")
    if Step == "Select" and Check == False: #and turn % 2 == 1: #AI V AI Remove turn % 2
        #print(Object)
        #print(len(Object))
        SelectedObject = random.choice(list(Object))
        #print(turn,ColourID)
        #print(Object)
        #print("HI")
        if turn % 2 == 1:
            while ColourID[SelectedObject] != "white":
                SelectedObject = random.choice(list(Object))
                #print(ColourID[SelectedObject])
        if turn % 2 == 0:
            while ColourID[SelectedObject] != "black":
                SelectedObject = random.choice(list(Object))
                #print(ColourID[SelectedObject])
        SelectedPiece = Object[SelectedObject]
        #print(SelectedPiece.Type)
        #print(Pieces[SelectedObject])
        EnableGrid = []
        #print(SelectedPiece.ID)
        return Moving(SelectedPiece.Type,SelectedPiece.Position,SelectedPiece.Scale,GridPos,SelectedPiece.Start,SelectedPiece.Colour,SelectedPiece.ID,SelectedPiece.ID,SelectedPiece.Pawnturn,SelectedPiece.Castling,"",False)
        #return Object[SelectedObject]
    if len(EnableGrid) != 0 and Step == "Move" and Check == False:
        Choice = EnableGrid[random.randint(0,len(EnableGrid)-1)]
        #print(EnableGrid)
        for i in GridPos.keys():
            if Choice == GridPos[i]:
                ChoiceIndex = i-1
        #print("Choice",ChoiceIndex)
        return ChoiceIndex
    if Step == "PawnTrade":
        pass
def ChessTurn(Pieces):
    global turn,EnabledPieces
    #print(Pieces)
    #print(Pieces.keys())
    for i in Pieces.keys():
        #print(Pieces)
        #print(ColourID)
        if ColourID[i] == "black" and turn % 2 == 0:
            Pieces[i].config(state = "disabled")
        elif ColourID[i] == "white" and turn % 2 == 1:
            Pieces[i].config(state = "disabled")
        else:
            Pieces[i].config(state = "normal",fg = "lime")
            EnabledPieces[i] = Pieces[i]
    turn += 1
def CheckKings():
    global PieceTypes
    KingNum = 0
    if len(KingPositions) == 1:
        Check = True
    if len(KingPositions) == 2:
        Check = False
        #print("Safe")
    return Check
def GenerateTape(PiecePosition,Colour,BoardSymbols,Type):
    global KingPositions
    if Type == "Pawn" and Colour == "white":
        BoardSymbols[0] = "I"
    Board = "~C"
    PieceHere = False
    SameColour = False
    KingHere = False
    #print("bOARD",ColourID)
    for i in GridPos.keys():
        PieceHere = False
        SameColour = False
        Piece = False
        KingHere = False
        #print(KingHere)
        if GridPos[i] == PiecePosition:
            BoardAdd = BoardSymbols[0] #N
            Piece = True
            #print(i)
        else:
            if i in KingPositions.keys() and ColourID[i] != Colour:
                KingHere = True
                #print("hi")
                BoardAdd = "K"
            else:
                pass
            if KingHere == False:
                #print(Positions)
                for x in range(0,len(Positions)):
                    if GridPos[i] != Positions[x]:
                        PieceHere = False
                    if GridPos[i] == Positions[x]:
                        PieceHere = True
                        BoardAdd = BoardSymbols[1] #X
                        C = i
                        #print("HERE")
                        break
                if PieceHere == True and KingHere == False:
                    #print(C)
                    if ColourID[C] != Colour:
                        SameColour = False
                    if ColourID[C] == Colour :
                        SameColour = True
                        BoardAdd = BoardSymbols[3] # B
                        #print("HOOO")
                #print(Board)
                if PieceHere == False and SameColour == False and Piece == False and KingHere == False:
                    BoardAdd = BoardSymbols[2]
        Board += BoardAdd
        #Checks if Rook Has Moved Or Not
        if Type == "King":
                if i in Object.keys():
                    #print(i)
                    if Object[i].Type == "Rook" and Object[i].Castling <= 0:
                        #print(Board[:-1])
                        Board = Board[:-1] + "T"
                        #print("BOARD",Board)
        if i % 8 == 0:
            Board += "C"
    Board += "#"
    BoardSymbols[0] = "N"
    #print(len(Board))
    return Board
def Moving(Type,PiecePosition,Scale,GridPositions,Start,Colour,ID,ID2,Pawnturn,Castling,CastlingBoard,Search):
    global EnableGrid,turn,PawnMove,Occupied,Positions,Pieces,Clicked,z,l,f,ColourID,InCheckMoves
    Board = "~C"
    #print(PiecePosition)
    #print(__import__("math").pi)
    #print(Castling)
    TempPositions = Positions
    print(Type)
    #print(ColourID)
    if InCheckMoves == None:
        InCheckMoves = []
    #print(InCheckMoves)
    PieceHere = False
    SameColour = False
    PositionsInCheck = ""
    #Works Tape for Turing Machine Make Function
    if Type == "CastlingRook":
        Board = CastlingBoard
    else:
        Board = GenerateTape(PiecePosition,Colour,BoardSymbols,Type)
    print(Board)
    #print(len(Board))
    readrules = open(Type+".txt","r")
    Move = ""
    CheckNum = 0
    TempMove = 0
    BoardAfterMove = ""
    Color = ""
    In = False
    b = []
    Counter = 0
    Check = []
    s = 0
    if Clicked == False:
        Clicked = True
        Castling += 1
        Hide(EnableGrid,z,Type)
    else:
        Clicked = False
        EnableGrid = []
        z = []
        l = []
        f = 0
    if Clicked == False:
        if Pawnturn == 0:
            PawnMoveIndex = 0
        else:
            PawnMoveIndex = 1
        Move = TuringMachine(readrules,Board)
        #print(Move)
        readrules.close()
        #print("Move",Move)
        if Type == "King" and Castling == 1: #King Can Not Be In Check
            readrules  = open("Castling.txt","r")
            Move = TuringMachine(readrules,Move)
            #print("Castle",Move)
            readrules.close()
        if Pawnturn == 0 and Type == "Pawn":
            readrules = open(Type+".txt","r")
            Move = TuringMachine(readrules,Move)
            readrules.close()
        Board = Move
        BoardAfterMove = Move
        BoardAfterMove = BoardAfterMove.replace("C","")
        BoardAfterMove = BoardAfterMove.replace("#","")
        Move = Move.split("C")
        #print(Type,BoardAfterMove)
        for i in range(1,len(Move)):
            for x in range(0,len(Move[i])):
                #print(Move[i][x])
                if ((i-1)*8)+(x+1) in GridPos.keys() and GridPos[((i-1)*8)+(x+1)] in InCheckMoves:
                    print("Hello")
                if Move[i][x] in MoveSymbols and (GridPos[((i-1)*8)+(x+1)] not in InCheckMoves or Type == "King"):
                    for l in InCheckMoves:
                        #print(l)
                        pass
                    EnableGrid.append(GridPos[((i-1)*8)+(x+1)])
                    z.append((i-1)*8+(x+1))
                    #print(InCheckMoves)
        #print(len(EnableGrid))
    if Search != True:
        Enable(Tiles,z,PiecePosition,Type,Colour,EnableGrid,ID,Start,ID2,Scale,Move,l,f,Castling,BoardAfterMove,Board)
        if AI == True: #and turn % 2 == 1: # Remove turn % 2 for AI V AI for now
            if len(EnableGrid) == 0: #or Type == "King":
                #print("Hi")
                EnableGrid = []
                SelectedPiece = ChessAI(EnableGrid,"Select")
                #return
            else:
                #print("SEC",ID)
                ChoiceIndex = ChessAI(EnableGrid,"Move")
                #print(ChoiceIndex)
                Movement(EnableGrid,PiecePosition,Type,Colour,Tiles,z,ID,Start,ChoiceIndex,[],ID2,Scale,0,Castling,Move,1,BoardAfterMove,Board)
    else:
        #print(Board)
        if "F" in Board:
            #print(Board)
            #print("Hello")
            PositionsInCheck = EnableGrid
        return PositionsInCheck
def Enable(Tiles,z,PiecePosition,Type,Colour,EnableGrid,ID,Start,ID2,Scale,Move,l,f,Castling,BoardAfterMove,Board):
    global GridPos,Positions,EnabledPieces,Pieces,Clicked,turn
    #print(globals())
    Row = 0
    ColourChange = []
    g = 0
    for i in EnabledPieces.keys(): #Uncomment later
        if Clicked == True:
            Pieces[i].config(state = "normal",fg = "lime green")
        elif Clicked == False:
            if GridPos[i] != PiecePosition:
                #print(len(Pieces))
                Pieces[i].config(state = "disabled")
    Occupation = []
    PositionsT = Positions
    l = []
    Colours = ""
    #print(GridPos)
    #print(Move)
    #print(EnableGrid)
    for i in range(1,len(Move)-1):
        s = (i-1)*8
        #print(Move[i])
        for x in range(0,len(Move[i])):
            #print(Move[i][x])
            if Type == "CastlingRook":
                if Move[i][x] == "V":
                    l.append(s+x)
                    break
            else:
                if Move[i][x] == "Y" or Move[i][x] == "F":
                    if Move[i][x] == "F":
                        Colours = "#ff8b28" #TOPAZ
                    else:
                        Colours = "red"
                    l.append(s+x)
                    ColourChange.append(Colours)
                if Move[i][x] == "A":
                    state = "normal"
                    Colours = "lime green"
                    l.append(s+x)
                    ColourChange.append(Colours)
                if Move[i][x] == "Q":
                    Row = i
                    state = "normal"
                    Colours = "Aquamarine"
                    l.append(s+x)
                    ColourChange.append(Colours)
            #print(l)
            #Could Shorten by adding a Colour List
        if len(l) >= 1:
            if Castling == 1 and Type == "CastlingRook":
                Type = "Rook"
                Movement(EnableGrid,PiecePosition,Type,Colour,Tiles,z,ID,Start,l[0],Occupation,ID2,Scale,g,Castling,Move,Row,BoardAfterMove,Board)
                #Enables Piece to also be clicked
                break
            else:
                for i in range(0,len(l)):
                    Colours = ColourChange[i]
                    f = l[i]
                    #print(f)
                    #print(f)
                    #print(GridPos[f],Positions)
                    if Option == "1V1":
                        #print("HI")
                        #print(Tiles[f])
                        Tiles[f].config(state = "normal",bg = Colours,command = partial(Movement,EnableGrid,PiecePosition,Type,Colour,Tiles,z,ID,Start,f,Occupation,ID2,Scale,g,Castling,Move,Row,BoardAfterMove,Board))
                    else:
                        Movement(EnableGrid,PiecePosition,Type,Colour,Tiles,z,ID,Start,f,Occupation,ID2,Scale,g,Castling,Move,Row,BoardAfterMove,Board)
            #print(Tiles)
                #Enables Piece to also be clicked
            #if GridPos[f] in Positions:
                #print(GridPos[f], Positions)
                #print(Pieces[f])
                #Pieces[f].config(state = "normal",fg = "red",command = partial(Movement,EnableGrid,PiecePosition,Type,Colour,Tiles,z,ID,Start,f,Occupation,ID2,Scale,g,Castling,Move,Row,BoardAfterMove))
    #Enables Piece to also be clicked
def Hide(EnableGrid,z,Type):
    global Tiles,TilesColour,GridPos
    for i in range(0,len(EnableGrid)):
        z[i] = z[i] - 1
        if Option == "1V1":
            Tiles[z[i]].config(state = "disabled",bg = TilesColour[z[i]])
#       Movement(EnableGrid,PiecePosition,Type,Colour,Tiles,z,ID,Start,ChoiceIndex,[],ID2,Scale,0,Castling,Move,1,BoardAfterMove,Board)
def Movement(EnableGrid,PiecePosition,Type,Colour,Tiles,l,ID,Start,f,Occupation,ID2,Scale,g,Castling,Move,Row,BoardAfterMove,Board):
    global ColourID,Pieces,GridPos,TilesColour,Positions,HasMoved,turn,EnabledPieces,Clicked,InCheckMoves,Option,AI,KingPositions,Object,PieceTypes,WhiteWins,BlackWins,Played
    #print((1+__import__("math").sqrt(5))/2)
    Occupied = False
    HasMoved = True
    Check = False
    s = list(Pieces.keys())
    s = s[-1]
    #if AI == True: # fix for now
       # print(ID2)
        #ID2 = ID
    PieceMove = Piece(Type,Start,True,GridPos[f+1],PiecePosition,Colour,ID2,1,Scale,Castling)
    for i in Positions:
        if GridPos[f+1] == i:
            Occupied = True
            for x in GridPos.keys():
                if i == GridPos[x]:
                    s = x
                    #print("x",x)
        if Occupied == True:
            Pieces[s].destroy()
            Positions.remove(GridPos[f+1])
            Object.pop(s)
            PieceTypes.pop(s)
            if s in KingPositions.keys():
                KingPositions.pop(s)
        Occupied = False
    PieceMove.Move()
    #print("Hi",PiecePosition)
    for x in range(1,len(GridPos)+1):
        if PiecePosition == GridPos[x]:
            #print("y",x)
            Pieces[x].destroy()
            Pieces.pop(x)
            Object.pop(x)
            PieceTypes.pop(x)
            ColourID.pop(x)
            Clicked = True
    #print(Object,len(Object))
    Hide(EnableGrid,z,Type)
    EnabledPieces = {}
    Check = CheckKings()
    Window.update()
    if Check == False: #and turn < 50:
        ChessTurn(Pieces)
        if AI == True: #and turn % 2 == 1:
            #print("boo")
            #print(KingPositions)
            ChessAI(Pieces,"Select")
            #print(SelectedPiece.Type)
        #SearchForCheck(Object)
        #print(InCheckMoves)
        #print(turn-1)
    if Check == True: #or turn == 50:
        if turn == 1:
            Check = False
        else:
            #print("Dead")
            #print(Check)
            print(ColourID[s],"Wins In:",turn//2,"Turns")
            if ColourID[s] == "white":
                WhiteWins += 1
            if ColourID[s] == "black":
                BlackWins += 1
            Played += 1
            print("White: ",WhiteWins,"Black: ",BlackWins,"GamesPlayed: ", Played)
            sleep(0.5)
            #Pieces[i].config(state = "disabled")
            #print(Pieces)
            Pieces = {}
            Object = {}
            KingPositions = {}
            #print(Positions)
            Positions = []
            turn = 0
            Clicked = True
            PieceTypes = {}
            Check = False
            #AI = False
            import Chess
            return Chess.Generate(0)
            #Make Board reset so more iterations of chess can be played and AI can learn
    #Pawn Trade at edge of board
    if Type == "Pawn":
        #print("Del")
        if AI == False:
            if EnableGrid[g][0] == Scale-1 or EnableGrid[g][0] == 0:
                for x in range(1,len(GridPos)+1):
                    if (GridPos[x][0] == Scale-1 and GridPos[f+1] == GridPos[x]) or (GridPos[x][0] == 0 and GridPos[f+1] == GridPos[x]):
                        s = x
                Pieces[s].destroy()
                Positions.remove(GridPos[f+1])
                Piece.PawnTrade(ID,GridPos[f+1],Colour,s,0,Scale)
        else:
            SelectedPiece = ChessAI(Pieces,"Select")
            return
    if Type == "King":
        if BoardAfterMove[f+1] == "Q":
            for x in range(0,len(Board)):
                if Board[x] == "I" or Board[x] == "N":
                    KingPos = x-1
            for i in Object.keys():
                NextTile = i+1
                if i == 64:
                    NextTile = i-1
                Checking = f + Row
                if (Object[i].Type == "Rook" and Object[i].Castling == 1) and ((BoardAfterMove[i-1] == "P" and Checking > KingPos) or (BoardAfterMove[NextTile] == "Q" and Checking < KingPos)):
                    if Checking > KingPos:
                        for g in range(0,KingPos):
                            if Board[g] not in CastleKeepers:
                                Board = Board.replace(Board[g],"B",g)
                    Board = Board.replace("N","I")
                    turn -= 1
                    Moving("CastlingRook",Object[i].Position,Scale,GridPos,Object[i].Start,Object[i].Colour,Object[i].ID,ID2,0,Castling,Board,False)
                    break
    ActualTurn = turn - 1
    #Might have to replace rook identifiers in king to determine move
def SearchForCheck(Object):
    global InCheckMoves
    for i in Object: #Might Check if piece is blocked to speed up
        #print(Object[i].Type)
        InCheckMoves.append(Moving(Object[i].Type,Object[i].Position,Scale,GridPos,Object[i].Start,Object[i].Colour,Object[i].ID,0,Object[i].Pawnturn,Object[i].Castling,"",True))
    #print("Not",InCheckMoves)
def Terminate():
    print("Hi")
    pass

