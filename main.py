mem = [0]*30000
ctr = 0

program = '''
,>,<.>.
'''

for i in program:
    if i == '+':
        if mem[ctr] == 255:
            mem[ctr] = 0
        else:
            mem[ctr] += 1
    elif i == '-':
        if mem[ctr] == 0:
            mem[ctr] = 255
        else:
            mem[ctr] -= 1
    elif i == '>':
        ctr += 1
    elif i == '<':
        ctr -= 1
    elif i == '.':
        c = chr(mem[ctr])
        print(c, end="")
    elif i == ',':
        mem[ctr] = int(input())
    
