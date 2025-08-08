#!/bin/env python3

import sys

# Se vuoi leggere/scrivere da file decommenta qua
fin = open("input3.txt", "r")  # File di input fornito dalla piattaforma
fout = open("output.txt", "wt+")  # File di output fornito dalla piattaforma

# Se vuoi leggere/scrivere da linea di comando decommenta qua
#fin = sys.stdin  # File di input fornito dalla piattaforma
#fout = sys.stdout  # File di output fornito dalla piattaforma


def compute_lps(s):
    length = len(s)
    lps = [0] * length
    i, j = 0, 1

    while j < length:
        if s[i] == s[j]:
            i += 1
            lps[j] = i
            j += 1
        else:
            if i != 0:
                i = lps[i - 1]
            else:
                lps[j] = 0
                j += 1

    return lps[-1]

def count_patterns(N, M, alphabet, S):
    lps = compute_lps(S)
    cover_length = M - lps
    return M // cover_length if cover_length > 0 else 1

T = int(fin.readline().strip())

for _ in range(T):
    N, M = map(int, fin.readline().strip().split())
    alph = fin.readline().strip()
    s = fin.readline().strip()
    fout.write(f"{count_patterns(N, M, alph, s)}\n")