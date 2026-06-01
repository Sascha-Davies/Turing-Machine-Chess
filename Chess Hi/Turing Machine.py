initialTape = "~00XX0X0XCX000XN0XC0XX000X0CX00XX00XC00XXX000CX000XX00C0XX000X0CX00XX00XC#"
readrules = open("Pawn.txt","r")
#ROOK Complete
def TuringMachine(readrules,initialTape):
    ReadWritePosition = 1
    Solution = 0
    Signs = []
    StateValue = 0
    State = ""
    States = []
    Lines = []
    tape = []
    haltStates = []
    signs = [">","<","-"]
    Values = [1,-1,0]
    rules = {}
    for i in readrules:
        i = i.split("\n")
        i[0] = i[0].split("|")
        Lines.append(i[0])
        #print(i)
    for x in range(1,len(Lines)):
        rules[x-1] = Lines[x]
        #Signs.append(rules[x-1][3])
        States.append(rules[x-1][4])
        #print(States)
    for i in range(0,len(States)):
        States[i] = States[i].split("S")
        if int(States[i][1]) > StateValue:
            StateValue = int(States[i][1])
        State = "S" + str(States[0][1])
            #Make Dictionary in future when more then one HaltStates
    haltStates.append("S"+str(StateValue))
    #print(haltStates)
    #print(rules)
    #print(rules[0][3])
    for i in range(0,len(initialTape)):
        tape.append(initialTape[i])
    #print(tape[1])
        #for i in range(0,len(Signs)):
            #if Signs[i] != signs[z] and signs[z] != signs[0]:
                #signs = Signs[i]
                #Signs.remove(Signs[i])
                #print(rules[i][3])
    #print(signs)
    #print(haltStates[0])
    #print(State)
    while State != haltStates[0]:
        #print(State)
        #print(Values)
        for i in rules.keys():
            if rules[i][0] == State:   
                if tape[ReadWritePosition] == rules[i][1]:
                    #print(rules[i])
                    tape[ReadWritePosition] = rules[i][2]
                    #print(tape[ReadWritePosition])
                    #print(Values)
                    if rules[i][1] == "~":
                        Values[0] = 1
                        Values[1] = -1
                    for x in range(0,len(signs)):
                        #print(signs[x],rules[i][3])
                        if signs[x] == rules[i][3]:
                            ReadWritePosition += Values[x]
                    if rules[i][1] == "N":
                        Values[0] = -1
                        Values[1] = 1
                    if rules[i][1] == "I":
                        rules[0][2] = "B"
                    State = rules[i][4]
        #print(Values)
        #print(tape[ReadWritePosition])
    #print(tape)
    for i in range(0,len(tape)):
        if tape[i] == "Y":
            Solution += 1
    print(Solution)
    return tape
turing = TuringMachine(readrules,initialTape)
print(turing)
#RULES FOR VERTICAL: GO ALL THE WAY TO THE BEGGINING AND CHANGE I BACK TO N
            
                    
            


