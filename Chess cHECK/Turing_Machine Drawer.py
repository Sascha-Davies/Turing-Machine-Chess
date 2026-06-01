import turtle
StateX = []
StateY = []
x = -850
y = 200
file = "Pawn.txt"
f = open(file,"r")
States = []
Graph = {}
Edges = []
for line in f:
    l = line[:-1].split("|")
    if l[0] in States or "#" in line:
        pass
    else:
        States.append(l[0])
        Graph[l[0]] = []
States.append("S" + str(int(States[-1].split("S")[1]) + 1))
Graph[States[-1]] = []
f.close()
print(Graph)
for i,it in enumerate(States):
    #print(it)
    f = open(file,"r")
    for line in f:
        l = line[:-1].split("|")
        #print(l[0],it)
        if (l[4] not in Graph[it]) and (l[0] == it):#and ("#" not in line):
            #print("hi")
            Graph[it].append(l[4])
    f.close()
f.close()
print(Graph)
def State(SNum,x,y):
    t = turtle
    t.speed("fastest")
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color("Black")
    t.circle(25)
    t.penup()
    t.goto(t.position()[0] - 5,t.position()[1] + 15)
    t.pendown()
    t.write(SNum)
def Edge(xC,yC,Current,New,NextState,xN,yN):
    t = turtle
    t.penup()
    t.colormode(255)
    t.color(__import__("random").randint(0,180),__import__("random").randint(0,180),__import__("random").randint(0,180))
    t.goto(xC,yC)
    t.pendown()
    t.goto(xN,yN)
    t.write(Current)
    #t.goto(xN,yN)
for i,it in enumerate(States):
    State(it,x,y)
    StateX.append(x)
    StateY.append(y)
    x = x + 100
    y = y
    if x >= 900:
        y = y - 100
        x = -850
f = open(file,"r")
for line in f:
    l = line[:-1].split("|")
    for i,it in enumerate(States):
        #print(it,l[0])
        if l[0] == it:
            Edges.append([it,l[1],l[2],l[4]])
print(len(Edges))
print(Edges)
State("SA",0,300)
State("S~#",0,0)
for i,it in enumerate(Edges):
    #print(it)
    StateIndexC = int((it[0].split("S")[1]))
    StateIndexN = int((it[3].split("S")[1]))
    #print(StateIndexC,StateIndexN)
    #print(StateX[0])
    if it[1] != "A" and it[1] != ("~" or "#") and it[3] != ("S0" or "S1"):
        Edge(StateX[StateIndexC] + 25,StateY[StateIndexC] + 25,0,0,0,StateX[StateIndexN] + 25,StateY[StateIndexN] + 25)
    elif it[1] == "A" and it[0]:
        Edge(StateX[StateIndexC],StateY[StateIndexC] + 50,0,0,0,0,300)
    elif it[1] == ("~" or "#"):
         Edge(StateX[StateIndexC],StateY[StateIndexC],0,0,0,0,50)
#print(Edges)
    #Edge(
#red for left blue for right, different shades
