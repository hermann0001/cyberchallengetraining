/*
    Input are N+2 lines:
    l1. Q - number of questions, N - candidates
    l2. list of correct answers as a string of Q uppercase letters in the set {A, B, C, D}
    l3, ..., lN+2. string of Q characters in {A, B, C, D, ?} (? is missing answer)
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>


#define abort(msg) do{fprintf(stderr, msg); exit(1);}while(0);
#define INPUT_PATH "dataset/input/"
#define OUTPUT_PATH "dataset/myoutput/"

const char correctSet[] = {'A', 'B', 'C', 'D'};
const char givenSet[] = {'A', 'B', 'C', 'D', '?'};
char* correctAnswers;
char** givenAnswers;
int* score;

int Q, N;


void readInput(char* filename);
void writeOutput();
void check();
void printData();

int main(int argc, char** argv)
{
    if(argc != 2)
        abort("usage: prestest2023 <input filename>\n"); 
    
    char* input = malloc(250);
    strcpy(input, INPUT_PATH);
    strcat(input, argv[1]);
    readInput(input);
    free(input);

    check();

    char* output = malloc(250);
    strcpy(output, OUTPUT_PATH);
    strcat(output, "output.txt");
    writeOutput(output);
    free(output);
}

void readInput(char* filename){
    FILE* file;

    if ((file = fopen(filename, "rt")) == NULL) 
        abort("Error opening file\n"); 

    // read number of questions and partecipants
    if(fscanf(file, "%d %d", &Q, &N) != 2) {
        fclose(file);
        abort("Error reading Q and N\n");
    }

    // read list of correct answers
    correctAnswers = malloc(Q * sizeof(char) + 1);      // + 1 cause of this friend -> '\0' (i spent 2 hours understanding why i had memory issues ._.)
    if(fscanf(file, "%s", correctAnswers) != 1){
        fclose(file);
        abort("Error reading correct answers\n");
    }

    givenAnswers = malloc(N * sizeof(char*));
    for(int i = 0; i < N; i++){
        givenAnswers[i] = malloc(Q * sizeof(char) + 1);
        if(fscanf(file, "%s", givenAnswers[i]) != 1){
            fclose(file);
            abort("Error reading answers given");
        }
    }
    fclose(file);
}

void writeOutput(char* filename)
{
    FILE* file;
    if ((file = fopen(filename, "wt+")) == NULL) 
        abort("Error opening file\n"); 

    for(int i = 0; i < N; i++)
        fprintf(file, "%d\n", score[i]);
}

void printData()
{
    printf("%d %d\n", Q, N);
    printf("%s\n", correctAnswers);
    for(int i = 0; i < N; i++)
        printf("%s\n", givenAnswers[i]);
}


void check()
{
    //allocate score array
    score = calloc(N, sizeof(int));

    for(int i = 0; i < N; i++){   
        for(int j = 0; j < Q; j++){
            if(givenAnswers[i][j] == correctAnswers[j])
                score[i]++; 
        }
        free(givenAnswers[i]);
    }
    free(givenAnswers);
    free(correctAnswers);
}


