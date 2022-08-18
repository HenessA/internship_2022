new_liste_pdb=[] #Déclaration de listes vides à remplir
liste_pdb=[]

with open("liste_ID.txt", "r") as ID: #Ouverture du fichier "liste_ID.txt" 
	for ligne in ID:
		liste_ID = ligne.split(',') # Création d'une liste contenant chaque identifiant de structure
		for i in range(0,len(liste_ID),1): 
			for j in range(i+1, len(liste_ID)-1,1):
				print(liste_ID[i]+".pdb"," ", liste_ID[j]+".pdb") # Affichage d'un paire d'identifiant par ligne au 
										   # au format .pdb
		
		
