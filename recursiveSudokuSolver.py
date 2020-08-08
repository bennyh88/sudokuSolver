#rows and columns are not 0 indexed
#cell value of '0' means it has no value

class Cell:

    def __init__(self, row, column, value):
        self.row = row
        self.column = column
        self.box = self.whereDoILive()
        self.value = value
        self.candidateList = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

        if value != "0":
            self.candidateList.clear()
            self.candidateList.append(value)

    def whereDoILive(self):
        if self.row < 4:
            if self.column < 4:
                return "A"
            elif self.column > 6:
                return "G"
            else:
                return "D"
        elif self.row > 6:
            if self.column < 4:
                return "C"
            elif self.column > 6:
                return "I"
            else:
                return "F"
        else:
            if self.column < 4:
                return "B"
            elif self.column > 6:
                return "H"
            else:
                return "E"


    def tryCandidate(self, candidate):
        if self.tryRow(candidate) == True and self.tryColumn(candidate) == True and self.tryBox(candidate) == True:
            return True
        return False

    def tryRow(self, candidate):
        for index in cellsList:
            if index.row == self.row:
                if index.value == candidate:
                    return False
        return True #return true if the candidate can be used

    def tryColumn(self, candidate):
        for index in cellsList:
            if index.column == self.column:
                if index.value == candidate:
                    return False
        return True #return true if the candidate can be used

    def tryRow(self, candidate):
        for index in cellsList:
            if index.row == self.row:
                if index.value == candidate:
                    return False
        return True #return true if the candidate can be used

    def tryBox(self, candidate):
        for index in cellsList:
            if index.box == self.box:
                if index.value == candidate:
                    return False
        return True #return true if the candidate can be used




#    def checkRow(self, cellsList):
#        if len(self.candidateList) > 1:
#            for index in cellsList:
#                if index.row == self.row:
#                    if index.value in self.candidateList:
#                        self.candidateList.remove(index.value)
#                        self.checkCandidateList();
#                        #print(index.value + " removed as in row")
#
#    def checkColumn(self, cellsList):
#        if len(self.candidateList) > 1:
#            for index in cellsList:
#                if index.column == self.column:
#                    if index.value in self.candidateList:
#                        self.candidateList.remove(index.value)
#                        self.checkCandidateList()
#                        #print(index.value + " removed as in column")
#
#    def checkBox(self, cellsList):
#        if len(self.candidateList) > 1:
#            for index in cellsList:
#                if index.box == self.box:
#                    if index.value in self.candidateList:
#                        self.candidateList.remove(index.value)
#                        self.checkCandidateList()
#
#    def checkCandidateList(self):
#        if len(self.candidateList) == 1:
#            self.value = self.candidateList[0]
#            print("New Cell value found! " + self.value + "  @ row:" + str(self.row) + " column:" + str(self.column))
#            simpleCheck()




#simple
#puzzleList = [  '0','1','0',    '0','2','9',    '0','6','0',
#                '0','0','0',    '0','4','0',    '0','3','0',
#                '0','0','0',    '8','6','1',    '2','0','5',
#
#                '0','0','7',    '0','0','0',    '1','9','2',
#                '2','0','0',    '9','7','8',    '0','0','4',
#                '5','9','4',    '0','0','0',    '8','0','0',
#
#                '7','0','6',    '1','3','5',    '0','0','0',
#                '0','4','0',    '0','8','0',    '0','0','0',
#                '0','5','0',    '4','9','0',    '0','8','0'    ]

#tricky
puzzleList = [  '0','0','0',    '0','0','2',    '0','0','4',
                '2','0','5',    '0','0','6',    '8','0','7',
                '0','1','0',    '5','0','0',    '0','0','0',

                '0','6','2',    '0','3','0',    '0','0','0',
                '7','0','8',    '0','0','0',    '6','0','5',
                '0','0','0',    '0','6','0',    '4','2','0',

                '0','0','0',    '0','0','7',    '0','8','0',
                '4','0','1',    '6','0','0',    '9','0','2',
                '9','0','0',    '2','0','0',    '0','0','0'    ]



cellsList = []

def loadPuzzle():
    counter = 0
    for row in range(1, 10):
        for column in range(1, 10):
            value = puzzleList[counter]
            cell = Cell(row, column, value)
            cellsList.append(cell)
            counter += 1

def printPuzzle():
    spaceList = [2, 5, 11, 14, 20, 23, 29, 32, 38, 41, 47, 50, 56, 59, 65, 68, 74, 77]
    newLineList = [8, 17, 26, 35, 44, 53, 62, 71, 80]
    extraLineList = [26, 53]
    string = ""
    for index in range(0, 81):
        string = string + cellsList[index].value + " "
        if index in spaceList:
            string = string + "| "
        if index in newLineList:
            string = string + "\n"
        if index in extraLineList:
            string = string + "- - - + - - - + - - - \n"
    print(string)

#def printCandidateList():
#    for index in range(1,81):
#        print(cellsList[index].candidateList)


spaceList = []

def bruteForce(spaceListIndex, stack):
    stack += 1
    #print("stack = " + str(stack))
    if (spaceListIndex >= len(spaceList)):
        return True
    cell = cellsList[spaceList[spaceListIndex]]
    #print("cell" + str(spaceList[spaceListIndex]))
    #print("cell candidateList = ")
    #print(cell.candidateList)

    for candidate in cell.candidateList:
        #print("stack = " + str(stack) +" candidate = " + str(candidate))
        if cell.tryCandidate(candidate) == True:
            cell.value = candidate
            print("trying new candidate " + cell.value + "  @ row:" + str(cell.row) + " column:" + str(cell.column))
            #printPuzzle()
            print("")
            newSpaceListIndex = spaceListIndex + 1
            if bruteForce(newSpaceListIndex, stack) == True:
                stack -= 1
                return True
    #print("stack = " + str(stack))
    print("no more candidates, return")
    stack -= 1
    cell.value = "0"
    return False






loadPuzzle()
printPuzzle()
print("============================================================================================================================")

for index in cellsList:
    if index.value == "0":
        spaceList.append(cellsList.index(index))

print("============================================================================================================================")
print("")
print("")

stack = 1
if bruteForce(0,0) == True:
    printPuzzle()
    print("SOLVED!!!")
else:
    print("Error: brute force returned false")
