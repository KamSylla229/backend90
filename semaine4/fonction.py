def total_payer(prix,quantite):
    prix = int(prix)
    quantite = int(quantite)
    prix_total = prix * quantite
    if prix_total >=50000 :
        montant_a_payer = prix_total - (prix_total * 0.1)
    else:
        montant_a_payer = prix_total
    return montant_a_payer


assert total_payer(2500, 4) == 10000
assert total_payer(10000, 5) == 45000
assert total_payer(12000, 5) == 54000
print("Tous les tests passent")