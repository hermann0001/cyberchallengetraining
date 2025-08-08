/*
    input:
    l1. M, N, S, - M = players, N = tasks, S = submissions
    l2 - N+1. task-id (unique int 1:N),  correct flag (10 chars string), points (positive integer <=1000)
    lN+2 - N+S+1. player-id, task-id, flag submitted (10 chars string), timestamp  (positive integer up to 10^6)

    output: 
    M lines with two values, the i-th line contains player-id of the player in i-th position and score.
*/

#include <iostream>
#include <sys/resource.h>
#include <fstream>
#include <filesystem>
#include <vector>
#include <string>
#include <queue>
#include <chrono>
#include <cmath>
#include <algorithm>
#include <numeric> 

#define OUTPUT_PATH "myoutput/"
#define OUTPUT_FILE OUTPUT_PATH "output.txt"
using namespace std;

int N, T, W;
vector<unsigned int> times; // times[servizio] = 30ms

void readInput(const string& filename);
void writeOutput(int W);
int solve();
bool estimate_workers(int workers);

void print_memory_usage() {
    struct rusage usage;
    getrusage(RUSAGE_SELF, &usage);
    
    // On Linux: ru_maxrss is in kilobytes
    std::cout << "Peak memory usage: " << (usage.ru_maxrss / 1024.0) << " MB" << std::endl;
}

int main(int argc, char** argv){
    using clock = chrono::high_resolution_clock;
    
    ios::sync_with_stdio(0);
    cin.tie(nullptr);
    
    if(argc != 2) {
        cerr << "usage: workers <input filename>\n";
        return 1;
    }
    
    readInput(argv[1]);
    
    auto start = clock::now();
    W = solve();
    auto end = clock::now();
    
    writeOutput(W);

    chrono::duration<double> diff = end - start;
    cout << "----------------------------------------------\n";
    cout << "Execution time: " << diff.count() << " seconds\n";
    print_memory_usage();
    
    return 0;
}

void readInput(const string& filename) {
    ifstream file(filename);
    if (!file) {
        cerr << "Error opening file\n";
        exit(1);
    } 
    
    // read number of services and duration of a round (ms)
    file >> N >> T;
    times.resize(N);

    // read check routine times
    for (int i = 0; i < N; i++) 
        file >> times[i];
}

void writeOutput(int W) {
    // Ensure myoutput directory exists
    filesystem::create_directories(OUTPUT_PATH);
    ofstream file(OUTPUT_FILE);
    if(!file) {
        cerr << "Error opening output file\n";
        exit(1);
    }

    file << W << "\n";
}

bool estimate_workers(int workers) {
    // Min-heap of pairs: (finish_time, worker_id)
    using Task = pair<int, int>;
    priority_queue<Task, vector<Task>, greater<>> task_heap;

    for (int i = 0; i < workers; i++) 
        task_heap.emplace(0, i);
    
    for (int i = 0; i < N; i++) {
        auto [finish_time, worker_id] = task_heap.top();
        task_heap.pop();

        if (finish_time + times[i] > T)
            return false;
        
        task_heap.emplace(finish_time + times[i], worker_id);
    }
    return true;
}

// bin search
int solve() {
    // lower bound: ceil(total_time / T)
    int low = static_cast<int>(ceil(static_cast<double>(accumulate(times.begin(), times.end(), 0LL)) / T));
    int high = N;

    if (estimate_workers(low))
        return low;
    
    while (low <= high) {
        int mid = (low + high) / 2;
        if (estimate_workers(mid)) {
            if (!estimate_workers(mid - 1))
                return mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    return -1; 
}

