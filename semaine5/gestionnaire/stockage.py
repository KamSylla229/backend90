import json

def sauvegarder_taches(taches, chemin):
    with open(chemin, "w", encoding="utf-8") as fichier:
        json.dump(taches, fichier)



def charger_taches(chemin):
    try:
        with open(chemin, "r", encoding="utf-8") as fichier:
            return json.load(fichier)
    except FileNotFoundError:
        return []

