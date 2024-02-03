# input:
# l1. M, N, S, - M = players, N = tasks, S = submissions
# l2 - N+1. task-id (unique int 1:N),  correct flag (10 chars string), points (positive integer <=1000)
# lN+2 - N+S+1. player-id, task-id, flag submitted (10 chars string), timestamp  (positive integer up to 10^6)

# output: 
# M lines with two values, the i-th line contains player-id of the player in i-th position and score.

import os 

INPUT_PATH = "input/"
OUTPUT_PATH = "myoutput/"

class Task:
    def __init__(self, tid, flag, score):
        self.tid = tid              # task id
        self.flag = flag                  # flag string
        self.score = score          # score

class Submission: 
    def __init__(self, pid, tid, flag, timestamp):
        self.pid = pid              # player id
        self.tid = tid              # task id
        self.flag = flag                  # flag string
        self.timestamp = timestamp  # time of submission

    def __str__(self):
        return f"Submission: pid={self.pid}, tid={self.tid}, flag={self.flag}, timestamp={self.timestamp}"





def read_input(filename):
    tasks = []
    submissions = []
    
    with open(filename, 'r') as file:
        # Read line 1
        M, N, S = map(int, file.readline().split())

        # Read line 2 to line N + 1
        for _ in range(N):
            tid, flag, score = file.readline().split()
            tasks.append(Task(int(tid), flag, int(score)))
        
        # Read line N + 2 to N + S + 1
        for _ in range(S):
            pid, tid, flag, timestamp = file.readline().split()
            submissions.append(Submission(int(pid), int(tid), flag, int(timestamp)))

        # initialize score dict
        scores = {pid: 0 for pid in range(1, M+1)}


    return M, N, S, tasks, submissions, scores

def check(tasks, submissions, scores):
    task_completed = {}             # task completed by a player

    for s in submissions:
        # take the task associated for this submission
        task = next(t for t in tasks if t.tid == s.tid)

        # check if the player has solved this task before
        if s.pid not in task_completed:
            task_completed[s.pid] = set()

        if task.tid not in task_completed[s.pid]:
            # check correctness of flag
            if task.flag == s.flag:
                scores[s.pid] += task.score
                task_completed[s.pid].add(task.tid)

    tiebreak = lambda x: (
        x[1],                                                                                 # Desceding score points
        -next((sub.timestamp for sub in submissions if sub.pid == x[0] and x[1] > 0), 0),     # Ascending timestamp
        -x[0]                                                                                 # Asceding player-id
    )

    return dict(sorted(scores.items(), key=tiebreak, reverse=True))

def write_output(filename, final_scoreboard):
    with open(filename, "wt+") as file:
        for pid, score in final_scoreboard.items():
            file.write(f"{pid} {score}\n")


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python3 winner.py <filename>")
        sys.exit(1)
    input_file = os.path.join(INPUT_PATH, sys.argv[1])
    M, N, S, tasks, submissions, scores = read_input(input_file)
    final_scoreboard = check(tasks, submissions, scores)

    output_file = os.path.join(OUTPUT_PATH, "output.txt")
    write_output(output_file, final_scoreboard)