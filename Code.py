import Instruction
symbol = []
ins = []
label = []
loc = ""
def readCode():
   
    symb = open("SymbTable.txt", "w")
    locat = open("out_pass.txt", "w")
    with open("modiSIC.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            sep = line.split()
            if sep[1] == "START":
                loc = sep[2].zfill(4).upper()
                locat.write(f"{loc} \t {sep[0]} \t {sep[1]} \t {sep[2]}\n")
                continue
            if len(sep) == 2:
                ins.append(sep[0])
                label.append(sep[1])
                locat.write(f"{loc} \t {sep[0]} \t {sep[1]}\n")
            else:
                symbol.append(sep[0])
                ins.append(sep[1])
                label.append(sep[2])
                symb.write(f"{sep[0]} \t {loc}\n")
                locat.write(f"{loc} \t {sep[0]} \t {sep[1]} \t {sep[2]}\n")
            if ins[-1] == "RESB":
                loc = hex(int(loc, 16) + int(label[-1]))
            elif ins[-1] == "RESW":
                z = int(label[-1])
                loc = hex(int(loc, 16) + (z * 3))
            elif ins[-1] == "BYTE":
                length = len(label[-1]) - 3
                if label[-1][0] == 'X':
                    length = length / 2
                    loc = hex(int(loc, 16) + int(length))
                elif label[-1][0] == 'C':
                    loc = hex(int(loc, 16) + int(length))
            elif ins[-1] == "WORD":
                loc = hex(int(loc, 16) + 3)
            for i in range(len(Instruction.ins)):
                if ins[-1] == Instruction.ins[i]:
                    loc = hex(int(loc, 16) + int(Instruction.form[i],16))
            loc = str(loc[2:].zfill(4).upper())
    locat.close()
    symb.close()
    return loc