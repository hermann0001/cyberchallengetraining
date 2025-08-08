import sys

def read_input(filename):         
    with open(filename, 'r') as file:
        N, M = map(int, file.readline().split())
        banned_strings = [file.readline().strip() for _ in range(M)]
        input_strings = [file.readline().strip() for _ in range(N)]

    return N, M, banned_strings, input_strings

def write_output(filename, results):
    with open(filename, 'wt+') as file:
        for r in results:
            file.write(f"{r}\n")

        
def check(N, M, banned_strings, input_strings):
    res = []
    safe = False
    for istring in input_strings:
        for string in banned_strings:
            if string in istring:
                safe = False
                break
            else:
                safe = True
        if safe == True:
            res.append("SAFE")
        else:
            res.append("BANNED")

    return res

if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print("Usage: python3 winner.py <input-filename>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    N, M, banned_strings, input_strings = read_input(input_file)

    res = check(N, M, banned_strings, input_strings)

    output_file = "output.txt"
    write_output(output_file, res)

        
        

