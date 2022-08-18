tmscore1= ["TMSCORE1"] #Déclaration de listes vides à remplir
tmscore2= ["TMSCORE2"]
rmsd=["RMSD"]
nom_pdb1=["PDB1"]
nom_pdb2=["PDB2"]
idseq=["SEQ_ID"]
with open("res_rnalign.txt", "r") as res: #Ouverture du fichier "res_rnalign.txt"
	for ligne in res:	#Pour chaque ligne du fichier
		if ligne[0:8] == "TM-score" and ligne[-31:-24]=="Chain_1":	
			tmscore1.append(float(ligne[10:18]))	#Ajout des 1e valeurs TM-score dans une liste
		elif ligne[0:8] == "TM-score" and ligne[-31:-24]=="Chain_2":
			tmscore2.append(float(ligne[10:18]))	#Ajout des 2e valeurs TM-score dans une liste
		elif ligne[20:24] == "RMSD":			
			rmsd.append(float(ligne[25:32]))	#Ajout des valeurs RMSD dans une liste
			idseq.append(float(ligne[-6:-1]))	#Ajout des scores d'identité dans une liste
		elif ligne[8:15] == "Chain_1":
			nom_pdb1.append(ligne[17:25]) #Ajout des identifiants dans une liste
		elif ligne[8:15] == "Chain_2":
			nom_pdb2.append(ligne[17:25]) #Ajout des identifiants dans une liste
			
for i in range(0,len(nom_pdb1),1):
	print(nom_pdb1[i],nom_pdb2[i],tmscore1[i], tmscore2[i],rmsd[i],idseq[i])  #Affichage des données

