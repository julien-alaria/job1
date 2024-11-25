# first_number = int(input("Enter a number:"))
# second_number = int(input("Enter a second number"))
# print("The sum is", first_number + second_number)




# print("abcdefghijklmnopqrstuvwxyz")
# alphabet = ["a", "b","c","d"]
# print(alphabet)


# compteur = 0
# i = 0

# texte = input("Entrez votre texte:  ")

# while i < len(texte):
#     if "r" in texte:
#         compteur +=i
#         i +=1
# print(f'"il y a {compteur}"')

# job2
# def fruits():
#     l = ["pomme", "cerise", "orange"]
#     return l[1]
# print(fruits())

# job3
# def fruits():
#     l = ["pomme", "cerise", "orange"]
#     l.append("melon")
#     return l
# print(fruits())

# job4
# def fruits():
#     l = ["pomme", "cerise", "orange", "melon"]
#     l.insert(2, "mangue")
#     return l
# print(fruits())

# job5
# def liste(l):
#     l[3] = l[2]+l[4]
#     return l
# l = list(range(1,6))
# print(l)
# print(l[1])
# print(liste(l))
# print(l[-1])

# job6
# def liste_reverse(l):
#     l[0],l[4]=l[4],l[0]
#     return l
# l = list(range(1,6))
# print(l)
# print(liste_reverse(l))

# job7
# c = 0
# l = [8, 24, 48, 2, 16]
# for i in l:
#     if i % 3 == 0:
#         c = c + 1
# print(f"Il y a {c} multiples de 3 dans la liste")

# job8
# def sum_pair(l):
#     for i in l:
#         if i%2 ==0:
#             c=i+1
#     return c
# l = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]
# print(sum_pair(l))

# job9
# def max_min(l):
#     n=0
#     max = l[0]
#     min = l[0]
#     if n > max:
#         max = n
#     if n < min:
#         min = n
#     print("la valeur max est", max)
#     print("la valeur min est", min)


# l = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]


# print(max_min(l))


# print("la valeur mas est:", (max(l)))
# print("la valeur min est:", (min(l)))

# job10
# def sum_interval(l):
#     n = 1
#     for i in l:
#         if 90>= i >=25:
#             n = n*i
#     return n

# l = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
# print(sum_interval(l))

# job11
# l = [7, 11, 42, 39, 2]
# for i in range(len(l)):
#     l[i]+=1
# print(l)

# functions job1
# def my_print_hello():
#     return "Hello world"
# print(my_print_hello())

# functions job2
# def my_print_name(name):
#     return name
# name = "hello"
# print(my_print_name(name))

# functions job3
# def add(nb1, nb2):
#     print(nb1, nb2)
# add(4, 8)

# functions job4
# def GetHello():
#     return "Hello la Plateforme"
# print(GetHello())

# functions job5
# def calcule(num1,operator, num2):
#     if operator == "+":
#         return num1 + num2
#     if operator == "-":
#         return num1 - num2
#     if operator == "/":
#         return num1 / num2
#     if operator == "*":
#         return num1 * num2
#     else: 
#         return "Error"

# num1 = int(input("Entrez un nombre entier:  "))
# operator =str(input("Entrez votre type d'operation:  "))
# num2 = int(input("Entrez un nombre:  "))
# print(int(calcule(num1, operator, num2)))

# functions job6
# def neg_pose(nombre):
#     if nombre <= 0:
#         return "negatif"
#     else:
#         return "positif"
# print(neg_pose(7))
# print(neg_pose(-5))
# print(neg_pose(8))
# print(neg_pose(-2))
# print(neg_pose(0))

# functions job7
# def job7(langage):
#     if langage == "javascript":
#         return "tu es un developpeur web"
#     if langage == "python":
#         return "tu es un developpeur ia"
#     if langage == "reactjs":
#         return "tu es un developpeur mobile"
#     else:
#         return "un jour, je serai le meilleur developpeur..."

# langage = input("Entrez votre valeur:  ")
# print(job7(langage))

# functions job8
# def job8(type, saison):
#     if type == "fruits" and saison == "hiver":
#         return "orange, mandarine et kiwi"
#     if type == "fruits" and saison == "ete":
#         return "poire, fraise, cassis"
#     if type == "legumes" and saison == "hiver":
#         return "carotte, topinambour, endive"
#     if type == "legumes" and saison == "ete":
#         return "artichaut, aubergine, navet"
#     else:
#         return "Erreur"


# type = input("Entrez votre type, fruits ou legumes:  ")
# saison = input("Entrez votre saison, ete ou hiver:  ")
# print(job8(type, saison))

# functions job9 PAS FINI
# def moyenne(note1, note2, note3):
#     return int((note1 + note2 + note3) /3)


# note1 = int(input("Entrez votre premiere note:  "))
# note2 = int(input("Entrez votre seconde note:  "))
# note3 = int(input("Entrez votre troisieme note:  "))
# print(moyenne(note1, note2, note3))

# moyenne_etudiant = moyenne(note1, note2, note3)

# # print(int(moyenne_etudiant))

# if 20 <= 15:
#     print("Tres bon eleve")
# if 15<= 10:
#     print("Bon eleve")
# if 10<= 7:
#     print("Eleve moyen")
# if  7<= 0:
#     print("Eleve devant faire des efforts")

# functions job10

