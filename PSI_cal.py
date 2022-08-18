import os
import math 

idt1=[]
x1=[]
y1=[]
z1=[]

idt2=[]
x2=[]
y2=[]
z2=[]

#Recuperation des coordonnees de tous les calpha et identifiants : 
#with open("mega_file.pdb","r") as pdb : #contient tous les fichiers pdb
	#for ligne in f1:
#		if ligne[0:6]== 'HEADER': 
#			idt.append(ligne[62:66])
#		elif ligne[0:4] == 'ATOM':
#			x.append(float(ligne[31:38]))
#			y.append(float(ligne[39:46]))
#			z.append(float(ligne[47:54]))

l1=[]
l2=[]


#Recuperation des sequences alignees :
with open("test_prog.txt", "r") as res_align:
	for ligne in res_align: 
		#ligne_res= ligne.split()
		#print(ligne_res)
		#for i in range(0,len(ligne_res),1):
		if ligne.startswith(('g','c','a','u','-')): # Identification des séquences nucléotidiques
			l1.append(ligne)
			l2.append(ligne)
l1= l1[0]
l2= l2[-1]
print(type(l2))
print(l1, l2)


cpt=0
for i in range(0,len(l1),1):
	if l1[i] != "-" and l2[i] != "-":
		cpt+=1				#Compte les calpha alignes
print(cpt)

	
#Calcul des distances : 
#dx=[]
#dy=[]
#dz=[]
#for i in range(0,len(x),1): 
#	for j in range(i+1, len(x)-1,1):
#		#paire= idt[i], idt[j]
#		dx= x[i]-x[j]
#		dy= y[i]-y[j]
#		dz= z[i]-z[j]
#		#print(round(dx,3), round (dy,3), round(dz, 3))
#		d = math.sqrt((dx*dx)+(dy*dy)+(dz*dz))
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

PSI = 100*(n_al/N)
print(PSI)

#for i in range(0,len(x),1):
	#print(idt[i],x[i],y[i],z[i])
