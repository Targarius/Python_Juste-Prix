import random, time

prix = 0
estimation = 0
inGame = True

def setPrix():
    global prix
    prix = random.randint(1, 10000)

def getEstimation():
    global estimation
    estimation = int(input("Quel est le prix: "))

def LancerJeu():
    print("Bienvenue au JUSTE PRIX")
    time.sleep(1)
    x = input("Voulez vous lancer une partie (y/n)")
    while inGame:
        if x == "y":
            boucleJeu()
            x = input("Voulez vous rejouer? (y/n)")
        elif x == "n":
            print("(° _ °)/")
            break
        else:
            print("On ne vous comprends pas!")
            x = input("Voulez vous lancer une partie (y/n)")

def boucleJeu():
    setPrix()
    while prix != estimation:
        getEstimation()
        if estimation == prix:
            print("Bien Joué il s'agissait bien de " + str(prix) )
            break
        elif estimation < prix:
            print("C'est plus cher")
        elif estimation > prix:
            print("C'est moins cher")
        else:
            print("Le prix n'est pas valide")


LancerJeu()

