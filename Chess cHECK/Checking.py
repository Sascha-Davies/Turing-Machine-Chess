#print(Line.splitlines())
#print((i.split(";"))[1],(MovesMadeWhite[x].split(";")[1]))
#print(MovesMadeWhite[x][-1])
i = "Knightwhite[0, 1][2, 0];2"

ProbabilityValue = (i.split(";"))[1]
MoveMade = (i.split(";"))[0]
#print(ProbabilityValue)
#print(MovesMadeWhite[x])
ProbabilityValue = str(int(ProbabilityValue) + 1)
print(ProbabilityValue)
#print(MoveMade)
MoveMadeAppended = MoveMade+";"+ProbabilityValue
print(MoveMadeAppended)
Line = Line.replace(i,MoveMadeAppended)
