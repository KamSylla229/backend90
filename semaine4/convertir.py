def convertir_en_entier(valeur):
    try:
        return int(valeur)
    except ValueError:
        return None


assert convertir_en_entier("42") == 42
assert convertir_en_entier("abc") is None
assert convertir_en_entier("") is None
print("Tous les tests passent")
