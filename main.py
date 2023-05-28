from Instruction import readInst
from Code import readCode
from Code2 import pass2


def main():
    readInst()
    end = readCode()
    pass2(end)

main()
