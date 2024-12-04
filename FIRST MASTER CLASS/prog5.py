nb = 20
i = 0
nb1 = 0 

while True:
    nb1 = int(input("Devinez le chiffre : "))
    i += 1  

    if nb1 < nb:
        print("Non, le chiffre que vous avez entré est inférieur. Réessayez.")
    elif nb1 > nb:
        print("Non, le chiffre que vous avez entré est superieure. Réessayez.")
    else:
        print(f"Bravo, vous avez deviné le chiffre {nb} en {i} essais !")
        break 
