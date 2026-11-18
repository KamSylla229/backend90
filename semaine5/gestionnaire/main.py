
from taches import ajouter_tache
from stockage import sauvegarder_taches, charger_taches

taches = charger_taches("taches.json")
while True :
    print("1. Ajouter une tâche")
    print ("2. Voir mes tâche")
    print ("3. Quitter")

    choix = input("entrer votre choix : " ).strip()
    if choix == "1" :
        nouvelle_tache=input("entrer la nouvelle tâche :")
        taches = ajouter_tache(taches, nouvelle_tache)
        sauvegarder_taches(taches, "taches.json")
        print("Tâche ajoutée")

    elif choix == "2" :
        if len(taches) == 0:
            print("Aucune tâche")
        else:
            for tache in taches:
                print (tache["id"], "-", tache["titre"])
    elif choix == "3":
        print("Aurevoir")
        break
    else:
        print("Choix inconnu")
        


 










