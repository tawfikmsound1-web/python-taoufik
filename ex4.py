P_SEUIL = 2.3
V_SEUIL = 7.41

print("--- Système de Surveillance de l'Enceinte Pressurisée ---")
print(f"Pression Seuil (pSeuil) : {P_SEUIL}")
print(f"Volume Seuil (vSeuil) : {V_SEUIL}")
print("-" * 45)

try:
    p_courante = float(input("Entrez la pression courante (P) : "))
    v_courant = float(input("Entrez le volume courant (V) : "))

except ValueError:
    print("\nErreur de saisie : Veuillez entrer des nombres valides pour la pression et le volume.")
    exit()

print("\n--- Comportement du Système ---")

if p_courante > P_SEUIL and v_courant > V_SEUIL:
    print("⚠️ DANGER CRITIQUE : Arrêt immédiat du système. Pression et Volume trop élevés.")

elif p_courante > P_SEUIL:
    print("⚠️ ATTENTION : Pression trop élevée.")
    print("Action recommandée : Demander d'augmenter le volume de l'enceinte.")

elif v_courant > V_SEUIL:
    print("⚠️ ATTENTION : Volume trop élevé.")
    print("Action recommandée : Demander de diminuer le volume de l'enceinte.")

else:
    print("✅ STATUT OK : Les conditions de pression et de volume sont dans les limites sécuritaires.")