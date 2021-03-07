#
# Created on Sun Mar 07 2021
#
# Copyright (c) 2021 Peterson Yuhala, IIUN
#

s = input("Enter a DNA string: ")


def valid_dna(dnaS):
    for i in dnaS:
        if(i not in 'ACGT'):
            return False
    return True


print("Valid DNA string: ", valid_dna(s))
