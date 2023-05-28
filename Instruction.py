ins = []
form = []
opcode = []
def readInst():
    with open("InstructionSet.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            sep = line.split(" ")
            ins.append(sep[0])
            form.append(sep[1])
            opcode.append(sep[2][:-1])