from taches import ajouter_tache

# TEST 1 : Ajouter une tâche à une liste vide
def test_ajout_liste_vide():
    taches = []

    resultat = ajouter_tache(taches, "Lire")

    assert resultat == [
        {"id": 1, "titre": "Lire", "fait": False}
    ]


# TEST 2 : La deuxième tâche doit recevoir l'ID 2
def test_deuxieme_tache_id_2():
    taches = [{"id": 1, "titre": "Lire", "fait": False}]
    resultat = ajouter_tache(taches, "coder")
    assert resultat[1]["id"] == 2

    

# TEST 3 : Un titre composé uniquement d'espaces ne doit rien ajouter
def test_titre_espaces_ne_change_rien():
    taches = []
    ancienne_liste = taches.copy()

    resultat = ajouter_tache(taches, "   ")

    assert resultat == ancienne_liste

#Test 4
def test_titre_nettoye():
    assert ajouter_tache([], "  Lire  ") == [{"id": 1, "titre": "Lire", "fait": False}]

#Test 5 
def test_titre_vide():
    assert ajouter_tache([], "") == []

#test 6
def test_deuxieme_tache_titre():
    taches = [{"id": 1, "titre": "Lire", "fait": False}]
    resultat = ajouter_tache(taches, "coder")
    assert resultat[1]["titre"] == "coder"


