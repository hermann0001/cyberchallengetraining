# input:
#   line 1: N tasks, T duration of a round (time constraint)
#   line 2: N values representing the length of the tasks t1, ... , tN
# output:
#   W *minimum* number of workers that is necessary to execute all tasks
#
# note: task time cannot be split between workers

import os
import sys
import math


INPUT_PATH = "input/"
OUTPUT_PATH = "myoutput/"

def read_input(filename):
    with open(filename, 'r') as file:
        N, T = map(int, file.readline().split())
        tasks_time = [int(t) for t in file.readline().split()]
    return N, T, tasks_time

def write_output(filename, W):
    with open(filename, 'wt+') as file:
        file.write(f"{W}\n")

# bruteforce
def calculate(N, T, times, workers):
    time_tables = {}                # dictionary to assign for each worker the finish time

    print("initial guess:", workers)
    # step 1 - assign task to all workers

    for i in range(workers):
        time_tables[i] = times[i]

    # step 2 - find minimum time in the time table
    for i in range(workers, N):
        first_to_finish = min(time_tables, key=time_tables.get)

        # step 3 - assign the new task to the worker
        print("assegno task numero", i)
        if time_tables[first_to_finish] + times[i] >= T:
            return calculate(N, T, times, workers+1)
        else:
            time_tables[first_to_finish] += times[i]

    return workers         

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python workers.py <input filename>")
        sys.exit(1)
    input_file = os.path.join(INPUT_PATH, sys.argv[1])
    N, T, tasks_time = read_input(input_file)
    W = calculate(N, T, tasks_time, math.ceil(sum(tasks_time) / T))

    output_file = os.path.join(OUTPUT_PATH, "output.txt")
    write_output(output_file, W)
