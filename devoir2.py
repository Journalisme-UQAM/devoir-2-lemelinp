#coding: utf-8

import csv
file = "concordia1.csv"
f = open(file)
lines = csv.reader(f)

for line in lines:
    longtitre = len(line[2])
    print(line[2])
    print(longtitre)

f1= open(file)
lines = csv.reader(f1)
next(lines)

m = 0
d = 0
# j'ai ajouté ces variables comme compteur, ca donne 4989 maitrises et 927 doctorats, 
# mais je ne sais pas si ça colle avec le nombre total d'entrées

for line in lines:
    if "M.A." in line[6]:
        m += 1
        print("Maitrise")
    if "Ph.D." in line[6]:
        d += 1
        print("Doctorat")
print(m)
print(d)

# Pour la partie 3, j'aurais peut-être été capable d'extraire le nombre de pages de chaque ligne si le nombre était toujours indiqué en premier. 
# Comme ça change et qu'il y a des chiffres romains, je n'y suis pas arrivé.
