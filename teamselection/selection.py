# INPUT: 
#   Line 1. T test cases
#   Line 2. N candidates, M players in a team, S set of skills
#   Line 3. list of M space-separated 3 characters representing skills name
#   Line 4 to 2+N(S+1) group of S+1 lines
#       Line 1. Unique id of candidate
#       Line 2 to S+1: skill name and skill score space-separated
# OUTPUT:
#   T positive integers, one for each line, representing maximum global score

import os, sys

INPUT_PATH = "input/"
OUTPUT_PATH = "myoutput/"

def read_input(filename):

    # Create data structure to store all test case info
    # big data sandwich
    test_cases = []          

    with open(filename, 'r') as file:
        # Line 1
        T = int(file.readline())

        for i in range(T):    
            N, M, S = map(int, file.readline().split())
            skills_required = file.readline().split() 
            
            # store {pid: {skill_name: skill_score}}
            players_info = {}
            for _ in range(N):
                pid = int(file.readline())
                players_info[pid] = {}

                for _ in range(S):
                    skill_name, skill_score  = file.readline().split()
                    players_info[pid][skill_name] = int(skill_score)

            test_cases.append((skills_required, players_info))

    return T, N, M, S, test_cases

def write_output(filename, T):
    with open(filename, 'wt+') as file:
        for value in range(T):
            file.write(f"{value}\n")


# so parallelizable...
def maketeam(test_cases_info):    
    print(type(test_cases_info))
    
    teamscore = (0)

    for skill in skills_required:
        # Read first skill required and make a group of every player who has it
        owners = {}

        for player in players_info:
            for player_skill, score in players_info[player].items():
                if player_skill in skills_required:
                    owners[player] = score

        # Retrieve the player with maximum skill score
        candidate, score = max(owners.items(), key=lambda x: x[1])
        teamscore += score


if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print("Usage: python3 winner.py <input-filename>")
        sys.exit(1)
    
    input_file = os.path.join(INPUT_PATH, sys.argv[1])
    T, N, M, S, test_cases_info = read_input(input_file)

    T = maketeam(test_cases_info)

    output_file = os.path.join(OUTPUT_PATH, "output.txt")
    write_output(output_file, T)

        
        

