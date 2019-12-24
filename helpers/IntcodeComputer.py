def getNextInstruction(instructionParam):
    return int(instructionParam) % 100


def getParameter(programCode, io, paramPos, instructionPosition, relativeModePosition):
    iofields = list(io)
    iofields.reverse()
    iofields = iofields + ['0', '0', '0', '0', '0']

    intermediate = int(iofields[paramPos + 1])

    if intermediate == 0:
        return int(programCode.setdefault(instructionPosition + paramPos, 0))
    elif intermediate == 1:
        return instructionPosition + paramPos
    elif intermediate == 2:
        return relativeModePosition + int(programCode.setdefault(instructionPosition + paramPos, 0))


def runProgram(programCode, input):
    programCodeDict = {i: programCode[i] for i in range(0, len(programCode))}

    instructionPosition = 0
    relativeModePosition = 0
    outputPosition = 0
    output = []
    inputPos = 0
    inputParam = input[0]

    instruction = getNextInstruction(int(programCodeDict.setdefault(instructionPosition, 0)))

    while instruction in (1, 2, 3, 4, 5, 6, 7, 8, 9):

        instructionObject = str(programCodeDict.setdefault(instructionPosition, 0))

        if len(instructionObject) > 2:
            firstInput = getParameter(programCodeDict, instructionObject, 1, instructionPosition, relativeModePosition)
            secondInput = getParameter(programCodeDict, instructionObject, 2, instructionPosition, relativeModePosition)
            outputPosition = getParameter(programCodeDict, instructionObject, 3, instructionPosition, relativeModePosition)
        else:
            firstInput = int(programCodeDict.setdefault(instructionPosition + 1, 0))
            secondInput = int(programCodeDict.setdefault(instructionPosition + 2, 0))
            try:
                outputPosition = int(programCodeDict.setdefault(instructionPosition + 3, 0))
            except IndexError:
                outputPosition = 0

        if instruction == 1:
            programCodeDict[outputPosition] = int(programCodeDict.setdefault(firstInput, 0)) + int(
                programCodeDict.setdefault(secondInput, 0))
            nextStep = instructionPosition + 4
        if instruction == 2:
            programCodeDict[outputPosition] = int(programCodeDict.setdefault(firstInput, 0)) * int(
                programCodeDict.setdefault(secondInput, 0))
            nextStep = instructionPosition + 4
        if instruction == 3:
            programCodeDict[firstInput] = inputParam
            if len(input) > inputPos + 1:
                inputParam = input[inputPos + 1]
                inputPos += 1
            nextStep = instructionPosition + 2
        if instruction == 4:
            output += [programCodeDict.setdefault(firstInput, 0)]
            print("Output is " + str(programCodeDict.setdefault(firstInput, 0)))
            nextStep = instructionPosition + 2
        if instruction == 5:
            if int(programCodeDict.setdefault(firstInput, 0)) != 0:
                nextStep = int(programCodeDict.setdefault(secondInput, 0))
            else:
                nextStep = instructionPosition + 3
        if instruction == 6:
            if int(programCodeDict.setdefault(firstInput, 0)) == 0:
                nextStep = int(programCodeDict.setdefault(secondInput, 0))
            else:
                nextStep = instructionPosition + 3
        if instruction == 7:
            if int(programCodeDict.setdefault(firstInput, 0)) < int(programCodeDict.setdefault(secondInput, 0)):
                programCodeDict[outputPosition] = 1
            else:
                programCodeDict[outputPosition] = 0
            nextStep = instructionPosition + 4

        if instruction == 8:
            if int(programCodeDict.setdefault(firstInput, 0)) == int(programCodeDict.setdefault(secondInput, 0)):
                programCodeDict[outputPosition] = 1
            else:
                programCodeDict[outputPosition] = 0
            nextStep = instructionPosition + 4

        if instruction == 9:
            relativeModePosition = relativeModePosition + int(programCodeDict.setdefault(firstInput, 0))
            nextStep = instructionPosition + 2

        instruction = getNextInstruction(programCodeDict.setdefault(nextStep, 0))
        instructionPosition = nextStep

    return output
