opcode={"add":"00000","sub":"00001","movI":"00010","movR":"00011","ld":"00100","st":"00101","mul":"00110","div":"00111","rs":"01000","ls":"01001","xor":"01010","or":"01011","and":"01100","not":"01101","cmp":"01110","jmp":"01111","jlt":"11100","jgt":"11101","je":"11111","hlt":"11010","movf":"10010","subf":"10001","addf":"10000"}


register = {"R0":"000","R1":"001","R2":"010","R3":"011","R4":"100","R5":"101","R6":"110","FLAGS":"111"}
k=0
def move_decimal_left(decimal_str, n):
    # Remove the decimal point from the string
    ind=decimal_str.index(".")
    # print(ind)
    n=ind-n
    global k
    # print(n)
    k=n
    decimal_str = decimal_str.replace('.', '')

    # Insert the decimal point n places from the left
    shifted_decimal_str = decimal_str[:n] + '.' + decimal_str[n:]

    return shifted_decimal_str

def manti(decimal_num):
    # Convert the whole number part to binary
    whole_number = int(decimal_num)
    # print(whole_number)
    binary_whole = bin(whole_number)[2:]  # Remove the '0b' prefix
    print(binary_whole)
    # Convert the fractional part to binary
    fractional_part = decimal_num - whole_number
    binary_fractional = ''
    while fractional_part != 0:
        fractional_part *= 2
        bit = int(fractional_part)
        binary_fractional += str(bit)
        fractional_part -= bit
    # print(fractional_part)
    # Normalize the binary fraction
    binary = binary_whole + '.' + binary_fractional
    binary_normalized = binary.lstrip('0')
    print(binary_normalized)
    # Determine the exponent
    shifted_places = len(binary_whole) - 1
    print(shifted_places)
    exponent = shifted_places + 3  # Adjusted exponent with bias of 3

    # Convert the exponent to binary
    binary_exponent = bin(exponent)[2:].zfill(3)
    # print(binary_exponent)
    # Extract the mantissa
    # print(binary_normalized)
    binary_normalized=move_decimal_left(binary_normalized,shifted_places)
    # print(binary_normalized)
    # print(binary_normalized.replace('.', ''))
    # print(binary_normalized)
    # print(k)
    mantissa = binary_normalized[k+1::]
    # print(mantissa)
    # Combine the parts
    binary_representation = binary_exponent + mantissa

    return binary_representation


def isfloat(num):
    try:
        float(num)
        return False
    except ValueError:
        return True

def typeF():#halt
    return "1101000000000000"

def binn(a,n):
    binary=bin(a)[2:]
    return binary.zfill(n)

def typeA(op,reg):
    s=""
    s+=opcode[op]
    s+="00"
    s+=register[reg[0]]
    s+=register[reg[1]]
    s+=register[reg[2]]
    return s

def typeE(op,mem_index):
    s=""
    s+=opcode[op]
    s+="0000"
    s+=mem_addr[mem_index]
    return s

def typeD(op,reg,mem_index):
    s=""
    s+=opcode[op]
    s+="0"
    s+=register[reg[0]]
    s+=mem_addr[mem_index]
    return s

def typeC(op,reg):
    s=""
    s+=opcode[op]
    s+="00000"
    s+=register[reg[0]]
    s+=register[reg[1]]
    return s

def typeB(op,reg,Imm):
    s=""
    s+=opcode[op]
    s+="0"
    s+=register[reg[0]]
    if op=="mov":
        s1=bin(int(Imm))
        s1=s1[2::]
    else :
        si=str(manti(int(Imm)))
    #print(s1)
    t=7-len(s1)
    s2=""
    if t==6:
        for i in range(6):
            s2+="0"
    elif t==5:
        for i in range(5):
            s2+="0"
    elif t==4:
        for i in range(4):
            s2+="0"
    elif t==3:
        for i in range(3):
            s2+="0"
    elif t==2:
        for i in range(2):
            s2+="0"
    elif t==1:
        for i in range(1):
            s2=s2+"0"
    s1=s2+s1
    s+=s1
    return s



def for_label(op,lab):
    s=""
    s+=opcode[op]
    s+="0000"
    s+=labellll[lab]
    return s



labellll={}
def error_checker(lines):
        
        instruction=[]
        # listofline=enumerate(instruction,1)
        for line in (lines):
                line = line.strip().split()
                instruction.append(line)
        ##print(instruction)

        opcodes=["add","sub","mov","ld","st","mul", "div","rs","ls","xor","or","and","not","cmp","jmp","jlt","jgt","je","hlt","var","addf","subf","movf"]

        variables=[]

        registers=["R0",
          "R1",
          "R2",
          "R3",
          "R4",
          "R5",
          "R6","FLAGS"]

        labels=[]

        NE=0
        t=0
        instruction=[q for q in instruction if q!=""]
        for i in instruction:
                #print(len(i)==0)
                # #print(i[0][-1]==":")
                if len(i) != 0 and i[0][-1] == ":":
                        #print("in side")
                        if i[0][:-1] in labellll.keys():
                                li.append("two label with same name")
                                #print("two label with same name")
                        else:
                                #print("in in side")
                                labellll[i[0][0:-1]]=binn(instruction.index(i)-len(variables),7)
                if len(i)==0:
                    # pass
                        continue

                elif i[0]=="var":
                        if t==1:
                               li.append(f"Error in line {instruction.index(i)+1}:Variables must be declared at the very beginning")
                               continue
                        else:
                                if len(i)!=2:
                                       li.append(f"Error in line {instruction.index(i) + 1}: Varibale definition not proper")
                                else:
                                       variables.append(i[1])
                                       continue

                elif i[0]=="add" or i[0]=="sub" or i[0]=="addf" or i[0]=="subf":
                        t=1
                        if len(i)!=4:
                                li.append(f"Error in Line {instruction.index(i) + 1}: add must contain 3 parameters ")
                                if (len(i)==3 and i[1] in register.keys() and i[1]!="FLAGS" and ((i[2][1:])).isdigit() and i[2][0]=="$"):
                                        li.append(f"Error in Line {instruction.index(i) + 1}: cannot add value of register and an integer ")
                                        #isa doesnt support addition of int and reg values unlike in the test case 1.
                                

                        else:
                                if i[1] in register.keys() and i[1]!="FLAGS" and i[2] in register.keys() and i[3] in register.keys()  :
                                        continue

                                else:
                                        li.append(f"Error in line {instruction.index(i) + 1}: A register can only be of type R0/1/2/3/4/5/6")
                elif i[0]=="movf":
                    if len(i)!=3:
                        li.append(f"Error in Line {instruction.index(i) + 1}: mov must contain 2 parameters ")
                        
                    if isfloat(i[2][1::]):
                        li.append(f"Error in Line {instruction.index(i) + 1}: movf dose not have float value")
                        
                elif i[0]=="mov":
                        t=1
                        if len(i)!=3:
                                li.append(f"Error in Line {instruction.index(i) + 1}: mov must contain 2 parameters ")
                        else:
                                
                                if not(i[2][1::].isdigit()):
                                        if (i[1] in register.keys() and i[1]!="FLAGS"  and i[2] in register.keys()):
                                                continue
                                        else:
                                               li.append(f"Error in line {instruction.index(i) + 1}: Register can be of type R0/1/2/3/4/5/6")
                                               continue
                                        
                                else:
                                        if (i[1] in register.keys() and i[1]!="FLAGS" and (0 <= int(i[2][1:]) and int(i[2][1:]) <= 127)):
                                                continue
                                        else:
                                                li.append(f"Error in line {instruction.index(i) + 1}: int value not defined / int value not in range / register name invalid ")
                                                # continue


                elif i[0]=="ld" or i[0]=="st":
                        t=1
                        if len(i)!=3:
                                li.append(f"Error in Line {instruction.index(i) + 1}: ld and st must contain 2 parameters ")
                        else:
                                if (i[1] in register.keys() and i[1]!="FLAGS" and i[2] in variables):
                                        continue
                                else:
                                        if i[2] not in variables:
                                                li.append(f"Error in line {instruction.index(i) + 1}: No variable named '{i[2]}' ")
                                        if i[1] not in register.keys():
                                                li.append(f"Error in line {instruction.index(i) + 1}: No register named '{i[1]}' ")
                

                elif i[0]=="mul" or i[0]=="div":
                        t=1
                        if i[0]=="mul":
                                if len(i)!=4:
                                        li.append(f"Error in Line {instruction.index(i) + 1}: mul must contain 3 parameters ")
                                else:
                                        if i[1] in register.keys() and i[1]!="FLAGS" and i[2] in register.keys() and i[2]!="FLAGS" and i[3] in register.keys() and i[3]!="FLAGS" :
                                                continue
                                        else:
                                                li.append(f"Error in line {instruction.index(i) + 1}: Registers can only be of type R0/1/2/3/4/5/6")
                                                
                        elif i[0]=="div":
                                if len(i)!=3:
                                        li.append(f"Error in Line {instruction.index(i) + 1}: div must contain 3 parameters ")
                                else:
                                        if i[1] in register.keys()  and i[1]!="FLAGS" and i[2] in register.keys() and i[2]!="FLAGS":
                                                continue
                                        else:
                                                li.append(f"Error in line {instruction.index(i) + 1}: Registers can only be of type R0/1/2/3/4/5/6")
                
                elif i[0]=="rs" or i[0]=="ls":
                        t=1
                        # #print(1)
                        if len(i)!=3:
                                li.append(f"Error in Line {instruction.index(i) + 1}: rs / ls must contain 2 parameters ")
                        else:
                                # #print(i[2])
                                if i[1] in register.keys() and i[1]!="FLAGS" and (0 <= int(i[2][1::]) and int(i[2][1::]) <= 127) :
                                        continue
                                else:
                                        li.append(f"Error in line {instruction.index(i) + 1}: Registers name not valid / int not in range")

                elif i[0]=="xor" or i[0]=="or" or i[0]=="and":
                        t=1
                        if len(i)!=4:
                                li.append(f"Error in Line {instruction.index(i) + 1}: xor/or/and must contain 3 parameters ")
                        else:
                                if i[1] in register.keys() and i[1]!="FLAGS" and i[2] in register.keys() and i[2]!="FLAGS" and i[3] in register.keys() and i[3]!="FLAGS" :
                                        continue
                                else:
                                        li.append(f"Error in line {instruction.index(i) + 1}: Registers can only be of type R0/1/2/3/4/5/6")

                elif i[0]=="not" or i[0]=="cmp":
                        t=1
                        if len(i)!=3:
                                li.append(f"Error in Line {instruction.index(i) + 1}: not / cmp must contain 2 parameters ")
                        else:
                                if i[1] in register.keys() and i[1]!="FLAGS" and i[2] in register.keys() and i[2]!="FLAGS" :
                                        continue
                                else:
                                        li.append(f"Error in line {instruction.index(i) + 1}: Registers can only be of type R0/1/2/3/4/5/6")

                elif i[0]=="jmp" or i[0]=="jlt" or i[0]=="jgt" or i[0]=="je":
                        t=1
                        if len(i)!=2:
                                li.append(f"Error in Line {instruction.index(i) + 1}: jump statements must contain 1 label ")
                        else:
                                labels.append(i[1])
                                w=1
                                
                                for q in instruction:
                                        
                                        if i[1]+":" in q:
                                               w+=1
                                        
                                if w<2:
                                       li.append(f"Error in Line {instruction.index(i) + 1}: No label named '{i[1]}' ")

                                               
                                

                elif i[0] in labels or i[0][-1]==":":
                        labels.append(i[0])
                        t=1
                        if i[0][-1]!=":":
                                li.append(f"Error in Line {instruction.index(i) + 1}: labels must end with ':' and no spaces are allowed in between ")
                        else:
                                j=[a for a in i[1:]]
                                ###
                                if j[0][-1] == ":" and len(j) != 0:
                                        
                                        if j[0][:-1] in labellll.keys():
                                                li.append("two label with same name")
                                                #print("two label with same name")
                                        else:
                                                #print("in in side")
                                                labellll[j[0][0:-1]]=binn(instruction.index(i)-len(variables),7)
                                if len(j)==0:
                                # pass
                                        continue

                                elif j[0]=="var":
                                        if t==1:
                                                li.append(f"Error in line {instruction.index(i)+1}:Variables must be declared at the very beginning")
                                                continue
                                        else:
                                                if len(j)!=2:
                                                        li.append(f"Error in line {instruction.index(i) + 1}: Varibale definition not proper")
                                                else:
                                                        variables.append(j[1])
                                                        

                                elif j[0]=="add" or j[0]=="sub":
                                        t=1
                                        if len(j)!=4:
                                                li.append(f"Error in Line {instruction.index(i) + 1}: add must contain 3 parameters ")
                                                if (len(j)==3 and j[1] in register.keys() and j[1]!="FLAGS" and ((j[2][1:])).isdigit() and j[2][0]=="$"):
                                                        li.append(f"Error in Line {instruction.index(i) + 1}: cannot add value of register and an integer ")
                                                        #isa doesnt support addition of int and reg values unlike in the test case 1.
                                                

                                        else:
                                                if j[1] in register.keys() and j[1]!="FLAGS" and j[2] in register.keys() and j[2]!="FLAGS" and j[3] in register.keys() and j[3]!="FLAGS"  :
                                                        continue

                                                else:
                                                        li.append(f"Error in line {instruction.index(i) + 1}: A register can only be of type R0/1/2/3/4/5/6")
                                                        
                                elif j[0]=="mov":
                                        t=1
                                        if not(j[2][1::].isdigit()):
                                                if (j[1] in register.keys() and j[1]!="FLAGS" and j[2] in register.keys()):
                                                        continue
                                                else:
                                                        li.append(f"Error in line {instruction.index(i) + 1}: Register can be of type R0/1/2/3/4/5/6")
                                                        continue
                                                
                                        else:
                                                if (j[1] in register.keys() and j[1]!="FLAGS" and (0 <= int(j[2][1:]) and int(j[2][1:]) <= 127) and j[2][0]=="$"):
                                                        continue
                                                else:
                                                        li.append(f"Error in line {instruction.index(i) + 1}: int value not defined / int value not in range / register name invalid ")
                                elif j[0]=="ld" or j[0]=="st":
                                        t=1
                                        if len(j)!=3:
                                                li.append(f"Error in Line {instruction.index(i) + 1}: ld and st must contain 2 parameters ")
                                        else:
                                                if (j[1] in register.keys() and j[1]!="FLAGS" and j[2] in variables):
                                                        continue
                                                else:
                                                        if j[2] not in variables:
                                                                li.append(f"Error in line {instruction.index(i) + 1}: No variable named '{j[2]}' ")
                                                        if j[1] not in register.keys():
                                                                li.append(f"Error in line {instruction.index(i) + 1}: No register named '{j[1]}' ")
                                

                                elif j[0]=="mul" or j[0]=="div":
                                        t=1
                                        if j[0]=="mul":
                                                if len(j)!=4:
                                                        li.append(f"Error in Line {instruction.index(i) + 1}: mul must contain 3 parameters ")
                                                else:
                                                        if j[1] in register.keys() and j[1]!="FLAGS" and j[2] in register.keys() and j[2]!="FLAGS" and j[3] in register.keys() and j[3]!="FLAGS" :
                                                                continue
                                                        else:
                                                                li.append(f"Error in line {instruction.index(i) + 1}: Registers can only be of type R0/1/2/3/4/5/6")
                                                        
                                        elif j[0]=="div":
                                                if len(j)!=3:
                                                        li.append(f"Error in Line {instruction.index(i) + 1}: div must contain 3 parameters ")
                                                else:
                                                        if len(i)!=3:
                                                                li.append(f"Error in Line {instruction.index(i) + 1}: div must contain 3 parameters ")
                                                        else:
                                                                if j[1] in register.keys() and j[1]!="FLAGS" and j[2] in register.keys() and j[2]!="FLAGS":
                                                                        continue
                                                                else:
                                                                        li.append(f"Error in line {instruction.index(i) + 1}: Registers can only be of type R0/1/2/3/4/5/6")
                                        
                                elif j[0]=="rs" or j[0]=="ls":
                                        t=1
                                        # #print(1)
                                        if len(j)!=3:
                                                li.append(f"Error in Line {instruction.index(i) + 1}: rs / ls must contain 2 parameters ")
                                        else:
                                                # #print(j[2])
                                                if j[1] in register.keys() and j[1]!="FLAGS" and (0 <= int(j[2][1::]) and int(j[2][1::]) <= 127) :
                                                        continue
                                                else:
                                                        li.append(f"Error in line {instruction.index(i) + 1}: Registers name not valid / int not in range")


                                elif j[0]=="xor" or j[0]=="or" or j[0]=="and":
                                        t=1
                                        if len(j)!=4:
                                                li.append(f"Error in Line {instruction.index(i) + 1}: xor/or/and must contain 3 parameters ")
                                        else:
                                                if j[1] in register.keys() and j[1]!="FLAGS" and j[2] in register.keys() and j[2]!="FLAGS" and j[3] in register.keys() and j[3]!="FLAGS":
                                                        continue
                                                else:
                                                        li.append(f"Error in line {instruction.index(i) + 1}: Registers can only be of type R0/1/2/3/4/5/6")

                                elif j[0]=="not" or j[0]=="cmp":
                                        t=1
                                        if len(j)!=3:
                                                li.append(f"Error in Line {instruction.index(i) + 1}: not / cmp must contain 2 parameters ")
                                        else:
                                                if j[1] in register.keys() and j[1]!="FLAGS" and j[2] in register.keys() and j[2]!="FLAGS" :
                                                        continue
                                                else:
                                                        li.append(f"Error in line {instruction.index(i) + 1}: Registers can only be of type R0/1/2/3/4/5/6")

                                elif j[0]=="jmp" or j[0]=="jlt" or j[0]=="jgt" or j[0]=="je":
                                        t=1
                                        if len(j)!=2:
                                                li.append(f"Error in Line {instruction.index(i) + 1}: jump statements must contain 1 label ")
                                        else:
                                                labels.append(j[1])
                                elif j[0]=="hlt":
                                        t=1
                                        if len(j)!=1:
                                                li.append(f"Error in Line {instruction.index(i) + 1}: only hlt must be there and no additional statements")
                                

                                elif j[0][:-1] not in labels:
                                        t=1
                                        li.append(f"Error in line {instruction.index(i) + 1}: Invalid Operand; '{''.join(i)}' ")
                                continue


                elif i[0]=="hlt":
                        t=1
                        if len(i)!=1:
                                li.append(f"Error in Line {instruction.index(i) + 1}: only hlt must be there and no additional statements")
                

                elif i[0][:-1] not in labels:
                        t=1
                        li.append(f"Error in line {instruction.index(i) + 1}: Invalid Operand; '{''.join(i)}' ")

        r=0
        s=0
        # instruction=[q for q in instruction if q!=" "]
        #print(instruction)
        for u in instruction:
               if "hlt" in u:
                      r+=1
                      if instruction[-1]==u:
                             s+=1
        
        if ["hlt"] not in instruction and r==0:
                li.append(f"Error : No hlt instruction present ")
        elif instruction[-1]!=["hlt"] and s==0:
                li.append(f"Error : Halt must be the last instruction/ cannot execute after halt")
              
                                        


        if len(li)==0:
            NE=1
        else:
            NE=0

        return NE


##print()
# opfile = open("output.txt", "w")
# filename="code.txt"
stat = 0
no_line = 0
mem_addr={}
data=[]
while (True):
        try:
                w=input().strip()
                data.append(w)
                
        except EOFError:
                break
       
# with open("code.txt", "r") as instructions:
#     data = instructions.read().split('\n')
    ##print(data)
        # list of instructions split by new line
li=[]
NE=error_checker(data)
###print(li)

##print('labellll = ',labellll)
# ##print('ne = ',NE)
for i in range(len(li)):
        print(str(li[i])+'\n')
if NE == 0 :
        ##print("abborting")
        quit()

       
   
# FOR VARIABLE DEFINITION
bk = 0
for line in data:
    # if bk == 1:
    #     break
    line = line.split()
    # ##print("data",line)
    no_line = no_line + 1
    stat = stat + 1
    if line[0] != "var":
        no_line=no_line-1
        bk=1
        break
    else:
        mem_addr[line[1]] = binn(len(mem_addr)+1+len(register)+len(labellll), 7)
for a in mem_addr.keys():
       mem_addr[a]=binn(list(mem_addr.keys()).index(a)+1+len(data)-stat,7)
for line in data[stat-1:]:
    ##print('##### ',line) #######################
    ##print(line.split()[0][0:-1] in labellll.values())
    ##print(line.split()[0][0:-1],labellll.values())
    no_line=no_line+1
    if line.split()[0]=="jmp" or line.split()[0]=="jlt" or line.split()[0]=="jgt" or line.split()[0]=="je":
        print(for_label(line.split()[0],line.split()[1])+"\n")
    elif line.split()[0][0:-1] in labellll.keys():
        #print("vaibhav")
        ###################################################
        lin=line.split(':')[1]
        #print(lin)
        #print('lin = ',lin)
        if lin == "hlt" or lin.split()[-1]=="hlt":
            print(typeF() + '\n')
        elif lin == '':
            pass
        else:
            no_of_rasis = 0
            resis_l = []
            imm = -1
            mem_val_c = 0
            line_part = lin.split()
            for instr_split in range(len(line_part)):
                # #print('aa', line_part[instr_split][0])
                if line_part[instr_split]=="\n":
                       #print(1)
                       continue
                elif instr_split == 0:
                    op = line_part[0]
                elif line_part[instr_split][0] != '$':
                    # #print(line_part[instr_split])
                    # #print(mem_addr.keys())
                    # #print(line_part[instr_split] in mem_addr.keys())
                    if line_part[instr_split] in mem_addr.keys():

                        mem_val = line_part[instr_split]
                        mem_val_c = 1
                    elif line_part[instr_split] not in register.keys():
                        #print("register value error in line",no_line)
                        #print("A register can be one of R0, R1, ... R6, and FLAGS only ")
                        #print("value given",line_part[instr_split])
                        NE=1
                    else:
                        no_of_rasis = no_of_rasis + 1
                        resis_l.append(line_part[instr_split])
                else:
                    if int(imm) >= 128:
                        #print('RunTimeError immediate value OVERFLOW in line', line, 'column',instr_split)
                        #print('Expected value -1<,128> got value', imm)
                        NE=1
                        for a in lin:
                            #print(a, end=' ')
                                quit()
                    elif imm == 0:
                        #print('RunTimeError immediate value NEGATIVE in line', line, 'column', instr_split,)
                        #print('Expected value -1<,128> got value', imm)
                        NE=1
                        for a in line:
                            #print(a, end=' ')
                                quit()
                    imm = line_part[instr_split][1:]
            if NE == 1:
                if no_of_rasis == 3:
                    print(typeA(op, resis_l) + '\n')
                elif no_of_rasis == 1 and imm != -1:
                    if op.replace(" ","") =='mov':
                        op = "movI"
                    print(typeB(op, resis_l, imm) + '\n')
                elif no_of_rasis == 2:
                    if op=='mov':
                        op="movR"
                    print(typeC(op, resis_l) + '\n')
                elif mem_val_c == 1 and no_of_rasis == 1:
                    print(typeD(op, resis_l, mem_val) + '\n')
                elif no_of_rasis == 0 and mem_val_c == 1:
                    print(typeE(op, mem_val)+'\n')   
        ###################################################
    elif line == "hlt":
        print(typeF() + '\n')
    elif line == '':
        pass
    else:
        no_of_rasis = 0
        resis_l = []
        imm = -1
        mem_val_c = 0
        line_part = line.split()
        for instr_split in range(len(line_part)):
            # #print('aa', line_part[instr_split][0])

            if instr_split == 0:
                op = line_part[0]
            elif line_part[instr_split][0] != '$':
                # #print(line_part[instr_split])
                # #print(mem_addr.keys())
                # #print(line_part[instr_split] in mem_addr.keys())
                if line_part[instr_split] in mem_addr.keys():

                    mem_val = line_part[instr_split]
                    mem_val_c = 1
                elif line_part[instr_split] not in register.keys():
                    #print("register value error in line",no_line)
                    #print("A register can be one of R0, R1, ... R6, and FLAGS only ")
                    #print("value given",line_part[instr_split])
                    NE=1
                else:
                    no_of_rasis = no_of_rasis + 1
                    resis_l.append(line_part[instr_split])
            else:
                if int(imm) >= 128:
                    #print('RunTimeError immediate value OVERFLOW in line', line, 'column',instr_split)
                    #print('Expected value -1<,128> got value', imm)
                    NE=1
                    for a in line:
                        #print(a, end=' ')
                        quit()
                elif imm == 0:
                    #print('RunTimeError immediate value NEGATIVE in line', line, 'column', instr_split,)
                    
                    NE=1
                    for a in line:
                        #print(a, end=' ')
                        quit()
                imm = line_part[instr_split][1:]
        if NE == 1:
            if no_of_rasis == 3:
                print(typeA(op, resis_l) + '\n')
            elif no_of_rasis == 1 and imm != -1:
                if op.replace(" ","") =='mov':
                    op = "movI"
                print(typeB(op, resis_l, imm) + '\n')
            elif no_of_rasis == 2:
                if op=='mov':
                    op="movR"
                print(typeC(op, resis_l) + '\n')
            elif mem_val_c == 1 and no_of_rasis == 1:
                print(typeD(op, resis_l, mem_val) + '\n')
            elif no_of_rasis == 0 and mem_val_c == 1:
                print(typeE(op, mem_val)+'\n')

#output
