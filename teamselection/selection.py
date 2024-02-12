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

    return T, test_cases

def write_output(filename, T):
    with open(filename, 'wt+') as file:
        #print(T, type(T))
        for value in T:
            file.write(f"{value}\n")


# so parallelizable...
def maketeam(test_cases_info):

    final_scores = []

    for skills_required, team_info in test_cases_info:
        #print("skills required", skills_required)
        players_unassigned = team_info.keys()
        skill2occ = {}
        for s in skills_required:
            skill2occ[s] = skills_required.count(s)
        
        #print(skill2occ)

        owners = {}
        selections = []
        for s, occ in skill2occ.items():
            owners[s] = list()
            #print("searching for players with:", s)
            for pid, skill in team_info.items():
                # if player has the skill searched
                if s in skill:
                    owners[s].append((pid, skill[s]))

            # sort skill score descend            
            owners[s].sort(key=lambda x: x[1], reverse=True)

            # pick players
            print(players_unassigned)
            print("skill required:", s, owners[s])
            print(occ)
            for i in range(occ):
                selections.append(owners[s][i])
            
        final_scores.append(sum(tupla[1] for tupla in selections))

    return final_scores    

if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print("Usage: python3 winner.py <input-filename>")
        sys.exit(1)
    
    input_file = os.path.join(INPUT_PATH, sys.argv[1])
    T, test_cases_info = read_input(input_file)

    T = maketeam(test_cases_info)

    output_file = os.path.join(OUTPUT_PATH, "output.txt")
    write_output(output_file, T)

        
        

