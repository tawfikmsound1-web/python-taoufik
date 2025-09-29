mot1 = input("Entrez le premier mot : ")
mot2 = input("Entrez le deuxième mot : ")

if mot1 < mot2:
    premier = mot1
    deuxieme = mot2
elif mot2 < mot1:
    premier = mot2
    deuxieme = mot1
else:
    premier = mot1
    deuxieme = mot2
    print("Les deux mots sont identiques.")

print(f"\n--- Méthode IF/ELSE ---")
print(f"L'ordre lexicographique est : {premier}, {deuxieme}")