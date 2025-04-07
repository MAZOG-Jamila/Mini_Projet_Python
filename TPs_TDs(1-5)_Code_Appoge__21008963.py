###MAZOG Jamila
##Code Appoge: 21008963
###TDs/TPs (1-5) PYTHON

#######TP1######

#EXERCICE1:
Str1, int1, dec1 = ("ceci est une chaîne", 12, 15.0)

print(type(Str1))
print(type(int1))
print(type(dec1))

nom, prenom, age = ("Park", "Tom", 30)

print(type(nom))
print(type(prenom))
print(type(age))

#EXERCICE2:

###Calcul de la moyenne des notes
note_anglais = float(input("Saisir la note d'Anglais : "))
coefficient_anglais = float(input("Saisir le coefficient d'Anglais : "))

note_physique = float(input("Saisir la note de Physique : "))
coefficient_physique = float(input("Saisir le coefficient de Physique : "))

note_maths = float(input("Saisir la note de Maths : "))
coefficient_maths = float(input("Saisir le coefficient de Maths : "))

note_svt = float(input("Saisir la note de SVT : "))
coefficient_svt = float(input("Saisir le coefficient de SVT : "))

moyenne = (note_anglais * coefficient_anglais + note_physique * coefficient_physique + note_maths * coefficient_maths + note_svt * coefficient_svt) / (coefficient_anglais + coefficient_physique + coefficient_maths + coefficient_svt)

print("La moyenne des notes est : ", moyenne)

###Vérification du budget
budget = float(input("Saisir le budget : "))
achats = float(input("Saisir le montant des achats : "))

if budget >= achats:
    print("Le budget permet de payer les achats.")
else:
    print("Le budget ne permet pas de payer les achats.")

#EXERCICE3:

import math


rayon = float(input("Saisir le rayon du cône : "))
hauteur = float(input("Saisir la hauteur du cône : "))

volume = (1/3) * math.pi * (rayon**2) * hauteur

print("Le volume du cône est : ", volume)

#EXERCICE4:

import math

Rg = float(input("Saisir le rayon extérieur du disque : "))
Rp = float(input("Saisir le rayon intérieur du disque : "))

surface = math.pi * (Rg**2 - Rp**2)

print("La surface du disque découpé est : ", surface)

#EXERCICE5:

phrase = input("Saisir une phrase : ")

longueur = len(phrase)

if longueur % 2 == 0:
    
    print(phrase[:longueur//2])
else:
    
    print(phrase[longueur//2 + 1:])



#######TP2##########

#EXERCICE1:

#1
Semaine = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
print(Semaine)
#2
Couleurs = ["Rouge", "Bleu", "Vert", "Jaune", "Orange"]
print(Couleurs)
#3
Reels = [1.2, 3.4, 5.6, 7.8, 9.0, 1.1, 2.2]
print(Reels[1], Reels[3], Reels[5])

#EXERCICE2:

mylist = ['apple', 'banana', 'cherry']
print(mylist[1]) # Résultat : banana

mylist = ['apple', 'banana', 'banana', 'cherry']
print(mylist[2]) # Résultat : banana

thislist = ['apple', 'banana', 'cherry']
print(len(thislist)) # Résultat : 3

mylist = ['apple', 'banana', 'cherry']
print(mylist[-1]) # Résultat : cherry

fruits = ["apple", "banana", "cherry"]
print(fruits[1]) # Résultat : banana

mylist = ['apple', 'banana', 'cherry', 'orange', 'kiwi']
print(mylist[1:4]) # Résultat : ['banana', 'cherry', 'orange']

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5]) # Résultat : ['cherry', 'orange', 'kiwi']

#EXERCICE3:

Matieres = ["Anglais", "Physique", "Maths", "Svt"]
print(Matieres)

Matieres = ["Anglais", "Physique", "Maths", "Svt"]
Matieres.append("Histoire")
Matieres.append("Geographie")
print(Matieres)

 
print(Matieres[:4])
print(Matieres[-3:])
print(Matieres[1:4])

#EXERCICE4:

mylist = ['apple', 'banana', 'cherry']
mylist[0] = 'kiwi'
print(mylist[1]) # Résultat : banana

fruits = ["apple", "banana", "cherry"]
fruits[0] = 'kiwi'
print(fruits) # Résultat : ['kiwi', 'banana', 'cherry']

mylist = ['apple', 'banana', 'cherry']
mylist[1:2] = ['kiwi', 'mango']
print(mylist[2]) # Résultat : mango

mylist = ['apple', 'banana', 'cherry']
mylist.insert(0, 'orange')
print(mylist[1]) # Résultat : apple

fruits = ["apple", "banana", "cherry"]
fruits.append('orange')
print(fruits) # Résultat : ['apple', 'banana', 'cherry', 'orange']

fruits = ["apple", "banana", "cherry"]
fruits.insert(1, 'lemon')
print(fruits) # Résultat : ['apple', 'lemon', 'banana', 'cherry']

#EXERCICE5:

Semaine = ['lun', 'mar', 'mer', 'jeu', 'ven', 'sam', 'dim']
Semaine.remove('mer')
print(Semaine) # Résultat : ['lun', 'mar', 'jeu', 'ven', 'sam', 'dim']

mylist = ['apple', 'banana', 'cherry']
mylist.pop(1)
print(mylist) # Résultat : ['apple', 'cherry']

fruits = ['apple', 'banana', 'cherry']
fruits.clear() # La fonction clear permet de vider la liste
print(fruits) # Résultat : []


############TP3#############

#EXERCICE1:

nombres = [4, 8, 15, 16, 23, 42]

def affListe(lst):
    for element in lst:
        print(element)

# Test de la fonction
affListe(nombres)

#EXERCICE2:

def somme_liste(liste):
    return sum(liste)

def moyenne_liste(liste):
    return somme_liste(liste) / len(liste)

nombres = [4, 8, 15, 16, 23, 42]
somme = somme_liste(nombres)
moyenne = moyenne_liste(nombres)

print("Somme des éléments :", somme)
print("Moyenne des éléments :", moyenne)

#EXERCICE3:

def extraire_pairs(liste):
    return [x for x in liste if x % 2 == 0]

nombres = [4, 8, 15, 16, 23, 42]
pairs = extraire_pairs(nombres)

print("Liste des nombres pairs :", pairs)

#EXERCICE4:

def element_existe(liste, element):
    return element in liste

nombres = [4, 8, 15, 16, 23, 42]

print(element_existe(nombres, 15))  # Résultat : True
print(element_existe(nombres, 50))  # Résultat : False

#EXERCICE5:

def liste_carres(liste):
    return [x**2 for x in liste]

nombres = [4, 8, 15, 16, 23, 42]
carres = liste_carres(nombres)

print("Liste des carrés :", carres)

#EXERCICE6:

def trouver_min_max(liste):
    return (min(liste), max(liste))

nombres = [4, 8, 15, 16, 23, 42]
min_max = trouver_min_max(nombres)
print("Minimum et Maximum :", min_max)

#EXERCICE7:

nombres = [7, 14, 21, 28, 35]
autres_nombres = [7, 11, 19, 24, 33]
def fusionner_et_trier(liste1, liste2):
    return sorted(liste1 +liste2)
resultat = fusionner_et_trier(nombres, autres_nombres)
print(resultat)

#EXERCICE8:

def est_palindrome(mot ):
    return mot == mot[::-1]

mots = ["radar", "python", "level"]
for mot in mots:
    print(est_palindrome(mot))



#############TP4##########

#EXERCICE1:

annuaire = {}

def ajouter_personne():
    personne = input("Entrez le nom et l'âge (Nom:Âge) : ")
    nom, age = personne.split(":")
    annuaire[nom] = int(age)
    print(f"{nom} ajouté(e) avec succès !")

def rechercher_personne():
    nom = input("Entrez le nom de la personne à rechercher : ")
    if nom in annuaire:
        print(f"{nom} a {annuaire[nom]} ans.")
    else:
        print(f"{nom} non trouvé(e) dans l'annuaire.")

def supprimer_personne():
    nom = input("Entrez le nom de la personne à supprimer : ")
    if nom in annuaire:
        del annuaire[nom]
        print(f"{nom} supprimé(e) avec succès !")
    else:
        print(f"{nom} non trouvé(e) dans l'annuaire.")

def afficher_annuaire():
    print("Annuaire :")
    for nom, age in annuaire.items():
        print(f"{nom} : {age} ans")

def main():
    while True:
        print("\nMenu :")
        print("1. Ajouter une personne")
        print("2. Rechercher une personne")
        print("3. Supprimer une personne")
        print("4. Afficher l'annuaire")
        print("5. Quitter")
        choix = input("Entrez votre choix : ")
        if choix == "1":
            ajouter_personne()
        elif choix == "2":
            rechercher_personne()
        elif choix == "3":
            supprimer_personne()
        elif choix == "4":
            afficher_annuaire()
        elif choix == "5":
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()


#EXERCICE2 :

dict1={"a":1,"c":'AHMED'}
dict2={"c":'HI',"d":41}
dict3={}
def Fusionner_dictionnaires(dict1,dict2):
    dict3.update(dict1)
    dict3.update(dict2)
    return dict3
fusion=Fusionner_dictionnaires(dict1,dict2)
print(f"fusion des deux dictionnaire est: {fusion}")

def Trie_alphabitique(dict1):
    return{key:dict1[key]for key in sorted(dict1)}
def fusion3(dict1,dict2):
    for key in sorted(dict1):
     Trier=Trie_alphabitique(dict1)
     print(f"les clé trier par ordre:{Trier}")


fusion3(dict1,dict2)

def fusion3(dict1,dict2):
   for key in sorted(dict1):
       if key in dict2:
          if((type(dict1[key])is (int or float))) and((type(dict2[key])is(int or float))):
             dict3=dict1[key]+dict2[key]
       else:
         dict3=str(dict1[key]+str(dict2[key]))
       return dict3
dict3=(dict1,dict2)
print(dict3)

#EXERCICE3:

def fusionner_dictionnaires(d1, d2):
    d_fusionne = {**d1, **d2}
    
    for cle in d1:
        if cle in d2:
            if isinstance(d1[cle], (int, float)) and isinstance(d2[cle], (int, float)):
                d_fusionne[cle] = d1[cle] + d2[cle]
            elif isinstance(d1[cle], str) and isinstance(d2[cle], str):
                d_fusionne[cle] = d1[cle] + d2[cle]
    
    d_fusionne = dict(sorted(d_fusionne.items()))
    
    return d_fusionne

# Exemple d'utilisation
d1 = {"a": 10, "b": "test"}
d2 = {"a": 5, "c": "data"}

resultat = fusionner_dictionnaires(d1, d2)
print(resultat)  # Résultat : {"a": 15, "b": "test", "c": "data"}

#EXERCICE4:

def analyser_notes(fichier):
    # Initialisation des variables
    notes = []
    total = 0
    
    # Lecture des données du fichier
    with open(fichier, 'r') as f:
        for ligne in f:
            nom, note = ligne.strip().split(',')
            notes.append((nom, int(note)))
            total += int(note)
    
    # Calcul de la note moyenne
    moyenne = total / len(notes)
    
    # Affichage des noms des étudiants ayant une note supérieure à la moyenne
    print("Étudiants ayant une note supérieure à la moyenne :")
    for nom, note in notes:
        if note > moyenne:
            print(f"{nom} : {note}")

# Appel de la fonction
analyser_notes('notes.txt')

#EXERCICE5:

class Etudiant:
    def __init__(self, nom, age, note):
        self.nom = nom
        self.age = age
        self.note = note

    def afficher_info(self):
        print(f"Nom : {self.nom}")
        print(f"Âge : {self.age} ans")
        print(f"Note : {self.note}/20")

    @staticmethod
    def calculer_moyenne(etudiants):
        total = sum(etudiant.note for etudiant in etudiants)
        return total / len(etudiants)

# Création d'objets Etudiant
etudiant1 = Etudiant("Jean", 20, 15)
etudiant2 = Etudiant("Marie", 22, 18)
etudiant3 = Etudiant("Pierre", 21, 12)

# Affichage des informations
etudiant1.afficher_info()
etudiant2.afficher_info()
etudiant3.afficher_info()

# Calcul de la moyenne
etudiants = [etudiant1, etudiant2, etudiant3]
moyenne = Etudiant.calculer_moyenne(etudiants)
print(f"Moyenne des notes : {moyenne:.2f}/20")

#EXERCICE6:

class CarnetAdresses:
    def __init__(self):
        self.contacts = {}

    def ajouter_contact(self, nom, email, telephone):
        self.contacts[nom] = {"email": email, "telephone": telephone}

    def supprimer_contact(self, nom):
        self.contacts.pop(nom, None)

    def rechercher_contact(self, nom):
        return self.contacts.get(nom, "Contact non trouvé")

    def afficher_contacts(self):
        return self.contacts
    
    def sauvegarder_contacts(self, fichier):
        with open(fichier, "w", newline="") as f:
            for nom, infos in self.contacts.items():
                email = infos["email"]
                telephone = infos["telephone"]
                f.write(f"{nom},{email},{telephone}\n")

# Test du programme
carnet = CarnetAdresses()
carnet.ajouter_contact("Maria", "mariaem@gmail.com", "0612151382")
carnet.ajouter_contact("Tom", "tomjmh@gmail.com", "079123415")

print(carnet.rechercher_contact("Maria"))
print("\n", carnet.afficher_contacts())

carnet.supprimer_contact("Maria")
print("\n", carnet.afficher_contacts())

carnet.sauvegarder_contacts("contacts.txt")



############TP5###########

#EXERCICE1:

import numpy as np

# Création des tableaux
tableau_1D = np.arange(10)
tableau_2D = np.random.rand(3, 3)
tableau_3D = np.zeros((2, 3, 4))
print("Tableau 1D:", tableau_1D)
print("\nTableau 2D:\n", tableau_2D)
print("\nTableau 3D:\n", tableau_3D)

# Accès aux éléments
troisieme_element = tableau_1D[2]
deuxieme_ligne_premiere_colonne = tableau_2D[1, 0]

# Modification d'un élément
tableau_3D[0, 1, 2] = 5
print("Tableau 3D modifié :\n", tableau_3D)

# Récupération des éléments
trois_premiers_elements = tableau_1D[:3]
derniere_colonne = tableau_2D[:, 2]

print("Tableau 1D :", tableau_1D)
print("Troisième élément :", troisieme_element)
print("Tableau 2D :\n", tableau_2D)
print("Deuxième ligne, première colonne :", deuxieme_ligne_premiere_colonne)
print("Tableau 3D :\n", tableau_3D)
print("Trois premiers éléments :", trois_premiers_elements)
print("Dernière colonne :", derniere_colonne)

#EXERCICE2:

import numpy as np

# Création des tableaux
tableau1 = np.array([1, 2, 3, 4, 5])
tableau2 = np.array([6, 7, 8, 9, 10])

# Opérations mathématiques élément par élément
addition = tableau1 + tableau2
soustraction = tableau1 - tableau2
multiplication = tableau1 * tableau2
division = tableau1 / tableau2

print("Addition :", addition)
print("Soustraction :", soustraction)
print("Multiplication :", multiplication)
print("Division :", division)

# Application des fonctions mathématiques
valeurs = np.linspace(0, np.pi, 10)
sinus = np.sin(valeurs)
cosinus = np.cos(valeurs)
exponentielle = np.exp(valeurs)

print("Sinus :", sinus)
print("Cosinus :", cosinus)
print("Exponentielle :", exponentielle)

# Création d'un tableau d'entiers
entiers = np.arange(10)

# Sélection des éléments pairs
pairs = entiers[entiers % 2 == 0]
print("Éléments pairs :", pairs)

# Remplacement les éléments impairs par -1
entiers[entiers % 2 != 0] = -1
print("Entiers modifiés :", entiers)

#EXERCICE3

import numpy as np
# Création d'un tableau de 12 éléments
tableau = np.arange(12)
print("Tableau original :", tableau)

# Transformation en tableau 2D de dimensions (3, 4)
tableau_2D = tableau.reshape(3, 4)
print("Tableau 2D :", tableau_2D)

# Transformation en tableau 3D de dimensions (2, 2, 3)
tableau_3D = tableau.reshape(2, 2, 3)
print("Tableau 3D :\n", tableau_3D)

# Transposition du tableau 2D
tableau_2D_transpose = tableau_2D.T
print("Tableau 2D transposé :\n", tableau_2D_transpose)

# Échange des axes
tableau_2D_echange_axes = np.swapaxes(tableau_2D, 0, 1)
print("Tableau 2D avec échange des axes :\n", tableau_2D_echange_axes)

# Création de deux tableaux 2D de dimensions (2, 3)
tableau_A = np.arange(6).reshape(2, 3)
tableau_B = np.arange(6, 12).reshape(2, 3)

# Concaténation verticale
concat_vertical = np.concatenate((tableau_A, tableau_B), axis=0)
print("Concaténation verticale :\n", concat_vertical)

# Concaténation horizontale
concat_horizontal = np.concatenate((tableau_A, tableau_B), axis=1)
print("Concaténation horizontale :\n", concat_horizontal)

# Division en sous-tableaux
sous_tableau_A, sous_tableau_B = np.vsplit(concat_vertical, 2)
print("Sous-tableau A :\n", sous_tableau_A)
print("Sous-tableau B :\n", sous_tableau_B)

#EXERCICE4:

import numpy as np

#  1
tableau = np.random.rand(5, 5)
print("Tableau aléatoire :\n", tableau)

moyenne_ligne = np.mean(tableau, axis=1)
ecart_type_ligne = np.std(tableau, axis=1)
min_ligne = np.min(tableau, axis=1)
max_ligne = np.max(tableau, axis=1)

print("Moyenne par ligne :", moyenne_ligne)
print("Écart-type par ligne :", ecart_type_ligne)
print("Minimum par ligne :", min_ligne)
print("Maximum par ligne :", max_ligne)

moyenne_colonne = np.mean(tableau, axis=0)
ecart_type_colonne = np.std(tableau, axis=0)
min_colonne = np.min(tableau, axis=0)
max_colonne = np.max(tableau, axis=0)

print("Moyenne par colonne :", moyenne_colonne)
print("Écart-type par colonne :", ecart_type_colonne)
print("Minimum par colonne :", min_colonne)
print("Maximum par colonne :", max_colonne)

# 2
tableau_aleatoire = np.random.rand(10)
print("Tableau aléatoire :", tableau_aleatoire)

tableau_trie = np.sort(tableau_aleatoire)
print("Tableau trié :", tableau_trie)

indice_max = np.argmax(tableau_aleatoire)
print("Indice de l'élément maximum :", indice_max)

# 3
tableau_1D = np.array([1, 2, 3, 4])
print("Tableau 1D :", tableau_1D)

tableau_2D = np.array([[5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print("Tableau 2D :\n", tableau_2D)

resultat = tableau_2D * tableau_1D
print("Résultat de la multiplication :\n", resultat)


#EXERCICE5:

import numpy as np
import matplotlib.pyplot as plt

#  1
np.random.seed(0)
donnees = np.random.randn(100, 3)
matrice_covariance = np.cov(donnees.T)
print("Matrice de covariance :\n", matrice_covariance)

#  2
t = np.linspace(0, 1, 1000)
donnees_sinusoïdales = np.sin(2 * np.pi * 10 * t) + 0.5 * np.sin(2 * np.pi * 20 * t)
transformation_fourier = np.fft.fft(donnees_sinusoïdales)
spectre_frequences = np.abs(transformation_fourier)
freq = np.fft.fftfreq(len(t), d=0.001)

plt.figure(figsize=(10, 6))
plt.plot(freq, spectre_frequences)
plt.xlabel("Fréquence")
plt.ylabel("Amplitude")
plt.title("Spectre de fréquences")
plt.show()

#  3
lancers_de = np.random.randint(1, 7, size=(1000, 2))
sommes = np.sum(lancers_de, axis=1)

plt.figure(figsize=(10, 6))
plt.hist(sommes, bins=11, edgecolor="black")
plt.xlabel("Somme")
plt.ylabel("Fréquence")
plt.title("Histogramme des sommes obtenues")
plt.show()

#EXERCICE6:

import numpy as np

# Création d'un tableau 2D de 12 mois x 3 produits avec valeurs aléatoires entre 100 et 1000
np.random.seed(42)  # Pour la reproductibilité
ventes = np.random.randint(100, 1000, size=(12, 3))
print("Tableau des ventes mensuelles (en unités):")
print(ventes)
#2
# Calcul du total annuel par produit
total_par_produit = np.sum(ventes, axis=0)
print("\nTotal annuel par produit:")
print(f"P1: {total_par_produit[0]}, P2: {total_par_produit[1]}, P3: {total_par_produit[2]}")
#3
# Calcul de la moyenne mensuelle par produit
moyenne_par_produit = np.mean(ventes, axis=0)
print("\nMoyenne mensuelle par produit:")
print(f"P1: {moyenne_par_produit[0]:.2f}, P2: {moyenne_par_produit[1]:.2f}, P3: {moyenne_par_produit[2]:.2f}")

#4
# Identification des mois avec ventes maximales
mois_max = np.argmax(ventes, axis=0) + 1  # +1 car les mois vont de 1 à 12
print("\nMois avec ventes maximales:")
print(f"P1: Mois {mois_max[0]}, P2: Mois {mois_max[1]}, P3: Mois {mois_max[2]}")

#5
# Calcul du taux de croissance mensuel
croissance = np.diff(ventes, axis=0) / ventes[:-1] * 100
print("\nTaux de croissance mensuel (%):")
print(croissance)

#6
# Identification des mois avec plus forte croissance
mois_croissance_max = np.argmax(croissance, axis=0) + 2  # +2 car diff déplace d'un mois
print("\nMois avec plus forte croissance:")
print(f"P1: Mois {mois_croissance_max[0]}, P2: Mois {mois_croissance_max[1]}, P3: Mois {mois_croissance_max[2]}")

#7
# Calcul du total des ventes tous produits confondus par mois
total_par_mois = np.sum(ventes, axis=1)
print("\nTotal des ventes par mois:")
print(total_par_mois)
