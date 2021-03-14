

# sommer avec la fonction sum

num = input("Entrer un nombre : ")

# creer une liste vide
l = []

# ajouter chaque membre du chaine en entree dans votre liste
for i in num:
    l.append(int(i))

# imprimer la somme avec sum
print("Sommation avec sum: ",sum(l))


# sommer sans la fonction sum

num = input("Entrer un nombre: ")

total = 0
for i in num:
    total += int(i)

print("Sommation sans sum: ",total)