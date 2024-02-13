import os, sys

INPUT_PATH = "input/"
OUTPUT_PATH = "myoutput/"

def read_input(filename):

    # Create data structure to store all test case info
    # big data sandwich
    test_cases = []          

    with open(filename, 'r') as file:
        

    return T, test_cases

def write_output(filename, T):
    with open(filename, 'wt+') as file:
        


if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print("Usage: python3 winner.py <input-filename>")
        sys.exit(1)
    
    input_file = os.path.join(INPUT_PATH, sys.argv[1])
    T, test_cases_info = read_input(input_file)

    T = maketeam(test_cases_info)

    output_file = os.path.join(OUTPUT_PATH, "output.txt")
    write_output(output_file, T)

        
        

