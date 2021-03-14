#
# Created on Sun Mar 07 2021
#
# Copyright (c) 2021 Peterson Yuhala, IIUN
#


# we assume the input is a valid dna string with only A, C, G or Ts.
def dna_stats(dnaS):
    dic = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    s = dnaS.upper()
    for c in s:
        dic[c] += 1
    return dic

def dna_stats2(dnaS):
    dic = {}
    s = dnaS.upper()
    for c in s:
        if c in dic:
            dic[c] += 1
        else:
            dic[c] = 1
    return dic

print("dna_stats('ACGTACGAATC'): ", dna_stats('ACGTACGAATC'))
print("dna_stats2('ACGTACGAATC'): ", dna_stats2('ACGTACGAATC'))
print("dna_stats('attac'): ", dna_stats('attac'))
