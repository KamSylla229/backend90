def compter_voyelles(texte):
    voyelle= "aeiouy"
    compteur = 0
    for lettre in texte.lower():
        if lettre in voyelle:
            compteur = compteur + 1
    return compteur




assert compter_voyelles("Bonjour") == 3         
assert compter_voyelles("PYTHON") == 2
assert compter_voyelles("") == 0
print("Tous les tests passent")