/*
    Input are N+2 lines:
    l1. Q - number of questions, N - candidates
    l2. list of correct answers as a string of Q uppercase letters in the set {A, B, C, D}
    l3, ..., lN+2. string of Q characters in {A, B, C, D, ?} (? is missing answer)
*/

#include <iostream>
#include <fstream>
#include <cstring>
#include <array>

#define abort(msg) do{std::cerr<<msg; exit(1);}while(0);
#define iFILENAME "dataset/input/input-1-0.txt"
#define oFILENAME "dataset/output/output-1-0.txt"

int Q, N;

void readInput();
void writeOutput();
void check();
void validate();

void readInput(){
    std::ifstream inputFile(iFILENAME);

    if (!inputFile.is_open()) abort("Error opening file\n"); 

    // read number of questions and partecipants
    inputFile >> Q >> N;

    // read list of correct answers
    char correctAnswers[Q];
    for(int i = 0; i < Q; i++)
        inputFile >> correctAnswers[i]; //sicuro qui crasha
    
    // validate the list with set {A,B,C,D}
    validate();


    char candidatesAnswers[N][Q];
    // read list of answers for each candidate
    for(int i = 0; i < N; i++){
        for(int j = 0; j < Q; j++)
            inputFile >> candidatesAnswers[N][Q];

    }

    // validate each list of answers with set {A,B,C,D,?}
    validate();

    inputFile.close();
}

