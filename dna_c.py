#
# Created on Sun Mar 07 2021
#
# Copyright (c) 2021 Peterson Yuhala, IIUN
#

s = input("Enter a DNA string: ")


def dna_c(dnaS):
    c_count = 0
    for i in dnaS:
        if(i == 'C'):
            c_count += 1

    return c_count


print("Number of Cs: ", dna_c(s))
