opcode={"add":"00000","sub":"00001","movI":"00010","movR":"00011","ld":"00100","st":"00101","mul":"00110","div":"00111","rs":"01000","ls":"01001","xor":"01010","or":"01011","and":"01100","not":"01101","cmp":"01110","jmp":"01111","jlt":"11100","jgt":"11101","je":"11111","hlt":"11010"}


register = {"R0":"000","R1":"001","R2":"010","R3":"011","R4":"100","R5":"101","R6":"110","FLAGS":"111"}


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
    s1=bin(int(Imm))
    s1=s1[2::]
    print(s1)
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
def error_checker(filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
        instruction=[]
        listofline=enumerate(instruction,1)
        for line in (lines):
                line = line.strip().split()
                instruction.append(line)
        #print(instruction)

        opcodes=["add","sub","mov","ld","st","mul", "div","rs","ls","xor","or","and","not","cmp","jmp","jlt","jgt","je","hlt","var"]

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
                print(len(i)==0)
                # print(i[0][-1]==":")
                if len(i) != 0 and i[0][-1] == ":":
                        print("in side")
                        if i[0][:-1] in labellll.keys():
                                li.append("two label with same name")
                                print("two label with same name")
                        else:
                                print("in in side")
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

                elif i[0]=="add" or i[0]=="sub":
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
                                        if (i[1] in register.keys() and i[1]!="FLAGS" and (0 <= int(i[2][1:]) and int(i[2][1:]) <= 127) and i[2][0]=="$"):
                                                continue
                                        else:
                                                li.append(f"Error in line {instruction.index(i) + 1}: int value not defined / int value not in range / register name invalid ")
                                                

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
                        # print(1)
                        if len(i)!=3:
                                li.append(f"Error in Line {instruction.index(i) + 1}: rs / ls must contain 2 parameters ")
                        else:
                                # print(i[2])
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
                                                print("two label with same name")
                                        else:
                                                print("in in side")
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
