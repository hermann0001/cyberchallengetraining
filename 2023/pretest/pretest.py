import os

INPUT_PATH = "dataset/input/"
OUTPUT_PATH = "dataset/myoutput/"

def read_input(filename):
    with open(filename, 'r') as file:
        Q, N = map(int, file.readline().split())
        correct_answers = file.readline().strip()
        given_answers = [file.readline().strip() for _ in range(N)]
    return Q, N, correct_answers, given_answers

def write_output(filename, scores):
    with open(filename, 'wt+') as file:
        for score in scores:
            file.write(f"{score}\n")

def check(correct_answers, given_answers):
    return [sum(1 for g, c in zip(ga, correct_answers) if g == c) for ga in given_answers]

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python prestest2023.py <input filename>")
        sys.exit(1)

    input_file = os.path.join(INPUT_PATH, sys.argv[1])
    Q, N, correct_answers, given_answers = read_input(input_file)
    scores = check(correct_answers, given_answers)

    output_file = os.path.join(OUTPUT_PATH, "output.txt")
    write_output(output_file, scores)
