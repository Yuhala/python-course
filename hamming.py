#
# Created on Sun Mar 07 2021
#
# Copyright (c) 2021 Peterson Yuhala, IIUN
#


def hamming(s1, s2):
    if(len(s1) != len(s2)):
        print("Both strings have different lengths!")
        return
    dist = 0
    for i in range(len(s1)):
        if(s1[i] != s2[i]):
            dist += 1

    return dist


print("hamming('ACGTACT', 'ACGATCT'): " + str(hamming('ACGTACT', 'ACGATCT')))
print("hamming('GACT', 'GACT'): " + str(hamming('GACT', 'GACT')))
