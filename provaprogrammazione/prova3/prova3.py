#!/bin/env python3

import sys

# Se vuoi leggere/scrivere da file decommenta qua
fin = open("input1-test.txt", "r")  # File di input fornito dalla piattaforma
fout = open("output.txt", "wt+")  # File di output fornito dalla piattaforma


def find_subsets(N, D, S):
    S.sort()
    lista_di_insiemi_possibili = []
    i = 0

    while i < N:
        j = i + 1
        current_set = set()
        current_set.add(S[i]) 
        while j < N and abs(S[i] - S[j]) <= D:
            current_set.add(S[j]) 
            j += 1
        lista_di_insiemi_possibili.append(current_set)
        i += 1

    max_set_A = max(lista_di_insiemi_possibili, key=len)
    max_sum = len(max_set_A)  

    for subset in lista_di_insiemi_possibili:
        if max_set_A.isdisjoint(subset):
            elem_sum = len(max_set_A) + len(subset)
            max_sum = max(max_sum, elem_sum)

    return max_sum

T = int(fin.readline().strip())

for _ in range(T):
    N, D = map(int, fin.readline().strip().split())
    S = list(map(int, fin.readline().strip().split()))
    assert len(S) == N
    fout.write(f"{find_subsets(N, D, S)}\n")

