nb1=int(input("donne moi un chiffre"))
nb2=int(input("donne moi un autre chiffre"))
print(f"Number 1: {nb1}")
print(f"Number 2: {nb2}")
choix=input("choisie entre les 3 operations + ,/, * ou -")
if choix=="+":
    s=nb1+nb2
    print(f"{nb1}+{nb2}={s}")
elif choix=="*" :
    m=nb1*nb2
    print(f"{nb1}*{nb2}={m}")
elif choix=="/" :
    d=nb1/nb2
    print(f"{nb1}/{nb2}={d}")
elif choix== "-":
    sub=nb1-nb2
    print(f"{nb1}-{nb2}={sub}")
else :
    print("nonnn dekhel hadja tesslh")
