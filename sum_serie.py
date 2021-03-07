#
# Created on Sun Mar 07 2021
#
# Copyright (c) 2021 Peterson Yuhala, IIUN
#

# I avoid using known function names as variable names: eg summ instead of sum

maxx = int(input("Enter max num: "))

summ = 0

for i in range(maxx+1):
    summ += i

print("Sum of series: ", summ)
