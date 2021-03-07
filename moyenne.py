#
# Created on Sun Mar 07 2021
#
# Copyright (c) 2021 Peterson Yuhala, IIUN
#

# manual version
def moyenne(l):
    summ = 0
    for i in range(len(l)):
        summ += l[i]
    moy = summ/len(l)
    return moy


# using built in functions
def moyenne2(l):
    summ = sum(l)
    return summ/len(l)

print("Moyenne([1,2,3]): ", moyenne([1, 2, 3]))
print("Moyenne([11,2,33.5,4,5]): ", moyenne([11, 2, 33.5, 4, 5]))
print("Moyenne([10,20,30,40]): ", moyenne([10, 20, 30, 40]))
