def bienvenue():
	nom = input("veuiller entrer votre nom svp :")
	age = int(input("veuiller entrer votre age svp :"))
	print(f"Bonjour {nom}, tu as {age} ans et bienvenue à l'université")

	"""==================================================================
	ou ce code ci dessous
	nom = input("veuiller entrer votre nom svp :")
	age = int(input("veuiller entrer votre age svp :"))
	print("Bonjour",nom,", tu as ",age," ans et bienvenue à l'université")"""
""" 
	la fonction bienvenu est une fonction qui permet de demander à l'utilisiteur
	son nom et son âge et ensuite lui retourné ça et en le souhaitant bienvenu 
	à l'université
	Le code en dessous en commentaire est une seconde manière d'écrire le code
""" 

def passGen():
	import random # importation du module random
	lettres_minuscules = "abcdefghijklmnopqrstuvwxyz"
	lettres_majuscules = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	chiffres = "0123456789"
	symboles = "!@#$%^&*()"

	tous_caracters = lettres_majuscules + lettres_minuscules + symboles + chiffres
	longueur_code = int(input("Entrer la longueur de votre code :"))
	liste_c = []
	for i in range(longueur_code):
		j = random.choice(tous_caracters)
		liste_c.append(j)

	code = "".join(liste_c)

	print(f"Votre code est : {code}")

""" 
	la fonction passGen permet de génerer des mots de passes aléatoire du 
	nombre de chiffre que l'utilisateur entre. Cool non 😊😊😊
"""	

def  ageUtilisateur():
	x = int(input("svp donner moi ds quelle annee on est actuellement ? :"))
	y = int(input("svp donner moi votre annee de naissance :"))
	print(f" Alors votre age est {x - y} cette annee")

"""
	la fonction ageUtilisateur permet de calculer l'age de l'utlisateur 
	qui fourni l'année actuelle et son année de naissance. Cool non 😊😊😊
"""

def addition():
	a = b = ""
	while not(a.isdigit() and b.isdigit()):
		a = input("Entrer le premier nombre :")
		b = input("Entrer le deuxieme nombre :")
		if not(a.isdigit() and b.isdigit()):
			print("veuiller des nombres valides")
	print(f"le résultat de l'adition de {a} avec {b} est égale à {int(a) + int(b)}")

"""
	la fonction addition une fonction qui permet de calculer l'addition
	de deux entier entrer par l'utilisateur. Cool non 😊😊😊
"""	

def invertow():
	"""A = int(input("Entrer la valeur de A :"))
	B = int(input("Entrer la valeur de  B :"))
	C = A
	A = B
	B = C
	print(f"la nouvel valeur de A est {A} et celle de B est {B}")"""

                    #OU

	A = int(input("Entrer la valeur de A :"))
	B = int(input("Entrer la valeur de  B :"))
	A,B = B,A
	print(f"la nouvel valeur de A est {A} et celle de B est {B}")

"""
	la fonction invertow est une fonction qui permet d'inverser 
	les contenus de deux variables différentes. Cool non 😊😊😊
	le code en commentaire est aussi une manière d'écrire le code.
"""

def Volsphere():
	import math
	x = float(input("veuiller entrer le rayon du sphère :"))
	V = (4*math.pi*(x**3))/3
	print("le volume du sphère est ",format(V,".2f"))

""" la fonction Volsphere est permet de calculer le volume d'un 
	sphere lorsque l'utilisateur entre le rayon du sphére. Cool non 😊😊😊
"""

def soDiv():
	"""x = float(input("Donner la valeur de x :"))
	y = float(input("Donner la valeur de y :"))
	somme = x + y
	soustraction = x - y
	produit = x *y
	if y != 0:
    	division = x/y
   	 	print(f"la division de {x} et de {y} = {division}")
	else:
    	print("la division est impossible veuiller saisir une autre valeur de y")
	print(f"la somme de {x} et de {y} = {somme}") 
	print(f"le produit de {x} et de {y} = {produit}")   
	print(f"la soustration de {x} et de {y} = {soustraction}")"""


	x = float(input("Donner la valeur de x :"))
	y = float(input("Donner la valeur de y :"))
	somme = x + y
	soustraction = x - y
	produit = x *y
	if y != 0:
		division = x/y
		print("la division est = ",format(division,".2f"))
	else:
		print("la division est impossible veuiller saisir une autre valeur de y")
	print(f"la somme est = ",format(somme,".2f")) 
	print(f"le produit est = ",format(produit,".2f"))   
	print(f"la soustration est = ",format(soustraction,".2f"))

""" la fonction soDiv() permet de calculer la somme, la soustration
	et la division de deux nombres réels. Cool non 😊😊😊
"""
def tabMul():
	n = 0
	x = int(input("la table de multiplication de ? :"))
	while n < 10 :
		n+=1
		print(n,"*",x,"=",n*x)

"""
	la fonction tabMul permet d'avoir la table de multiplication 
	du nombre ou chiffre spécifié par l'utlisateur. Cool non 😊😊😊
"""

def classement():
	students = []
	for _ in range(int(input("Nombre d'étudiant : "))):
		name = input("Entrer le nom :")
		score = float(input("Entrer le score :")) 
		students.append([name, score])

	scores = [student[1] for student in students]
	second_lowest_score = sorted(set(scores))[1]
	second_lowest_students = [student[0] for student in students if student[1] == second_lowest_score]
	second_lowest_students.sort()
	for name in second_lowest_students:
		print(name)
"""
	la fonction classement permet de donner nom de l'étudiant qui a 
	eu  la plus forte note de la salle. Cool non 😊😊😊
"""

def searchint():
	x =int(input("Entrer la valeur de la premiere extrémité de l'interval :"))
	y =int(input("Entrer la valeur de la seconde extrémité de l'interval :"))
	t = int(input("Entrer la valeur à chercher dans l'interval :"))
	if x <= t <= y:
		print(f"{t} est dans l'interval [{x},{y}]")
	else:
		print(f"{t} n'est pas dans l'interval [{x},{y}]")
"""
	la fonction searchint permet de chercher une valeur dans un interval
	dont les extrémités sont données par l'utilisateur. Cool non 😊😊😊
"""

def SumImp():
	n = int(input("Entrer l'entier n :"))
	i = 0
	s = 0
	while i != n:
		for j in range(2*n):
			if j%2 != 0:
				s = s + j**2
				i+= 1 # incrémentation de i après chaque somme

	# affichage du résultat
	print(f"la somme des {n} nombres impaire est :",s)

"""
	la fonction SumImp permet de calculer la somme des n nombre(s)
	impaire(s).
	NB: le n est entrer par l'utilisateur. Cool non 😊😊😊
""" 

def listPairs():
	x = input().split()
	nombres = list(map(int, x))
	nombres_pairs = [i for i in nombres if i%2 == 0]
	print("les nombres pairs :")
	print(nombres_pairs)
"""
	la fonction permet à un utilisateur d'entrer une liste 
	d'entier et reçois une entiers uniquement pairs. Cool non 😊😊😊
"""

def TriFichier():
	from pathlib import Path
	dirs = {
		"mp3": "Musique",
		"mav": "Musique",
		"flac": "Musique",
		"bmp" : "images",
		"png" : "images",
		"jpg" : "images",
		"mp4" : "vidéos",
		"gif" : "vidéos",
		"txt" : "Documents",
		"pptx" : "Documents",
		"csv" : "Documents",
		"xls" : "Documents",
		"odp" : "Documents",
		"pages": "Documents",
		"pdf"  : "fichier_pdf"
	}

	chemin = input("Entrer votre chemin de dossier")
	p = Path.home()/chemin
	files_list = [i for i in p.iterdir() if i.is_file()]
	for j in files_list:
		output_dir = p/dirs.get(j.suffix, "Autre")
		output_dir.mkdir(exist_ok = True)
		j.rename(output_dir/j.name)

"""
	la fonction TriFichier permet de trier les fichier dans un dossier
	selon les extensions. Cool non 😊😊😊
"""

def SumMoy():
	s,m= 0,0
	n = int(input("Entrer le nombre d'entier dont vous souhaitez calculer la somme et la moyenne :"))
	for i in range(n):
		x = int(input(f"nombre [{i + 1}] :"))
		s = s + x
	m = s/n
	print(f"la somme des nombre est",format(s))
	print(f"la moyenne est ",format(m,".2f"))    
    
"""
	la fonction SumMoy permet de calculer la somme et la moyenne. Cool non 😊😊😊
"""



        