/*
    input:
    l1. M, N, S, - M = players, N = tasks, S = submissions
    l2 - N+1. task-id (unique int 1:N),  correct flag (10 chars string), points (positive integer <=1000)
    lN+2 - N+S+1. player-id, task-id, flag submitted (10 chars string), timestamp  (positive integer up to 10^6)

    output: 
    M lines with two values, the i-th line contains player-id of the player in i-th position and score.
*/

#include <iostream>
#include <fstream>
#include <filesystem>
#include <vector>
#include <string>
#include <chrono>
#include <algorithm>

#define OUTPUT_PATH "myoutput/"
#define OUTPUT_FILE OUTPUT_PATH "output.txt"
using namespace std;

struct Task{
    string flag;                // flag string
    unsigned int score;         // score (always positive)
};

struct Submission{  
    int pid;                    // player id
    int tid;                    // task id associated
    string flag;                // flag string
    unsigned long timestamp;    // timestamp 
};

int M, N, S;
vector<Task> tasks;
vector<Submission> submissions;         
vector<unsigned int> scores;            // scores[pid]
vector<vector<bool>> completed;         // map player -> tasks --- completed completed[pid][tid]
vector<unsigned int> last_time;         // map player -> timestamp of last correctly scored submission --- last_time[pid]

void readInput(const string& filename);
void writeOutput();
void solve();
bool tiebreak(const pair<int, unsigned int>& a, const pair<int, unsigned int>& b);

int main(int argc, char** argv){
    using clock = chrono::high_resolution_clock;
    
    ios::sync_with_stdio(0);
    cin.tie(nullptr);
    
    if(argc != 2) {
        cerr << "usage: winner <input filename>\n";
        return 1;
    }
    
    readInput(argv[1]);
    
    auto start = clock::now();
    solve();
    auto end = clock::now();
    
    writeOutput();

    chrono::duration<double> diff = end - start;
    cout << "----------------------------------------------\n";
    cout << "Execution time: " << diff.count() << " seconds\n";
    
    return 0;
}

void readInput(const string& filename)
{
    ifstream file(filename);

    if (!file) {
        cerr << "Error opening file\n";
        exit(1);
    } 
    
    // read players, tasks, submissions
    file >> M >> N >> S;

    scores.assign(M, 0);
    completed.assign(M, vector<bool>(N + 1, false));
    last_time.assign(M, 0);
    
    // read task info
    tasks.assign(N + 1, Task{});
    for(int i = 1; i <= N; i++){
        int tid, pts;
        string flag;

        file >> tid >> flag >> pts;
        tasks[tid] = { flag, static_cast<unsigned int>(pts) };
    }

    // read submission info
    submissions.resize(S);
    for(auto& sub : submissions) {
        file >> sub.pid >> sub.tid >> sub.flag >> sub.timestamp;
        sub.pid--;
    }

}

void writeOutput() {
    // Ensure myoutput directory exists
    filesystem::create_directories(OUTPUT_PATH);

    vector<pair<int, unsigned int>> result;
    for (int pid = 0; pid < M; pid++) 
        result.emplace_back(pid, scores[pid]);
    
    sort(result.begin(), result.end(), tiebreak);

    ofstream file(OUTPUT_FILE);
    if(!file) {
        cerr << "Error opening output file\n";
        exit(1);
    }

    for (const auto& [pid, score] : result) 
        file << (pid + 1) << " " << score << "\n";
}

bool tiebreak(const pair<int, unsigned int>& a, const pair<int, unsigned int>& b) {
    // descending score
    if (a.second != b.second)
        return a.second > b.second;

    // ascending last timestamp
    if (last_time[a.first] != last_time[b.first]) 
        return last_time[a.first] < last_time[b.first];

    // ascending player ID
    return a.first < b.first;
}


void solve() {
    // sort submissions by ascending timestamp
    sort(submissions.begin(), submissions.end(), [](const Submission& a, const Submission& b) {
        return a.timestamp < b.timestamp;
    });
    
    // iterate through each submission
    for (const auto& sub: submissions) {
        const auto& task = tasks[sub.tid];
        
        // First submission by this player? initialize their set
        if (!completed[sub.pid][sub.tid] && sub.flag  == task.flag) {
            scores[sub.pid] += task.score;
            completed[sub.pid][sub.tid] = true;
            last_time[sub.pid] = sub.timestamp;
        }
    }
}