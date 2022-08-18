import os 

col2=[] #Déclaration de listes vides à remplir
col1=[]

with open("liste_pdb.txt", "r") as struc: # Ouverture du fichier "liste_pdb.txt"
 for ligne in struc:			  # comprenant la liste des fichiers de structure d'ARN
  if len(ligne) != 0: 			# Pour chaque ligne n'étant pas vide 
   fichierpdb= ligne.split()		# on ajoute les éléments de la lignes séparés par un espace dans une liste vide
   if len(fichierpdb)==2: 		# On verifie que les lignes contiennent une paire de fichiers
   	os.system("./RNAalign "+ fichierpdb[0]+" "+fichierpdb[1]) # Appel systeme de RNAalign pour lancer les alignements
   
  # print(fichierpdb)		#création d'une liste contenant chaque fichier de structure 
   #for i in fichierpdb:		#Dans la liste de fichiers
    #if i not in col2:	
     #print(fichierpdb[:][1])	#si le fichier n'est pas dans la liste vide col2
     #col2.append(fichierpdb[:][1])	#on ajoute l'élément d'indice 1 à la liste vide col2
     #for j in fichierpdb:
      #if j not in col1:
    	#  col1.append(fichierpdb[:][0])	#on ajoute l'élément d'indice 0 à la liste vide col1
    	 # break

#for i in range(0,len(col1)):		
 #os.system("./RNAalign "+ col1[i]+" "+col2[i]) #Appel système de lancement de RNAalign pour
 				 		#tous les fichiers de la colonne 1 et 2
 

