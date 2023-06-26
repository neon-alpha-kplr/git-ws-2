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
