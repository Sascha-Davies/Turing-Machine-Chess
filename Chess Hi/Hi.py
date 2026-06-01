file = open("Bishop.txt","r")
rules = {}
Lines = []
for i in file:
        i = i.split("\n")
        i[0] = i[0].split("|")
        Lines.append(i[0])
        print(i)
for x in range(1,len(Lines)):
        i = Lines[x][0]
        z = Lines[x][4]
        i = i.split("S")
        z = z.split("S")
        i[1] = int(i[1])
        z[1] = int(z[1])
        i[1] += 17
        z[1] += 17
        i[1] = str(i[1])
        z[1] = str(z[1])
        v = "S" + i[1]
        j = "S" + z[1]
        Lines[x][0] = v
        Lines[x][4] = j
        #print(Lines[x])
        line = Lines[x][0] +"|" + Lines[x][1] + "|" + Lines[x][2] + "|" + Lines[x][3] + "|" + Lines[x][4]
        print(line)
for i in range(0,len(States)):
        States[i] = States[i].split("S")
        if int(States[i][1]) > StateValue:
            StateValue = int(States[i][1])
        State = "S" + str(States[0][1])
