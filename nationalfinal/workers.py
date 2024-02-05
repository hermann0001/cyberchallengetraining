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
    #time_tables = {}                # dictionary to assign for each worker the finish time
    task_heap = [(0, i) for i in range(workers)]  # Priority queue (heap) to efficiently find the worker with minimum workload

    #print("initial guess:", workers)


    # step 1 - find minimum time in the time table
    i = 0
    while i < N: 
        finish_time, worker_index = heapq.heappop(task_heap)

        # step 2 - assign the new task to the worker
        #print("assegno task numero", i, "al lavoratore", worker_index)
        if finish_time + times[i] >= T:
            # heapq.heappush(task_heap, (times[i], workers))
            #return calculate(N, T, times, workers+1)
            workers += 1
            task_heap = [(0, j) for j in range(workers)]  # Re-initialize the heap
            i = 0
            print("workers:", workers)

        else:
            finish_time += times[i]
            #print("pushing", (finish_time, worker_index))
            heapq.heappush(task_heap, (finish_time, worker_index))
            i += 1

    return workers
        
# def can_complete_tasks(workers, N, T, times):
    
#     #Checks if a given number of workers can complete all tasks within the time limit T.
#     print(workers)
#     # Initialize a priority queue with workers' next available time starting at 0
#     task_heap = [(0, i) for i in range(workers)]
#     for time in times:
#         finish_time, worker_index = heapq.heappop(task_heap)
#         if finish_time + time > T:
#             # If adding the current task exceeds T, return False
#             return False
#         heapq.heappush(task_heap, (finish_time + time, worker_index))
#     # If all tasks can be assigned without exceeding T, return True
#     return True   

# def calculate(N, T, times):

#     #Uses binary search to find the minimum number of workers needed to complete all tasks within T.
    
#     # Sort times to potentially optimize the distribution of tasks
#     times.sort(reverse=True)
#     left, right = 1, N  # At least one worker is needed, and at most one worker per task
    
#     while left < right:
#         mid = (left + right) // 2
#         if can_complete_tasks(mid, N, T, times):
#             right = mid
#         else:
#             left = mid + 1
    
#     return left      

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python workers.py <input filename>")
        sys.exit(1)
    input_file = os.path.join(INPUT_PATH, sys.argv[1])
    N, T, tasks_time = read_input(input_file)
    W = calculate(N, T, tasks_time, 101088)#math.ceil(sum(tasks_time) / T))

    output_file = os.path.join(OUTPUT_PATH, "output.txt")
    write_output(output_file, W)
