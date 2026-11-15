def total_par_produit(ventes):
    resultat = {}
    for vente in ventes :
        produit = vente["produit"]
        montant = vente["montant"]
        if produit in resultat:
            resultat[produit] += montant
        else:
            resultat[produit] = montant
    return resultat


ventes = [
    {"produit": "pain", "montant": 500},
    {"produit": "lait", "montant": 800},
    {"produit": "pain", "montant": 300},
]

assert total_par_produit(ventes) == {"pain": 800, "lait": 800}
assert total_par_produit([{"produit": "riz", "montant": 1000}]) == {"riz": 1000}
assert total_par_produit([]) == {}
print("Tous les tests passent")











# def nombre_ventes_par_produit(ventes):
#     resultat = {}
#     for vente in ventes:
#         produit = vente["produit"]
#         if produit in resultat:
#             resultat[produit] += 1   # trou 1 : on ajoute combien à chaque vente ?
#         else:
#             resultat[produit] = 1      # trou 2 : on démarre à combien la 1re fois ?
#     return resultat



# ventes = [
#     {"produit": "pain", "montant": 500},
#     {"produit": "lait", "montant": 800},
#     {"produit": "pain", "montant": 300},
# ]

# assert nombre_ventes_par_produit(ventes) == {"pain": 2, "lait": 1}
# assert nombre_ventes_par_produit([{"produit": "riz", "montant": 1000}]) == {"riz": 1}
# assert nombre_ventes_par_produit([]) == {}
# print("Tous les tests passent")