import math

try:
    nombre = float(input("Veuillez saisir un nombre réel : "))

    if nombre >= 0:
        racine = math.sqrt(nombre)
        print(f"La racine carrée de {nombre} est : {racine}")
    else:
        print("Erreur : Impossible de calculer la racine carrée d'un nombre négatif dans l'ensemble des réels.")

except ValueError:
    print("Erreur de saisie : Veuillez entrer un nombre réel valide.")
