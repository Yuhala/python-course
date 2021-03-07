#
# Created on Mon Mar 01 2021
#
# Copyright (c) 2021 Peterson Yuhala, IIUN
#

num = int(input("Enter a number: "))


rem3 = num % 3
rem5 = num % 5
rem7 = num % 7
rem11 = num % 11

if (rem3 == 0):
    print(num//3)
elif (rem5 == 0):
    print(num//5)
elif (rem7 == 0):
    print(num//7)
elif (rem11 == 0):
    print(num//11)
else:
    print(0)
