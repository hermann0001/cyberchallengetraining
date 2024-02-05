# input:
#   line 1: N tasks, T duration of a round (time constraint)
#   line 2: N values representing the length of the tasks t1, ... , tN
# output:
#   W *minimum* number of workers that is necessary to execute all tasks
#
# note: task time cannot be split between workers and task must be executed in the listed order

import os
import sys
import math
import heapq

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

def calculate(N, T, times, workers):
    task_heap = [(0, i) for i in range(workers)]  # Priority queue (heap) to efficiently find the worker with minimum workload
    print("attempting with workers:", workers)
    # step 1 - find minimum time in the time table
    i = 0
    while i < N:
        finish_time, worker_index = heapq.heappop(task_heap)

        # step 2 - assign the new task to the worker
        # print("assegno task numero", i, "al lavoratore", worker_index)
        if finish_time + times[i] > T:
            # workers += 1
            # task_heap = [(0, j) for j in range(workers)]  # Re-initialize the heap
            # i = 0
            # print("sto per ritornare false, somma=",finish_time + times[i])
            return False

        else:
            finish_time += times[i]
            heapq.heappush(task_heap, (finish_time, worker_index))
            i += 1

    return True


def bin_search(N, T, times):
    low = math.ceil(sum(times) / T)
    high = N

    # W is low
    res = calculate(N, T, times, low)
    if res == True:
        return low
    
    # Binary search W
    while low <= high:
        mid = (low + high) // 2
        res = calculate(N, T, times, mid)
        if res == True:
            # Is it optimal W?
            # is optimal if calculate(...) return False for W = min - 1, and True for W = mid
            is_optimal = not calculate(N, T, times, mid - 1)     
            if is_optimal == True:
                return mid 
            else: 
                high = mid - 1
        else:
            low = mid + 1

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python workers.py <input filename>")
        sys.exit(1)
    input_file = os.path.join(INPUT_PATH, sys.argv[1])
    N, T, tasks_time = read_input(input_file)

    W = bin_search(N, T, tasks_time)
    #W = calculate(N, T, tasks_time, 558379)

    output_file = os.path.join(OUTPUT_PATH, "output.txt")
    write_output(output_file, W)
