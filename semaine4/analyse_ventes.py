def convertir_en_entier(valeur):
    try:
        return int(valeur)
    except ValueError:
        return None


def lire_ventes(chemin):
    ventes = []
    with open(chemin, encoding="utf-8") as fichier:
        next(fichier)
        for ligne in fichier:
            ligne = ligne.strip()
            if ligne == "":
                continue
            morceaux = ligne.split(",")
            produit = morceaux[1]
            montant = convertir_en_entier(morceaux[2])
            if montant is None:
                print("Ligne ignorée (montant invalide) :", ligne)
                continue
            ventes.append({"produit": produit, "montant": montant})
    return ventes


def total_par_produit(ventes):
    resultat = {}
    for vente in ventes:
        produit = vente["produit"]
        montant = vente["montant"]
        if produit in resultat:
            resultat[produit] += montant
        else:
            resultat[produit] = montant
    return resultat


def main():
    try:
        ventes = lire_ventes("ventes_test.csv")
    except FileNotFoundError:
        print("Erreur : le fichier ventes.csv est introuvable.")
        return

    nombre = len(ventes)
    if nombre == 0:
        print("Aucune vente valide.")
        return

    total = 0
    for vente in ventes:
        total += vente["montant"]
    moyenne = total / nombre

    print("Nombre de ventes :", nombre)
    print("Total :", total)
    print("Moyenne :", round(moyenne, 2))
    print("Total par produit :")
    totaux = total_par_produit(ventes)
    for produit in totaux:
        print("-", produit, ":", totaux[produit])


main()