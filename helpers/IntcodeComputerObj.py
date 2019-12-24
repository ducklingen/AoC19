class IntcodeComputer:
    programCode = {}
    instructionPosition = 0
    relativeModePosition = 0

    def __init__(self, programCode):
        self.programCode = {i: programCode[i] for i in range(0, len(programCode))}
        self.instructionPosition = 0
        self.relativeModePosition = 0

    def getNextInstruction(self, instructionParam):
        return int(instructionParam) % 100

    def getParameter(self, io, paramPos):
        iofields = list(io)
        iofields.reverse()
        iofields = iofields + ['0', '0', '0', '0', '0']

        intermediate = int(iofields[paramPos + 1])

        if intermediate == 0:
            return int(self.programCode.setdefault(self.instructionPosition + paramPos, 0))
        elif intermediate == 1:
            return self.instructionPosition + paramPos
        elif intermediate == 2:
            return self.relativeModePosition + int(self.programCode.setdefault(self.instructionPosition + paramPos, 0))

    def runProgram(self, input, input2):
        self.instructionPosition = 0
        self.relativeModePosition = 0
        output = 0
        inputParam = input

        instruction = self.getNextInstruction(int(self.programCode.setdefault(self.instructionPosition, 0)))

        while instruction in (1, 2, 3, 4, 5, 6, 7, 8, 9):

            instructionObject = str(self.programCode.setdefault(self.instructionPosition, 0))

            if len(instructionObject) > 2:
                firstInput = self.getParameter(instructionObject, 1)
                secondInput = self.getParameter(instructionObject, 2)
                output = self.getParameter(instructionObject, 3)
            else:
                firstInput = int(self.programCode.setdefault(self.instructionPosition + 1, 0))
                secondInput = int(self.programCode.setdefault(self.instructionPosition + 2, 0))
                try:
                    output = int(self.programCode.setdefault(self.instructionPosition + 3, 0))
                except IndexError:
                    output = 0

            if instruction == 1:
                self.programCode[output] = int(self.programCode.setdefault(firstInput, 0)) + int(self.programCode.setdefault(secondInput, 0))
                nextStep = self.instructionPosition + 4
            if instruction == 2:
                self.programCode[output] = int(self.programCode.setdefault(firstInput, 0)) * int(self.programCode.setdefault(secondInput, 0))
                nextStep = self.instructionPosition + 4
            if instruction == 3:
                self.programCode[firstInput] = inputParam
                inputParam = input2
                nextStep = self.instructionPosition + 2
            if instruction == 4:
                output = self.programCode.setdefault(firstInput,0)
                print("Output is " + str(output))
                nextStep = self.instructionPosition + 2
            if instruction == 5:
                if int(self.programCode.setdefault(firstInput, 0)) != 0:
                    nextStep = int(self.programCode.setdefault(secondInput, 0))
                else:
                    nextStep = self.instructionPosition + 3
            if instruction == 6:
                if int(self.programCode.setdefault(firstInput, 0)) == 0:
                    nextStep = int(self.programCode.setdefault(secondInput, 0))
                else:
                    nextStep = self.instructionPosition + 3
            if instruction == 7:
                if int(self.programCode.setdefault(firstInput, 0)) < int(self.programCode.setdefault(secondInput, 0)):
                    self.programCode[output] = 1
                else:
                    self.programCode[output] = 0
                nextStep = self.instructionPosition + 4

            if instruction == 8:
                if int(self.programCode.setdefault(firstInput, 0)) == int(self.programCode.setdefault(secondInput, 0)):
                    self.programCode[output] = 1
                else:
                    self.programCode[output] = 0
                nextStep = self.instructionPosition + 4

            if instruction == 9:
                self.relativeModePosition = self.relativeModePosition + int(self.programCode.setdefault(firstInput, 0))
                nextStep = self.instructionPosition + 2

            instruction = self.getNextInstruction(self.programCode.setdefault(nextStep, 0))
            self.instructionPosition = nextStep

        return output
