#
# Created on Sun Mar 07 2021
#
# Copyright (c) 2021 Peterson Yuhala, IIUN
#

s = input("Enter a string: ")

invS = ""

# NB: the range function always stops 1 short of the end value
for i in range(len(s)-1, -1, -1):
    invS += s[i]

print("Inverse of string is: ", invS)
