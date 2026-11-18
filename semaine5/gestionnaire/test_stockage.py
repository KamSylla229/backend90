from stockage import sauvegarder_taches, charger_taches

# Test 1 : sauvegarder puis recharger donne la même liste
liste = [{"id": 1, "titre": "Lire", "fait": False}]
sauvegarder_taches(liste, "test.json")
assert charger_taches("test.json") == liste

# Test 2 : fichier absent → liste vide
assert charger_taches("absent.json") == []

# Test 3 : liste vide sauvegardée puis rechargée → liste vide
sauvegarder_taches([], "test.json")
assert charger_taches("test.json") == []

#Test 4: 
lire_coder = [{ "id": 2, "titre": "Lire", "fait": False},
               {"id": 3, "titre": "coder", "fait": True}]
sauvegarder_taches(lire_coder, "test.json")
assert charger_taches("test.json") == lire_coder

print("Tous les tests de stockage passent !")