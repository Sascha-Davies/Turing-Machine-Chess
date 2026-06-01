initialTape = "~CBBBBB0BBCBBBB0BBBC00000000C00000000C0000000XCX0000X00CXXXXX00NCX0XXXX0XC#"
#CXXXXXXXXCXXXX0XXXC00000000C0000X000C00000000C00000000CBBBBBBBBCBBBBBNBBC
#CBBBBB0BBCBBBB0BBBC00000000C00000000C0000000XCX0000X00CXXXXX00NCX0XXXX0XC
#C - Edge of row
#B - Same Colour / Cant Move
#X - Different Colour
#Y - Can take
#A - Can Move
#0 - Available Space
#I or N - Position of Piece Clicked
#~ or # - End of Board
#D - End Of Board (Better to take to other states)
#Q - Castle Possible Move
#R - Rook identity for castling
#P - Determine the Rook
#Z - B on the left side of king ( for castling )
#T - ROOK
readrules = open("Bishop.txt","r")
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
    EndTape = ""
    #print("HHII")
    for i in readrules:
        #print("HI")
        i = i.split("\n")
        i[0] = i[0].split("|")
        Lines.append(i[0])
        #print(i)
    for x in range(1,len(Lines)):
        rules[x-1] = Lines[x]
        #print(rules[x-1])
        Signs.append(rules[x-1][3])
        States.append(rules[x-1][4])
        #print(States)
    for i in range(0,len(States)):
        States[i] = States[i].split("S")
        if int(States[i][1]) > StateValue:
            StateValue = int(States[i][1])
        State = "S" + str(States[0][1])
            #Make Dictionary in future when more then one HaltStates
    haltStates.append("S"+str(StateValue))
    for i in range(0,len(initialTape)):
        tape.append(initialTape[i])
    #print(tape[1])
        #for i in range(0,len(Signs)):
            #if Signs[i] != signs[z] and signs[z] != signs[0]:
                #signs = Signs[i]
                #Signs.remove(Signs[i])
                #print(rules[i][3])
    while State != haltStates[0]:
        for i in rules.keys():
            if rules[i][0] == State:
                #print(State)
                #print(rules[i])
                if tape[ReadWritePosition] == rules[i][1]:
                    #print(State)
                    #print(rules[i])
                    #print(tape[ReadWritePosition])
                    tape[ReadWritePosition] = rules[i][2]
                    #print(tape[ReadWritePosition])
                    #print(Values)
                    if rules[i][1] == "~" or rules[i][1] == "I":
                        Values[0] = 1
                        Values[1] = -1
                    for x in range(0,len(signs)):
                        #print(signs[x],rules[i][3])
                        if signs[x] == rules[i][3]:
                            ReadWritePosition += Values[x]
                    if rules[i][1] == "N": #or rules[i][1] == "#":
                        Values[0] = -1
                        Values[1] = 1
                    #if rules[i][1] == "I":
                        #rules[0][2] = "B"
                    #print(tape)
                    #print(Values)
                    #print(ReadWritePosition)
                    ##print(rules[i])
                    ##print(tape[ReadWritePosition])
                    ##print(State,"OLD")
                    State = rules[i][4]
                    ##print(State,"NEW")
    for i in range(0,len(tape)):
        EndTape += tape[i]
        if tape[i] == "Y" or tape[i] == "A":
            Solution += 1
    #print(Solution)
    return EndTape
#turing = TuringMachine(readrules,initialTape)
#print(turing,"turing ,arun")
#RULES FOR VERTICAL: GO ALL THE WAY TO THE BEGGINING AND CHANGE I BACK TO N
##After all first iterations (left side) when reaching a y or a add 2 to value and then change if possible
                    
            


