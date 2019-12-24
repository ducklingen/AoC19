from helpers import AoCHelper
from itertools import permutations

from helpers.IntcodeComputerObj import IntcodeComputer


def runDay7Program(input1, input2):
    programDefinition = AoCHelper.readInputCommaLine("day7input.txt")

    computer = IntcodeComputer(programDefinition)

    return computer.runProgram(input1, input2)


combinations = permutations([0, 1, 2, 3, 4])

maxThrust = 0

for c in combinations:
    outputA = runDay7Program(c[0], 0)
    outputB = runDay7Program(c[1], outputA)
    outputC = runDay7Program(c[2], outputB)
    outputD = runDay7Program(c[3], outputC)
    outputE = runDay7Program(c[4], outputD)

    if outputE > maxThrust:
        maxThrust = outputE

print(maxThrust)
