import Code
import Instruction
hte = open("HTE.txt", "w")
file2 = open("out_pass2.txt", "w")
def pass2(end):
    objectCode = []
    count = 0
    with open("out_pass.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            cpy = line
            flag = 0
            flag2 = 0
            sep = line.split()
            if not objectCode:
                start = sep[0]
            if len(sep) == 3:
                instIndex = 1
                operandIndex = 2
            else:
                instIndex = 2
                operandIndex = 3
            if sep[instIndex] == "START":
                end = hex(int(end,16) - int(sep[0],16))
                end = str(end[2:].zfill(6).upper())
                erec = sep[0].zfill(6)
                hte.write(f"H.{sep[1]}.{erec}.{end.zfill(6)}\n")
                file2.write(f"{line[:-1]}\n")
            if sep[instIndex] == "RESB" or sep[instIndex] == "RESW":
                file2.write(f"{line[:-1]}\n")
                if objectCode:
                    length = hex(count)
                    length = str(length[2:].zfill(2).upper())
                    hte.write(f"T.{start.zfill(6)}.{length}")
                    for i in objectCode:
                        hte.write(f".{i}")
                    hte.write("\n")
                    objectCode.clear()
                    count = 0
                continue
            if sep[instIndex] == "BYTE":
                if sep[operandIndex][0] == "X":
                    temp = sep[operandIndex][2:-1]
                    count += len(temp)
                    objectCode.append(temp)
                    file2.write(f"{line[:-1]}\t\t{temp}\n")
                    continue
                elif sep[operandIndex][0] == "C":
                    temp = ""
                    for i in sep[operandIndex][2:-1]:
                        x = str(hex(ord(i)))
                        x = str(x[2:].upper())
                        temp += x
                    count += len(temp)
                    objectCode.append(temp)
                    file2.write(f"{line[:-1]}\t\t{temp}\n")
                    continue
            if sep[instIndex] == "WORD":
                temp = hex(int(sep[operandIndex]))
                temp = str(temp[2:].zfill(6).upper())
                count += 6
                objectCode.append(temp)
                file2.write(f"{line[:-1]}\t\t{temp}\n")
                continue
            for i in range(len(Instruction.ins)):
                if sep[instIndex] == Instruction.ins[i]:
                    if Instruction.form[i] == "1":
                        objectCode.append(Instruction.opcode[i].zfill(2))
                        count += 2
                        break
                    else:
                        count += 6
                        temp = Instruction.opcode[i]
                        if sep[operandIndex][0] == "#":
                            temp = hex(int(temp,16) + 1)
                            temp = str(temp[2:].zfill(2).upper())
                            sep[operandIndex] = sep[operandIndex][1:]
                        if sep[operandIndex][-2:] == ",X":
                            flag = 1
                            sep[operandIndex][:-2]
                        with open("SymbTable.txt", "r") as file:
                            lines = file.readlines()
                            for line in lines:
                                sep2 = line.split()
                                if sep[operandIndex] == sep2[0]:
                                    temp2 = sep2[1]
                                    flag2 = 1
                        if flag == 1:
                            temp2 = hex(int(sep[0], 16) + 4)
                            temp2 = str(temp2[2:].zfill(4).upper())
                        if flag2 == 1:
                            temp += temp2
                            objectCode.append(temp)
                            file2.write(f"{cpy[:-1]}\t\t{temp}\n")
                        else:
                            if sep[instIndex] == "RSUB":
                                temp = "4C0000"
                                objectCode.append(temp)
                                file2.write(f"{cpy[:-1]}\t\t{temp}\n")
                            else:
                                temp2 = hex(int(sep[operandIndex]))
                                temp2 = str(temp2[2:].zfill(4).upper())
                                temp += temp2
                                objectCode.append(temp)
                                file2.write(f"{cpy[:-1]}\t\t{temp}\n")
                        if count > 25:
                            length = hex(count)
                            length = str(length[2:].zfill(2).upper())
                            hte.write(f"T.{start.zfill(6)}.{length}")
                            for i in objectCode:
                                hte.write(f".{i}")
                            hte.write("\n")
                            objectCode.clear()
                            count = 0
    if objectCode:
        length = hex(count)
        length = str(length[2:].zfill(2).upper())
        hte.write(f"T.{start.zfill(6)}.{length}")
        for i in objectCode:
            hte.write(f".{i}")
        hte.write("\n")
        objectCode.clear()
    hte.write(f"E.{erec.zfill(6)}")




