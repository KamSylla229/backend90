import json

def sauvegarder_taches(taches, chemin):
    with open(chemin, "w", encoding="utf-8") as fichier:
        json.dump(taches, fichier)

# # Essai (à supprimer après)
# sauvegarder_taches([{"id": 1, "titre": "Lire", "fait": False}], "test.json")


def charger_taches(chemin):
    try:
        with open(chemin, "r", encoding="utf-8") as fichier:
            return json.load(fichier)
    except FileNotFoundError:
        return []

# Essais (à supprimer après)
print(charger_taches("test.json"))
print(charger_taches("absent.json"))