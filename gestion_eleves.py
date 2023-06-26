def ajouter_eleve():
    id_eleve = input("Entrez l'identifiant de l'élève : ")
    nom_eleve = input("Entrez le nom de l'élève : ")
    eleves[id_eleve] = nom_eleve
    print("Élève ajouté avec succès !")
