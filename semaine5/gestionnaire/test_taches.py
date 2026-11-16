from taches import ajouter_tache

# TEST 1 : Ajouter une tâche à une liste vide
taches = []

resultat = ajouter_tache(taches, "Lire")

assert resultat == [
    {"id": 1, "titre": "Lire", "fait": False}
]


# TEST 2 : La deuxième tâche doit recevoir l'ID 2
ajouter_tache(taches, "Apprendre Python")

assert taches[1] == {
    "id": 2,
    "titre": "Apprendre Python",
    "fait": False
}


# TEST 3 : Un titre composé uniquement d'espaces ne doit rien ajouter
ancienne_liste = taches.copy()

resultat = ajouter_tache(taches, "   ")

assert resultat == ancienne_liste

assert ajouter_tache([], "  Lire  ") == [{"id": 1, "titre": "Lire", "fait": False}]

assert ajouter_tache([], "") == []

print(" Tous les tests sont réussis !")