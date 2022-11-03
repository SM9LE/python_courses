import math
import random
from collections import Counter

# Exercice 1 :

print("Exercice 1 : Déclarer et renseigner des variables :")
# Déclaration des variables demandées
prenom = "Pierre"
age = 20
majeur = True
compte_en_banque = 20135.384
# Différence entre un tuple et un tableau est les [] pour array et () pour tuple
amis = ['Marie', 'Julien', 'Adrien']
parents = ('Marc', 'Caroline')

# Vérification du type Prénom et print de la variable prénom
print("Le type de la variable prenom est : " + str(type(prenom)))
print(prenom)
print("--------")

# Vérification du type age et print de la variable age
print("Le type de la variable age est : " + str(type(age)))
print(age)
print("--------")

# Vérification du type majeur et print de la variable majeur
print("Le type de la variable majeur est : " + str(type(majeur)))
print(majeur)
print("--------")

# Vérification du type compte_en_banque et print de la variable compte_en_banque
print("Le type de la variable compte_en_banque est : " + str(type(compte_en_banque)))
print(compte_en_banque)
print("--------")
# Vérification du type amis et print de la variable amis
print("Le type de la variable amis est : " + str(type(amis)))
print(amis)
print("--------")

# Vérification du type parents et print de la variable parents
print("Le type de la variable parents est : " + str(type(parents)))
print(parents)
print("--------")

# Exercice 2

print("Exercice 2 : Supprimer l'erreur présente dans la variable site_web :")
site_web = "voila"
print(site_web)
print("--------")

# Exercice 3

print("Exercice 3 : Afficher une variable int avec du texte dans le print :")

nombre = 15
# J'utilise la fonction "str()" car j'écris du texte dans mon print, de plus la variable "nombre" est un int, je la transforme donc.
print("Le nombre est " + str(nombre))
print("--------")

# Exercice 4

print("Exercice 4 : Effectuer un calcul et afficher le calcul ainsi que le résultat : ")

print("Méthode 1 : ")
x = 2 + 6 + 3
print("2 + 6 + 3 = " + str(x))
print("--------")

print("Méthode 2 : ")
a = 2
b = 6
c = 3
print (str(a) + " + " + str(b) + " + "+ str(c) + " = "+ str(2+6+3))
print("--------")

print("Méthode 3 : ")
# La fonction "sep" permet de séparer les variables a b et c par des + précédés et suivis d'espaces
print(a,b,c, sep=" + " )
print("--------")

# Exercice 5

print("Exercice 5 : Quelle est l'erreur au sein de la variable list ? :")
# L'erreur ici est que list est réservé selon la doc de Python. On utilise donc le list1 ou liste
list1 = range(3)
list2 = range(5)
print(list(list2))
print("---------")

# Exercice 6

print("Exercice 6 : Vérifier qu'une variable est bien de type chaîne de caractères : ")
print("Méthode 1 : ")

print("prenom est une chaîne de caractères avec comme valeur 'Pierre'")
prenom = "Pierre"

# Etape vérification avec prenom => chaîne de caractère
print(type(prenom))

# Si prenom est égale à Pierre alors on affiche, sinon on renvoie false
if (type(prenom) == str()):
    {
        print("La variable est bien une chaîne de caractères")
    }
else:
    {
        print(False)
    }
print("--------")

print("Méthode 2 : ")
if isinstance(prenom, str):
    print("Variable prenom est une chaîne de caractères")

print("--------")

print("Changement de type de variable, prenom devient un int avec pour valeur 0")
print("Méthode 1 : ")
# Changement de valeur pour prenom, donc changement de type
prenom = 0

# Si prenom n'est pas une chaîne de caractère, on retourne false, sinon on affiche le prénom
if (type(prenom) != str()):
    {
        print(False)
    }
else:
    {
        print(prenom)
    }
print("--------")

print("Méthode 2 : ")
# isinstance permet de comparer deux variables. Ici je compare le fait que la variable prenom est une chaine de caractere.
if isinstance(prenom, str):
    print("Variable prenom est une chaine de caracteres")
else:
    print("Variable prenom n'est pas une chaine de caractères")

print("--------")

# Exercice 6 Bonus

print("Exercice 6 Bonus : Une autre façon de connaître le type d'une variable : ")

print("Essai de fonction pour connaitre le type : ")
def methodeVerif(value, type):
        if isinstance(value ,type):
            print("La valeur" + str(value) + " est une : " + str(type))
        else:
            print("La valeur " + str(value) + " n'est pas une : " + str(type))

methodeVerif("Quentin", int)

print("--------")

# Exercice 7

print("Exercice 7 : Remplacer dans la variable phrase le mot 'Bonjour' par le mot 'salut' : ")
phrase = "Bonjour les amis"
# Le replace permet de remplacer "bonjour" par "Salut"
nouvelle_phrase = phrase.replace("Bonjour", "salut")
print(nouvelle_phrase)

print("--------")

# Exercice 7 Bonus

print("Exercice 7 Bonus : Dynamiser le remplacement d'occurrences au sein d'une variable : ")
print("Essai de fonction pour remplacer : ")

def methodeReplace(nomVariable, valeurOrigine, valeurRemplacer, nbFois):
    # # Me sert de console.log pour être sûr que je récupère les bonnes valeurs
    # print(len(nomVariable))
    # print(len(valeurOrigine))
    # print(len(valeurRemplacer))
    # print(nbFois)
    if (len(nomVariable) != 0) and (len(valeurOrigine) != 0) and (len(valeurRemplacer) != 0):
        {
            print(nomVariable.replace(valeurOrigine, valeurRemplacer, nbFois))
        }
    # Je vérifie la longueur des variables que j'accorde.
    elif (len(nomVariable) == 0):
        {
            print("Vous devez renseigner un nom de variable correct")
        }
    elif (len(valeurOrigine) == 0):
        {
            print("La valeur d'origine doit contenir au moins un caractère")
        }
    elif(len(valeurRemplacer) == 0):
        {
            print("La valeur à remplacer doit contenir au moins un caractère")
        }
    elif(type(nbFois) != type(int)):
        {
            print("tu cringe ?")
        }
    else:
        print("Not Working")

x = "salut,salut,salut,salut, bonjour"
methodeReplace(x, "salut", "aaaaaa", 3)

print("--------")

# Exercice 8

print("Exercice 8 : Manipulation de la valeur du booléen : ")
x = 20
print(x > 5 and x < 15)

print("--------")

# Exercice 9

print("Exercice 9 : Manipulation de liste :")
liste12 = ["pomme", "poire", "cerise"]

def afficheListe(demande, liste):
    # Retourne true si le str est dans la liste
    print(demande in liste)
    # Renvoie le string de l'index, le numéro de l'index et le nombre d'éléments total dans la liste
    print(demande + " se trouve à l'index numéro " + str(liste.count(demande)) + " il y a au total " + str(len(liste)) +
          " index dans la liste")

afficheListe("pomme", liste12)

print("--------")

# Exercice 10

print("Exercice 10 : Retirer, remettre dans l'ordre et renvoyer une chaîne de caractère en liste : ")
chaine = "pomme, abricot, cerise, fraise, orange"
# Permet d'effacer les virgules et espaces pour en faire une phrase
chaine_liste = chaine.split(", ")
# Remet la liste dans l'ordre
chaine_liste.sort()
# Remet la chaine sous forme de liste
chaine_en_ordre = ", ".join((chaine_liste))
print(chaine_en_ordre)

print("--------")

# Exercice 11

print("Exercice 11 : Permettre à l'utilisateur de calculer le volume d'une sphère : ")
def volSphere (rayon):
    volume = ((4 * math.pi / 3) * rayon ** 3)
    print(str(volume))

volSphere(2)

print("--------")

# Exercice 11 Bonus

print("Exercice 11 Bonus : Permettre à l'utilisateur de  décider entre deux options de calculer le volume d'une sphère ou le volume d'un parallélépipède : ")

"""""
La question posée : Comment permettre à l'utilisateur de choisir entre deux options : Calculer volume sphere ou para
Ce que je veux faire : 
1) Attendre une variable string pour activer la première fonction. Cette fonction déterminera 
quelle formule doit être activée.
2) Si la formule Sphère est attendue, demander à l'user d'insert la valeurs, renvoyer le volume en sortie
3) Si la formule para est attendue, demander à l'user d'insert les valeurs, renvoyer le volume en sortie
"""""

def calcul(nom, longueur, largeur, hauteur, rayon):
    if (nom == "para"):
            volParal(longueur, largeur, hauteur)
    elif (nom == "sphere"):
            volSphere(rayon)

def volSphere (rayon):
    volume = ((4.0 * math.pi / 3) * rayon ** 3)
    print(str(volume))

def volParal (longueur, largeur, hauteur):
    volume = longueur * largeur * hauteur
    print(str(volume))

calcul("para", 4, 10, 12, 0)
# calcul("sphere", 0, 0, 0, 12)

print("--------")

# Exercice 12

print("Exercice 12 : Récupérer les nombres de 10 à 100 et les mettre dans une liste : ")
listeNombre = []
for x in range(10, 101):
    listeNombre.append(x)
print(listeNombre)

print("--------")

# Exercice 13

print("Exercice 13 : Récupérer les nombres de 1 à 200 et mettre seulement les nombres pairs dans une liste : ")
listeNombreImpair = []

for x in range(1, 201):
    if x%2 == 0:
        listeNombreImpair.append(x)

print(listeNombreImpair)

print("--------")

# Exercice 14

print("Exercice 14 : Créer un jeu de dés et afficher le résultat : ")
print("Jeter les dés !")
def jeuDeDes():
    print("Vous avez obtenu le score de : " + str(random.randint(1, 6)))

jeuDeDes()

print("--------")

# Exercice 14 Bonus

print("Exercice 14 Bonus : Créer une jeu de dés qui récupère le nombre total de lancés et en tire une moyenne : ")
def jeuDeDesMoyenne(nombre):
    """""
    Pour cet exercice, il faut que je créer un tableau qui récupère le nombre de fois où les dés sont lancés.
    Les dés sont lancés autant de fois que l'utilisateur le souhaite. En effet, j'ai créé une variable "nombre" qui récupère le choix de l'utilisateur
    Chaque fois que les dés sont lancés, ils sont renseignés dans le tableau que j'ai créé au tout début.
    Une fois le dés lancé, sont résultat s'ajoute à la fin du tableau.
    Une fois le tableau complété, j'additionne chaque nombre tiré
    Lorsque mes nombres se sont ajoutés, je les divise par le nombre de fois que les dés ont été lancés et j'obtiens ma moyenne :)
    """""

    result = []
    for x in range(nombre):
    # je vérifie le nombre inséré par l'utilisateur
    # print(nombre)
      result.append(random.randint(1,6))
    # je vérifie que le tableau ait bien des données
    # print(result)
    moyenne = sum(result) / nombre
    # je vérifie le bon résultat des données présentes dans le tableau
    # print(sum(result))
    print("Les dés ont été lancés " + str(nombre) + " fois. La moyenne des résultats est le suivant : " + str(moyenne) + ".")

jeuDeDesMoyenne(5)

print("--------")

# Exercice 15

print("Exercice 15 : Récupérer le nombre total d'une lettre au sein d'une phrase : ")
phraseDeux = "Voila les amis. Alors ça va ?"
# le .lower() permet mettre toute la phrase en miniscule pour pouvoir compter toutes les lettres "a" miniscules
print("Il y a " + str(phraseDeux.lower().count("a")) + " fois la lettre a")
print("--------")

# Exercice 15 Bonus 1 :

print("Exercice 15 Bonus 1 :  ")
# J'utilise le package counter pour compter le nombre d'occurence de chaque caractère
# Ensuite, le most_common me permet de récupérer le top 1 qui est réutilisé le plus de fois.
collection = Counter(phraseDeux.lower()).most_common(1)[0]
print(collection)
print("--------")

# Exercice 15 Bonus 2 :

# Je sais que le caractère le plus utilisé est l'espace, je l'ai donc remplacé par un b
print(phraseDeux.lower().replace(' ', 'b'))
print(collection)
print("--------")


# Exercice 16

liste1 = [1,2,3,4,5,6,7,8]
# le premier : permet de dire que je commence au début, le deuxième : permet de dire que je vais jusqu'à la fin
# le 2 permet de dire que je prends un index sur 2, donc 1 3 5 7
print(liste1[::2])

#artzvincent@gmail.com