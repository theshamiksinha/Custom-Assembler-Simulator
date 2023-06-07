register = ["0000000000000000"]*7
flags=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def binarytodecimal(str):
    decimal = int(str, 2)
    return decimal

def decimal_to_binary(decimal):
    binary = format(decimal, '016b')
    return binary
def bitwise_or(binary1, binary2):

    #bitwise OR operation
    result = ''
    for bit1, bit2 in zip(binary1, binary2):
        if bit1 == '1' or bit2 == '1':
            result += '1'
        else:
            result += '0'

    return result
def bitwise_and(binary1, binary2):
    #bitwise AND operation
    result = ''
    for bit1, bit2 in zip(binary1, binary2):
        if bit1 == '1' and bit2 == '1':
            result += '1'
        else:
            result += '0'

    return result
def bitwise_not(binary):
    #bitwise NOT operation
    result = ''
    for bit in binary:
        if bit == '1':
            result += '0'
        else:
            result += '1'

    return result



MEM = ["0000000000000000"] * 128

data = []
while (True):
        try:
                w=input().strip()
                data.append(w)
                
        except EOFError:
                break

t=0;
for i in data:
    i.strip("\n")
    # print(i.strip("\n"))
    MEM[t] = i.strip("\n")
    t+=1

# print(data)


programcounter = 0
printcounter=0
# print(MEM)
while MEM[programcounter]!="1101000000000000":
    current_instruction=MEM[programcounter]

    i=programcounter

    #! add operation 
    if MEM[i][0:5:1] == "00000":                                 #! ADD FUNCTION
        c = binarytodecimal(MEM[i][7:10:1])
        a = binarytodecimal(MEM[i][10:13:1])
        b = binarytodecimal(MEM[i][13:16:1])
        result=binarytodecimal(register[a])+binarytodecimal(register[b])
        
        if result >=128:
            flags[12] = 1
            register[c]="0000000000000000"
            flags=[0 for k in flags]
        else:
            result=decimal_to_binary(result)
            register[c]=result
            flags=[0 for k in flags]
    elif MEM[i][0:5:1]=="00001":                                #!SUBTRACT
        a=binarytodecimal(MEM[i][7:10:1])
        b=binarytodecimal(MEM[i][10:13:1])
        c=binarytodecimal(MEM[i][13:16:1])
        
        result=binarytodecimal(register[a])-binarytodecimal(register[b])
        # print(result)
        if result>=0:
            result=decimal_to_binary(result)
            register[a]=result
            flags=[0 for k in flags]
        elif result<0:
            flags[12] = 1
            register[c]="0000000000000000"
            flags=[0 for k in flags]

    elif MEM[i][0:5:1] == "00110":                               #! MULTIPLICATION
        c = binarytodecimal(MEM[i][7:10:1])
        a = binarytodecimal(MEM[i][10:13:1])
        b = binarytodecimal(MEM[i][13:16:1])
        result=binarytodecimal(register[a])*binarytodecimal(register[b])
        
        if result >=128:
            flags[12] = 1
            register[c]="0000000000000000"
            flags=[0 for k in flags]
        else:
            result=decimal_to_binary(result)
            register[c]=result
            flags=[0 for k in flags]
    elif MEM[i][0:5:1] == "00111":                               #! DIVIDE
        c = binarytodecimal(MEM[i][10:13:1])
        a = binarytodecimal(MEM[i][13:16:1])
        if  binarytodecimal(register[a])==0:
            print("OVERFLOW")
            flags[12] = 1
            register[0]="0000000000000000"
            register[1]="0000000000000000"
            flags=[0 for k in flags]
        else:
            register[0]=decimal_to_binary((binarytodecimal(register[c]))//(binarytodecimal(register[a])))
            register[1]=decimal_to_binary((binarytodecimal(register[c]))%(binarytodecimal(register[a])))
            flags=[0 for k in flags]
    elif MEM[i][0:5:1] == "01011":                               #! OR
        c = binarytodecimal(MEM[i][7:10:1])
        a = binarytodecimal(MEM[i][10:13:1])
        b = binarytodecimal(MEM[i][13:16:1])
        result=binarytodecimal(bitwise_or(register(a),register(b)))
        
        
        result=decimal_to_binary(result)
        register[c]=result
        flags=[0 for k in flags]
    elif MEM[i][0:5:1] == "01100":                               #! AND
        c = binarytodecimal(MEM[i][7:10:1])
        a = binarytodecimal(MEM[i][10:13:1])
        b = binarytodecimal(MEM[i][13:16:1])
        result=binarytodecimal(bitwise_and(register[a],register[b]))
        
        result=decimal_to_binary(result)
        register[c]=result
        flags=[0 for k in flags]
    elif MEM[i][0:5:1] == "01101":                               #! Invert not function
        c = binarytodecimal(MEM[i][10:13:1])
        a = binarytodecimal(MEM[i][13:16:1])
        result=binarytodecimal(bitwise_not(register[a]))
        result=decimal_to_binary(result)
        register[c]=result
        flags=[0 for k in flags]
    elif MEM[i][0:5:1] == "01010":                               #! XOR
        c = binarytodecimal(MEM[i][7:10:1])
        a = binarytodecimal(MEM[i][10:13:1])
        b = binarytodecimal(MEM[i][13:16:1])
        result=binarytodecimal(str(int(register[a])^int(register[b])))
        
        result=decimal_to_binary(result)
        register[c]=result
        flags=[0 for k in flags]
    
    elif MEM[i][0:5:1] == "01110":                               #! COMPARE
        C = binarytodecimal(MEM[i][10:13:1])
        A = binarytodecimal(MEM[i][13:16:1])
        c=register[C]
        a=register[A]
        if c<a:
            flags[13]=1
        elif c>a:
            flags[14]=1
        else:
            flags[15]=1

    elif MEM[i][0:5:1] == "01000":                               #! RIGHT SHIFT
        c = binarytodecimal(MEM[i][6:9:1])
        a = int(binarytodecimal(MEM[i][9:16:1]))
        register[c]=decimal_to_binary(binarytodecimal(register[c])>>a)
        flags=[0 for k in flags]
    elif MEM[i][0:5:1] == "01001":                               #! LEFT SHIFT
        c = binarytodecimal(MEM[i][6:9:1])
        a = int(binarytodecimal(MEM[i][9:16:1]))
        register[c]=decimal_to_binary(binarytodecimal(register[c])<<a)
        flags=[0 for k in flags]

    elif MEM[i][0:5:1] == "00010": #MOV IMMEDIATE
        a = binarytodecimal(MEM[i][6:9:1])
        b = binarytodecimal(MEM[i][9:16:1])
        
        register[a]=decimal_to_binary(b)
        flags=[0 for k in flags]
        

    elif MEM[i][0:5:1] == "00011": #MOV REGISTER
        a = binarytodecimal(MEM[i][10:13:1])
        b = binarytodecimal(MEM[i][13:16:1])
        if b==7:
            s1=''
            for j in range(len(flags)):
                s1+=str(flags[j])
            register[a]=s1
            flags=[0 for k in flags]
        else:
            register[a]=register[b]
            flags=[0 for k in flags]
    elif MEM[i][0:5:1] == "00100": #LOAD
        a = binarytodecimal(MEM[i][6:9:1])
        b = binarytodecimal(MEM[i][9:16:1])
        register[a]=MEM[b]
        flags=[0 for k in flags]

    elif MEM[i][0:5:1] == "00101": #STORE
        a = binarytodecimal(MEM[i][6:9:1])
        b = binarytodecimal(MEM[i][9:16:1])
        MEM[b]=register[a]
        # print(MEM[b])
        flags=[0 for k in flags]

    elif MEM[i][0:5:1] == "01111": #UNCONDITIONAL JUMP
        a = binarytodecimal(MEM[i][9:16:1])
        flags=[0 for k in flags]
        print(decimal_to_binary(programcounter)[9::],end='        ')
        for i in range(len(register)):
            print(register[i],end=" ")
        s=''
        for j in range(len(flags)):
            s+=str(flags[j])
        print(s)
        programcounter=a           
        # flags=[0 for k in flags]
        continue


    elif MEM[i][0:5:1] == "11100": #JUMP elif LESS THAN
        # print("vkakmefvsenbnsr")
        a = binarytodecimal(MEM[i][9:16:1])
        # print(a)
        if flags[13]==1:
            flags=[0 for k in flags]
            print(decimal_to_binary(programcounter)[9::],end='        ')
            for i in range(len(register)):
                print(register[i],end=" ")
            s=''
            for j in range(len(flags)):
                s+=str(flags[j])
            print(s)
            programcounter=a           
            continue
        else:
            flags=[0 for k in flags]

    elif MEM[i][0:5:1] == "11101": #JUMP IF GREATER THAN
        a = binarytodecimal(MEM[i][9:16:1])
        # print(a)
        if flags[14]==1:
            flags=[0 for k in flags]
            print(decimal_to_binary(programcounter)[9::],end='        ')
            for i in range(len(register)):
                print(register[i],end=" ")
            s=''
            for j in range(len(flags)):
                s+=str(flags[j])
            print(s)
            programcounter=a           
            continue

        else:
            flags=[0 for k in flags]

    elif MEM[i][0:5:1] == "11111": #JUMP IF EQUAL TO
        a = binarytodecimal(MEM[i][9:16:1])
        if flags[15]==1:
            flags=[0 for k in flags]
            print(decimal_to_binary(programcounter)[9::],end='        ')
            for i in range(len(register)):
                print(register[i],end=" ")
            s=''
            for j in range(len(flags)):
                s+=str(flags[j])
            print(s)
            programcounter=a           
            # flags=[0 for k in flags]
            continue
        else:
            flags=[0 for k in flags]
    print(decimal_to_binary(programcounter)[9::],end='        ')
    for i in range(len(register)):
        print(register[i],end=" ")
    s=''
    for j in range(len(flags)):
        s+=str(flags[j])
    print(s)
    programcounter+=1

print(decimal_to_binary(programcounter)[9::],end='        ')
for i in range(len(register)):
    print(register[i],end=" ")
s=''
for j in range(len(flags)):
        s+=str(flags[j])
print(s)
for i in range(len(MEM)):
    print(MEM[i])
