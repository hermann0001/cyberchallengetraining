/*
    Input are N+2 lines:
    l1. Q - number of questions, N - candidates
    l2. list of correct answers as a string of Q uppercase letters in the set {A, B, C, D}
    l3, ..., lN+2. string of Q characters in {A, B, C, D, ?} (? is missing answer)
*/

#include <iostream>
#include <fstream>
#include <filesystem>
#include <vector>
#include <string>
#include <chrono>

#define OUTPUT_PATH "myoutput/"
#define OUTPUT_FILE OUTPUT_PATH "output.txt"
using namespace std;

int Q, N;
string correctAnswers;
vector<string> givenAnswers;
vector<int> scores;

void readInput(const string& filename);
void writeOutput();
void solve();

int main(int argc, char** argv) {
    using clock = chrono::high_resolution_clock;
    
    ios::sync_with_stdio(0);
    cin.tie(nullptr);

    if(argc != 2) {
        cerr << "usage: prestest <input filename>\n";
        return 1;
    }
    
    readInput(argv[1]);

    auto start = clock::now();
    solve();
    auto end = clock::now();

    writeOutput();
    
    chrono::duration<double> diff = end - start;
    cout << "----------------------------------------------\n";
    cout << N << " Candidates and " << Q << " Questions\n";
    cout << "Execution time: " << diff.count() << " seconds\n";
    
    return 0;
}

void readInput(const string& filename){
    ifstream file(filename);
    if (!file) {
        cerr << "Error opening file\n";
        exit(1);
    } 

    // read number of questions and partecipants
    file >> Q >> N;
    correctAnswers.resize(Q);
    file >> correctAnswers;

    givenAnswers.resize(N);
    for (int i = 0; i < N; i++) {
        givenAnswers[i].resize(Q);
        file >> givenAnswers[i];
    }
}

void writeOutput() {
    // Ensure myoutput directory exists
    filesystem::create_directories(OUTPUT_PATH);
    
    ofstream file(OUTPUT_FILE);
    if(!file) {
        cerr << "Error opening output file\n";
        exit(1);
    }

    for(int s : scores)
        file << s << "\n";
}

void solve() {
    scores.resize(N);
    
    const char* correct = correctAnswers.data();
    for(int i = 0; i < N; i++){
        const char* answer = givenAnswers[i].data();
        int count = 0;   
        for(int j = 0; j < Q; j++)
            count += (answer[j] == correct[j]);
        scores[i] = count;
    }
}


