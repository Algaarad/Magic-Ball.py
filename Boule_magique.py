# Boule magique on pose une question et renvoie une réponse déjà fait

import random

def boule_magique ():
    rep = random.randint(1,11)
    if rep == 2 :
        print("Ouais, je pense")
    elif rep == 3:
        print("Non, t'abuse frere")
    elif rep == 4:
        print("Pas con")
    elif rep == 5:
        print(" Mais comment ça mon reuf !?")
    elif rep == 6:
        print("Pfffff")
    elif rep == 7:
        print("Jamais de la vie")
    elif rep == 8:
        print("Sinon va dormir là")
    elif rep == 9:
        print("Mais ohhhhhhh")
    elif rep == 10:
        print("Allez asy")
    else:
        print("Sinon tu connais berserk ?")

boule_magique()




