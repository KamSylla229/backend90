def compteur_mots(phrase):
    mots=phrase.lower().split()
    resultat= {}
    for mot in mots:
        if mot in resultat:
            resultat[mot]= resultat[mot] + 1
        else :
            resultat[mot]= 1
    return resultat


assert compteur_mots("le chat et le chien") == {"le":2,"chat":1,"et":1,"chien":1}    
assert compteur_mots("Le le LE") == {"le":3}
assert compteur_mots("") == {}
print("Tous les tests passent")