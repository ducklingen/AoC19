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
    instructionPosition = 0
    relativeModePosition = 0
    output = 0
    inputPos = 0
    inputParam = input[0]

    instruction = getNextInstruction(int(programCode.setdefault(instructionPosition, 0)))

    while instruction in (1, 2, 3, 4, 5, 6, 7, 8, 9):

        instructionObject = str(programCode.setdefault(instructionPosition, 0))

        if len(instructionObject) > 2:
            firstInput = getParameter(programCode, instructionObject, 1, instructionPosition, relativeModePosition)
            secondInput = getParameter(programCode, instructionObject, 2, instructionPosition, relativeModePosition)
            output = getParameter(programCode, instructionObject, 3, instructionPosition, relativeModePosition)
        else:
            firstInput = int(programCode.setdefault(instructionPosition + 1, 0))
            secondInput = int(programCode.setdefault(instructionPosition + 2, 0))
            try:
                output = int(programCode.setdefault(instructionPosition + 3, 0))
            except IndexError:
                output = 0

        if instruction == 1:
            programCode[output] = int(programCode.setdefault(firstInput, 0)) + int(
                programCode.setdefault(secondInput, 0))
            nextStep = instructionPosition + 4
        if instruction == 2:
            programCode[output] = int(programCode.setdefault(firstInput, 0)) * int(
                programCode.setdefault(secondInput, 0))
            nextStep = instructionPosition + 4
        if instruction == 3:
            programCode[firstInput] = inputParam
            if len(input) > inputPos:
                inputParam = input[inputPos + 1]
                inputPos += 1
            nextStep = instructionPosition + 2
        if instruction == 4:
            output = programCode.setdefault(firstInput, 0)
            print("Output is " + str(output))
            nextStep = instructionPosition + 2
        if instruction == 5:
            if int(programCode.setdefault(firstInput, 0)) != 0:
                nextStep = int(programCode.setdefault(secondInput, 0))
            else:
                nextStep = instructionPosition + 3
        if instruction == 6:
            if int(programCode.setdefault(firstInput, 0)) == 0:
                nextStep = int(programCode.setdefault(secondInput, 0))
            else:
                nextStep = instructionPosition + 3
        if instruction == 7:
            if int(programCode.setdefault(firstInput, 0)) < int(programCode.setdefault(secondInput, 0)):
                programCode[output] = 1
            else:
                programCode[output] = 0
            nextStep = instructionPosition + 4

        if instruction == 8:
            if int(programCode.setdefault(firstInput, 0)) == int(programCode.setdefault(secondInput, 0)):
                programCode[output] = 1
            else:
                programCode[output] = 0
            nextStep = instructionPosition + 4

        if instruction == 9:
            relativeModePosition = relativeModePosition + int(programCode.setdefault(firstInput, 0))
            nextStep = instructionPosition + 2

        instruction = getNextInstruction(programCode.setdefault(nextStep, 0))
        instructionPosition = nextStep

    return output
