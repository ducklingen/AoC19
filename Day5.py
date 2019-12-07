from helpers import AoCHelper, IntcodeComputer

programToRun = AoCHelper.readInputCommaLine("day5input.txt")

IntcodeComputer.runProgram(programToRun, 5)
