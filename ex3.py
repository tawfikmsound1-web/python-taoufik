import math
import cmath

a = float(input("Donnez a (non nul) : "))
b = float(input("Donnez b : "))
c = float(input("Donnez c : "))

if a == 0:
    print("Erreur : 'a' doit être non nul pour une équation quadratique.")

delta = b**2 - 4*a*c

print("\n--- Résolution dans R ---")
if delta > 0:
    x1 = (-b - math.sqrt(delta)) / (2*a)
    x2 = (-b + math.sqrt(delta)) / (2*a)
    print("Deux solutions réelles : x1 =", x1, " , x2 =", x2)
elif delta == 0:
    x = -b / (2*a)
    print("Une solution réelle double : x =", x)
else:
    print("Pas de solution réelle (Δ < 0)")

print("\n--- Résolution dans C ---")
x1 = (-b - cmath.sqrt(delta)) / (2*a)
x2 = (-b + cmath.sqrt(delta)) / (2*a)
print("Solutions dans C : x1 =", x1, " , x2 =", x2)
