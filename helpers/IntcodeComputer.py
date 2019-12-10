class IntcodeComputer:
    programCode = []

    def __init__(self, programCode):
        self.programCode = programCode

    def getNextInstruction(self, instructionParam):
        return int(instructionParam) % 10

    def getParameter(self, io, paramPos, instructionPos, programToRun):
        iofields = list(io)
        iofields.reverse()
        iofields = iofields + ['0', '0', '0', '0', '0']

        intermediate = int(iofields[paramPos + 1])

        if intermediate == 0:
            return int(programToRun[instructionPos + paramPos])
        elif intermediate == 1:
            return instructionPos + paramPos

    def runProgram(self, input, input2):
        instructionPosition = 0
        output = 0
        inputParam = input

        instruction = self.getNextInstruction(int(self.programCode[instructionPosition]))

        while instruction in (1, 2, 3, 4, 5, 6, 7, 8):

            instructionObject = str(self.programCode[instructionPosition])

            if len(instructionObject) > 2:
                firstInput = self.getParameter(instructionObject, 1, instructionPosition, self.programCode)
                secondInput = self.getParameter(instructionObject, 2, instructionPosition, self.programCode)
                output = self.getParameter(instructionObject, 3, instructionPosition, self.programCode)
            else:
                firstInput = int(self.programCode[instructionPosition + 1])
                secondInput = int(self.programCode[instructionPosition + 2])
                try:
                    output = int(self.programCode[instructionPosition + 3])
                except IndexError:
                    output = 0

            if instruction == 1:
                self.programCode[output] = int(self.programCode[firstInput]) + int(self.programCode[secondInput])
                nextStep = instructionPosition + 4
            if instruction == 2:
                self.programCode[output] = int(self.programCode[firstInput]) * int(self.programCode[secondInput])
                nextStep = instructionPosition + 4
            if instruction == 3:
                self.programCode[firstInput] = inputParam
                inputParam = input2
                nextStep = instructionPosition + 2
            if instruction == 4:
                output = self.programCode[firstInput]
                print("Output is " + str(output))
                nextStep = instructionPosition + 2
            if instruction == 5:
                if int(self.programCode[firstInput]) != 0:
                    nextStep = int(self.programCode[secondInput])
                else:
                    nextStep = instructionPosition + 3
            if instruction == 6:
                if int(self.programCode[firstInput]) == 0:
                    nextStep = int(self.programCode[secondInput])
                else:
                    nextStep = instructionPosition + 3
            if instruction == 7:
                if int(self.programCode[firstInput]) < int(self.programCode[secondInput]):
                    self.programCode[output] = 1
                else:
                    self.programCode[output] = 0
                nextStep = instructionPosition + 4

            if instruction == 8:
                if int(self.programCode[firstInput]) == int(self.programCode[secondInput]):
                    self.programCode[output] = 1
                else:
                    self.programCode[output] = 0
                nextStep = instructionPosition + 4

            instruction = self.getNextInstruction(self.programCode[nextStep])
            instructionPosition = nextStep

        return output
