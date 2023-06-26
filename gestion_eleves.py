def ajouter_eleve():
    id_eleve = input("Entrez l'identifiant de l'élève : ")
    nom_eleve = input("Entrez le nom de l'élève : ")
    eleves[id_eleve] = nom_eleve
    print("Élève ajouté avec succès !")

def modifier_eleve():
    id_eleve = input("Entrez l'identifiant de l'élève à modifier : ")
    if id_eleve in eleves:
        nouveau_nom = input("Entrez le nouveau nom de l'élève : ")
        eleves[id_eleve] = nouveau_nom
        print("Élève mis à jour avec succès !")
    else:
        print("L'élève n'existe pas.")

def supprimer_eleve():
    id_eleve = input("Entrez l'identifiant de l'élève à supprimer : ")
    if id_eleve in eleves:
        del eleves[id_eleve]
        print("Élève supprimé avec succès !")
    else:
        print("L'élève n'existe pas.")

eleves = {}
def afficher_tous_les_eleves():
    if eleves:
        print("Liste complète des élèves :")
        for id_eleve, nom_eleve in eleves.items():
            print(f"ID : {id_eleve}, Nom : {nom_eleve}")
    else:
        print("Aucun élève dans la liste.")

def gestion_eleves():
    print("Bienvenue dans la gestion des élèves !")
    while True:
        print("\nMenu :")
        print("1. Ajouter un élève")
        print("2. Modifier un élève")
        print("3. Supprimer un élève")
        print("4. Afficher la liste complète des élèves")
        print("5. Quitter")

        choix = input("Veuillez sélectionner une option (1-5) : ")

        if choix == "1":
            ajouter_eleve()
        elif choix == "2":
            modifier_eleve()
        elif choix == "3":
            supprimer_eleve()
        elif choix == "4":
            afficher_tous_les_eleves()
        elif choix == "5":
            break
        else:
            print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    gestion_eleves()
