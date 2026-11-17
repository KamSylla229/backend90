
from taches import ajouter_tache
from stockage import sauvegarder_taches, charger_taches

taches = charger_taches("taches.json")
taches = ajouter_tache(taches, "Réviser Python")
sauvegarder_taches(taches, "taches.json")
print(taches)











# from taches import ajouter_tache

# # Initialiser une liste vide
# taches = []

# # Ajouter deux tâches
# ajouter_tache(taches, "Apprendre Python")
# ajouter_tache(taches, "Apprendre Django")

# # Afficher la liste des tâches
# print("Ma liste de tâches :")
# print(taches)