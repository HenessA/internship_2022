# internship_2022
Scripts on RNA structure data and alignment. 

Etape 1 : Identification des séquences alignées, 
Etape 2 : Comptage des c alpha alignés, 
Etape 3 : Récupération des fichiers pdb correspondants aux structures alignés,
Etape 3': Récupération des coordonnées de position associées,
Etape 4 : Calculs des distances, 
Etape 4': Calcul PSI. 

Input : fichier .txt de l'alignement de deux structures ARN réalisé par l'algorithme RNA-Align. Sha Gong, Chengxin Zhang, Yang Zhang. RNA-align: quick and accurate alignment of RNA 3D structures based on size-independent TM-scoreRNA. (2019) Bioinformatics, 35:  4459-4461.

  Exemple : 

 ************************************************************************
 * RNA-align (Version 20220412): RNA and DNA structural alignment       *
 * Reference: S Gong, C Zhang and Y Zhang (2019) Bioinformatics         *
 * Please email your comments and suggestions to yangzhanglab@umich.edu *
 ************************************************************************

Name of Chain_1: 5FK6.pdb (to be superimposed onto Chain_2)
Name of Chain_2: 2KUV.pdb
Length of Chain_1: 94 residues
Length of Chain_2: 48 residues

Aligned length= 23, RMSD=   3.43, Seq_ID=n_identical/n_aligned= 0.348
TM-score= 0.16456 (if normalized by length of Chain_1, i.e., LN=94, d0=3.30)
TM-score= 0.22945 (if normalized by length of Chain_2, i.e., LN=48, d0=1.64)
(You should use TM-score normalized by length of the reference structure)

(":" denotes residue pairs of d <  5.0 Angstrom, "." denotes other aligned residues)
-ggcuuaucaagagagggagagcgacuggcgcgaagacccccggcaaccagaaauggugccaauuccugcagcggaaacgu-----------------------ugaaa-gaugagcca
 :::::::::                                                     .               ..                       :.    .::::::::
ggcucgauug-----------------------------------------------------u---------------auuuuuaaauuaauucuuaaaaacuac---aaaucgagcc

Total CPU time is  0.03 seconds


Output : à venir...
