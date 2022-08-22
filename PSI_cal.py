import os
import math 

f1= [] #pdb fichier 1
f2= [] #pdb fichier 2

idt1=[]
x1=[]
y1=[]
z1=[]

idt2=[]
x2=[]
y2=[]
z2=[]

#Recuperation des sequences alignees :
l1=[]
l2=[]
with open("test_prog.txt", "r") as res_align:
	for ligne in res_align: 
		#ligne_res= ligne.split()
		#print(ligne_res)
		#for i in range(0,len(ligne_res),1):
		if ligne.startswith(('g','c','a','u','-')): 
			l1.append(ligne)
			l2.append(ligne)
l1= l1[0]
l2= l2[-1]
print(type(l2))
print(l1, l2)

#Compte les calpha alignes
position1=[]
position2=[]
cpt=0
for i in range(0,len(l1),1):
	if l1[i] != "-" and l2[i] != "-":
		cpt+=1				
		position1 = l1.index(l1[i])
		position2 = l2.index(l2[i])
		print(position1, position2)
print(cpt)

#Ouverture des pdb correspondants aux alignements :
#with open("test_prog.txt",'r') as res_align: 
#	for ligne in res_align: 
#		if ligne[8:15] == "Chain_1":
#			idt1.append(ligne[17:25]) 
#		elif ligne[8:15] == "Chain_2":
#			idt2.append(ligne[17:25])

#filename1 = "\\wsl$\Ubuntu\home\henes\exo_python\idt1.txt"
#filename2 = "\\wsl$\Ubuntu\home\henes\exo_python\idt2.txt"

#Recuperation des coordonnees des calpha alignes :
#with open(filename1,"r") as f1 : 
	#for ligne in f1:
#		if ligne[0:6]== 'HEADER': 
#			idt1.append(ligne[62:66])
#		elif ligne[0:4] == 'ATOM' and ligne[23:26] == position1:
#			x1.append(float(ligne[31:38]))
#			y1.append(float(ligne[39:46]))
#			z1.append(float(ligne[47:54]))

#with open(filename2,"r") as f2 : 
#	for ligne in f2:
#		if ligne[0:6]== 'HEADER': 
#			idt2.append(ligne[62:66])
#		elif ligne[0:4] == 'ATOM' and ligne[23:26] == position2:
#			x2.append(float(ligne[31:38]))
#			y2.append(float(ligne[39:46]))
#			z2.append(float(ligne[47:54]))
	
#Calcul des distances : 
#dx=[]
#dy=[]
#dz=[]
#for i in range(0,len(x),1): 
#	for j in range(i+1, len(x)-1,1):
#		#paire= idt[i], idt[j]
#		dx= x1[i]-x2[j]
#		dy= y1[i]-y2[j]
#		dz= z1[i]-z2[j]
#		#print(round(dx,3), round (dy,3), round(dz, 3))
#		d = math.sqrt((dx**2)+(dy**2)+(dz**2))
#		if d < 4: 
#			print(d)
		
		
#Calcul PSI :
n_al = []
N=[]
nom1= []
nom2=[]
longueur1=[]
longueur2=[]
with open("test_prog.txt", "r") as res_align:
	for ligne in res_align:
		if ligne[10:17] == "Chain_1":
			longueur1.append(ligne[19:21])
		elif ligne[10:17] == "Chain_2":
			longueur2.append(ligne[19:21])	
		elif ligne[10:17] == "Chain_1":
			nom1.append(ligne[19:21])
		elif ligne[10:17] == "Chain_1":
			nom2.append(ligne[19:21])
		elif longueur1 > longueur2 :
			N = longueur2
		elif longueur1 < longueur2:
			N = longueur1
print('RNA le plus petit contient ',N,'nucleotides.')

#PSI = 100*(n_al/N)
#print(PSI)

#for i in range(0,len(x),1):
	#print(idt[i],x[i],y[i],z[i])
