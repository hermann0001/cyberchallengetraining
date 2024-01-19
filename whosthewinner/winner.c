/*
    input:
    l1. M, N, S, - M = players, N = tasks, S = submissions
    l2 - N+1. task-id (unique int 1:N),  correct flag (10 chars string), points (positive integer <=1000)
    lN+2 - N+S+1. player-id, task-id, flag submitted (10 chars string), timestamp  (positive integer up to 10^6)

    output: 
    M lines with two values, the i-th line contains player-id of the player in i-th position and score.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define INPUT_PATH "input/"
#define OUTPUT_PATH "myoutput/"
#define abort(msg) do{fprintf(stderr, msg); exit(1);}while(0);

typedef struct task{
    int tid;                // task id associated
    char f[11];             // flag string
    unsigned int score;     // score (always positive)
} TASK;

typedef struct submission{  
    int pid;                    // player id
    int tid;                    // task id associated
    char f[11];                 // flag string
    unsigned long timestamp;    // timestamp 
} SUB;



void readInput();
void writeOutput();

int M, N, S;
TASK* tasks;
SUB* submissions;
unsigned int* pscore;           //points achieved by each player

int main(int argc, char** argv)
{
    if(argc != 2)
        abort("usage: winner <input-filename>\n");


}

void readInput(char* filename)
{
    FILE* file;

    if ((file = fopen(filename, "rt")) == NULL) 
        abort("Error opening file\n");

    // read line 1
    if(fscanf(file, "%d %d %d", &M, &N, &S) != 3) {
        fclose(file);
        abort("Error reading line 1\n");
    }

    // allocate memory for each data structure
    tasks = (TASK*)malloc(N * sizeof(TASK));        //delete me when you write free(tasks)
    submissions = (SUB*)malloc(S * sizeof(SUB));    //delete me when you write free(submissions)
    pscore = (unsigned long*)calloc(M, sizeof(unsigned long));  //delete me when you write free(pscore)


    // read from line 2 to line N+1
    for(int i = 0; i < N; i++){
        if(fscanf(file, "%d %s %u", tasks->tid, tasks->f, tasks->score) != 3){
            fclose(file);
            abort("Error reading task info lines\n");
        }
    }


    // read from line N+2 to N+S+1
    for(int i = 0; i < S; i++){
        if(fscanf(file, "%d %d %s %lu", 
        submissions->pid, submissions->tid, submissions->f, submissions->timestamp) != 4){
            fclose(file);
            abort("Error reading subs info lines\n");
        }
    }

    fclose(file);
}

void check(){

    for(int i = 0; i < S; i++){
        
    }


}