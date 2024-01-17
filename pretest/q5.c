#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    struct {
        char s1[3];
        char s2[5];
    } s;

    strcpy(s.s1, "ok");
    strcpy(s.s2, "flag");

    printf("%s\n", &((char*)&s)[3]);
}