prix = input("Entrez le prix :")
prix = int(prix)
quantite = input("Entrez la quantité :")
quantite = int(quantite)
total_prix = prix * quantite
if total_prix >= 50000:
    total_remise = int(total_prix - (total_prix *0.1))
    print(f"Remise appliquée. Total à payer : { total_remise } FCFA")
else:
    print(f"Total à payer : {total_prix} FCFA")