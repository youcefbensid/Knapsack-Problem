import math

class Element :
	def __init__(self,nom,poids,gain):
		self.nom=nom
		self.poids=poids
		self.gain=gain

def affichertab(grille,x,y):
	print("Table")
	for i in range(x):
		for j in range(y):
			print(grille[i][j],end =' ')
		print()


def creerMatrice(objets,lignes,colonnes):
	matrice = [[0] * colonnes for _ in range(lignes)]

	for i in range(1,lignes):
		for j in range(1,colonnes):
			if (objets[i-1].poids>j):
				matrice[i][j]=matrice[i-1][j]
			else:
				matrice[i][j]=max(matrice[i-1][j],matrice[i-1][j-objets[i-1].poids] + objets[i-1].gain)
	return matrice

def trouveResultat(matrice,poids,objets):
        i=len(objets)
        resultat = []
        while (i > 0 ):
                if (poids < objets[i-1].poids):
                        i = i-1
                else:
                        if (matrice[i][poids] == matrice[i-1][poids-objets[i-1].poids] +objets[i-1].gain):
                                resultat.append(objets[i-1])
                                poids = poids - objets[i-1].poids
                                i = i-1
                                
                        else:
                                i = i-1
        return resultat
        
        
