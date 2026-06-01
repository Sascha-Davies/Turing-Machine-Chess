import turtle
import math
StateCoor = []
x = 0
y = -400
file = "Queen.txt"
f = open(file,"r")
States = []
## for repeat arches draw a semi circle of smaller radius using t.circle(radius,period)
Graph = {}
Edges = []
t = turtle
t.penup()
t.ht()
ArrowSize = 5
t.tracer(0)
t.goto(x,y)
StatesDict = []
#t.pendown()
t.speed(100)
Arc = []
#356.2147192619392, -275.85394390673196
complete = False
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
#print(Graph)
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
#print(Graph)
def State(SNum,x,y):
    StateCoor.append([SNum])
    #t.speed("fastest")
    t.penup()
    t.goto(x,y)
    t.pendown()
    StatesDict.append(t.color("Black"))
    for i in range(0,4):
        StateCoor[len(StateCoor) - 1].append([t.xcor(),t.ycor()])
        #t.write(i)
        t.circle(25,90)
        #StateCoor[len(StateCoor) - 1].append([t.xcor(),t.ycor()])
        #print(i)
    t.penup()
    t.goto((((StateCoor[-1][1][0]+StateCoor[-1][3][0])/2)),((StateCoor[-1][1][1]+StateCoor[-1][3][1])/2))
    t.pendown()
    t.write(SNum)
    t.penup()
    t.goto(t.xcor(),t.ycor()-3)
    if SNum == States[-1]:
        t.pendown()
        t.circle(15)
        t.penup()
    t.goto(x,y)
    t.pendown()
def Edge(CoorC,ListOfChange,CoorN,C,N):
    lefthand = ""
    righthand = ""
    #i,j = 1,3
    #x,y = 0,0
    Repeat = False
    #print(abs(C-N))
    if abs(C - N) == 1:
        if C < N:
            i,j = 2,4
        else:
            i,j = 4,2
    else:
        i,j = 3,3
    if abs(C-N) == 0:
        Repeat = True
        #pass
    #if C == 0 and N == 1:
        #print("hi")
        #print(ListOfChange)
    #print(CoorC,CoorN)
    t.penup()
    #t._colormode(255)
    t.color(Colour)
    #t.color(__import__("random").randint(0,180),__import__("random").randint(0,180),__import__("random").randint(0,180))
    t.goto(CoorC[i][0],CoorC[i][1])
    if Repeat == False:
        t.pendown()
        t.setheading(t.towards(CoorN[j][0],CoorN[j][1]))
        t.speed(10)
        #print(t.xcor())
        #print(Colour)
        t.goto(CoorN[j][0],CoorN[j][1])
        #print(t.xcor())
        t.penup()
        t.goto((CoorC[i][0] + CoorN[j][0])/2,(CoorC[i][1] + CoorN[j][1])/2)
    else:
        #t.left(90)
        t.setheading(t.towards(CoorN[1][0],CoorN[1][1]))
        t.goto(CoorN[1][0],CoorN[1][1])
        t.pendown()
        t.circle(20,360)
        t.penup()
        t.left(180)
        #print(Colour)
    #print(CoorC[i][0],CoorN[j][0])
    t.pendown()
    if C-N < 0:
        t.color("#FC3974")
    if C-N > 0:
        t.color("#B769FA")
    if C-N == 0:
        t.color("#C5F172")
    t.begin_fill()
    t.rt(90)
    t.fd(ArrowSize)
    t.left(120)
    t.fd(2*ArrowSize)
    t.lt(120)
    t.fd(2*ArrowSize)
    t.lt(120)
    t.fd(ArrowSize)
    t.end_fill()
    t.penup()
    t.color(Colour)
    if abs(CoorC[i][0] - CoorN[j][0]) >= abs(CoorC[i][1] - CoorN[j][1]):
        if Colour == "Blue":
            x,y = t.xcor(),t.ycor() - 10
            t.color("Brown") #7285B2
        else:
            x,y = t.xcor(),t.ycor() + 10
            t.color("Brown")
    if abs(CoorC[i][0] - CoorN[j][0]) <= abs(CoorC[i][1] - CoorN[j][1]):
        if Colour == "Blue":
            x,y = t.xcor() - 10,t.ycor()
            t.color("Brown") ##2235C2
        else:
            x,y = t.xcor() + 10,t.ycor()
            t.color("Brown") #C63952
    if Repeat == True and CoorN[1][1] < CoorN[3][1]:
        x,y = t.xcor(),t.ycor() - 25
    elif Repeat == True and CoorN[1][1] > CoorN[3][1]:
        x,y = t.xcor(),t.ycor() + 25
    t.goto(x,y)
    for i,it in enumerate(ListOfChange):
        if i < len(ListOfChange) - 1:
            lefthand += it[0]+ ","
            righthand += it[1] + ","
        else:
            lefthand += it[0]
            righthand += it[1]
    t.write(lefthand + "|" + righthand,font = ("Elephant Pro",10)) ##101##01100
    #if Repeat == True:
        #t.color(Colour)
        #t.circle(20,180)
    #t.goto(xN,yN)
angle = 360/len(States)
f = 2500/len(States) #2500
for i,it in enumerate(States):
    State(it,x,y)
    t.penup()
    t.forward(f)
    t.left(angle)
    t.pendown()
    x = t.xcor()
    y = t.ycor()
    #if x >= 900:
        #y = y - 100
        #x = -850
f = open(file,"r")
#print(StateCoor[1])
for line in f:
    if "\n" in line:
        l = line[:-1].split("|")
    else:
        l = line.split("|")
    for i,it in enumerate(States):
        #print(it,l[0])
        EdgeDirection = it+":"+l[4]
        #print(EdgeDirection)
        if l[0] == it and EdgeDirection not in Arc:
            Arc.append(EdgeDirection)
            Edges.append([EdgeDirection,l[3]])
            #print(EdgeDirection)
            #print(Edges[len(Edges)-1])
        if l[0] == it and EdgeDirection in Arc:
            for x,xt in enumerate(Edges):
                if EdgeDirection == xt[0]:
                    xt.append([l[1],l[2]])
#print(Edges[0][2:])
#print(len(Edges))
#print(Edges)
#print(StatesDict)
#State("SA",0,300)
#State("S~#",0,0)
#(x-h)^2+(y-a)^2 = r^2
#x^2 +y^2 = r^2
#sqrt(x^2+y^2) = r
Colour = "Red"
#xC,yC,xN,yN = 0,0,0,0
NDetected = False
for i,it in enumerate(Edges):
    #print(it)
    l = it[0].split(":")[0]
    #print(l)
    StateIndexC = int((l.split("S")[1]))
   # print(it)
    l = it[0].split(":")[1]
    #print((l.split("S")[1]))
    StateIndexN = int((l.split("S")[1]))
    #print(StateIndexC,StateIndexN)
    #Direction of Turing Machine Pointer
    if Edges[0][:2] == "N":
        NDetected = True
    if Edges[0][:2] == "I":
        NDetected = False
    if (it[1] == ">" and NDetected == False) or (it[1] == "<" and NDetected == True):
        Colour = "Red"
    if (it[1] == "<" and NDetected == False) or (it[1] == ">" and NDetected == True):
        Colour = "Blue"
    #print(StateIndexC,StateIndexN)
    #print(StateX[0])
    #if it[1] != "A" and it[1] != ("~" or "#") and it[3] != ("S0" or "S1"):
    Edge(StateCoor[StateIndexC],it[2:],StateCoor[StateIndexN],StateIndexC,StateIndexN)
t.hideturtle()

    #elif it[1] == "A" and it[0]:
        #Edge(StateX[StateIndexC],StateY[StateIndexC] + 50,0,0,0,0,300)
    #elif it[1] == ("~" or "#"):
         #Edge(StateX[StateIndexC],StateY[StateIndexC],0,0,0,0,50)
#print(Edges)
    #Edge(
#red for left blue for right, different shades
