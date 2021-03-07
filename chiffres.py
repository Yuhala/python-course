#
# Created on Sun Mar 07 2021
#
# Copyright (c) 2021 Peterson Yuhala, IIUN
#

num = input("Enter a number: ")

n = len(num)
sum = 0
for i in range(n):
    sum += int(num[i])

print("Sum is: ", sum)
