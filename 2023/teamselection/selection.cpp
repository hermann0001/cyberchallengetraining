/*
INPUT: 
  Line 1. T test cases
  Line 2. N candidates, M players in a team, S set of skills
  Line 3. list of M space-separated 3 characters representing skills name
  Line 4 to 2+N(S+1) group of S+1 lines
      Line 1. Unique id of candidate
      Line 2 to S+1: skill name and skill score space-separated
OUTPUT:
  T positive integers, one for each line, representing maximum global score
*/

#include <iostream>
#include <sys/resource.h>
#include <fstream>
#include <filesystem>
#include <vector>
#include <string>
#include <chrono>
#include <unordered_map>

#define OUTPUT_PATH "myoutput/"
#define OUTPUT_FILE OUTPUT_PATH "output.txt"
using namespace std;

struct Candidate {
    int pid;
    unordered_map<string, unsigned int> skills;
};

struct TestCase {
    int N, M, S;
    vector<string> required_skills;
    vector<Candidate> candidates;
};

int T;
vector<TestCase> test_cases;
vector<unsigned int> global_scores;

void readInput(const string& filename);
void writeOutput();
void solve();

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
    solve();
    auto end = clock::now();
    
    writeOutput();

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

    // read test cases, candidates, team size, number of skills
    file >> T;
    test_cases.resize(T);
    for (int t = 0; t < T; t++) {
        auto& test = test_cases[t];
        file >> test.N >> test.M >> test.S;
        
        test.required_skills.resize(test.M);
        // read skills required
        for (int i = 0; i < test.M; i++) 
        file >> test.required_skills[i];
        
        test.candidates.resize(test.N);
        for (int i = 0; i < test.N; i++) {
            int pid;
            file >> pid;
            pid--;

            test.candidates[i].pid = pid;
            test.candidates[i].skills.clear();

            for (int j = 0; j < test.S; j++) {
                string skill_name;
                int skill_score;
                file >> skill_name >> skill_score;
                test.candidates[i].skills[skill_name] = skill_score;
            }
        }
    }
    global_scores.assign(T, 0);
}

void writeOutput() {
    // Ensure myoutput directory exists
    filesystem::create_directories(OUTPUT_PATH);
    ofstream file(OUTPUT_FILE);
    if(!file) {
        cerr << "Error opening output file\n";
        exit(1);
    }

    for (int t = 0; t < T; t++) 
        file << global_scores[t] << "\n";
}

void solve() {
}

