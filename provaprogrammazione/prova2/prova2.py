import os, sys

def read_input(filename):         
    with open(filename, 'r') as file:
        N = int(file.readline().strip())
        codelines = [file.readline().strip() for _ in range(N)]
    return N, codelines

        

def write_output(filename, val):
    with open(filename, 'wt+') as file:
        file.write(f"{val}\n")

def eval(N, codelines):
    variables = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0}

    i = 0
    while i < len(codelines):
        instr = codelines[i].split()
        if instr[0] == 'add':
            variables[instr[1]] += int(instr[2])
        elif instr[0] == 'sub':
            variables[instr[1]] -= int(instr[2])
        elif instr[0] == 'mul':
            variables[instr[1]] *= int(instr[2])
        elif instr[0] == 'lab':
            pass
        elif instr[0] == 'jmp':
            if variables[instr[1]] == int(instr[2]):
                i = codelines.index('lab ' + instr[3])
        i += 1
            
    return sum(variables.values())

if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print("Usage: python3 winner.py <input-filename>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    N, codelines = read_input(input_file)

    val = eval(N, codelines)

    output_file = "output.txt"
    write_output(output_file, val)

        
        

