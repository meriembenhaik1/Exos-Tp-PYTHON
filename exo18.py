import sys

numbers = [1, 2, 3, 4, 5]
def Append():
    elm=int(input("1 Enter value:"))
    numbers.append(elm)
    print(f"Updated List: {numbers}")
    enregistrer_menu()


def insert():
    elm=int(input("2 Enter value:"))
    i = int(input("Enter index: ")) 
    numbers.insert(i, elm)
    print(f"Updated List: {numbers}")
    enregistrer_menu()

def pop():
    i = int(input("Enter index: ")) 
    numbers.pop(i)
    print(f"Updated List: {numbers}")
    enregistrer_menu()

def remove():
    elm = input("Enter value to remove: ")  # Demande à l'utilisateur d'entrer la valeur à supprimer
    if elm in numbers:  # Vérifie si l'élément existe dans la liste
        numbers.remove(elm)  # Supprime la première occurrence de l'élément
        print(f"Updated List: {numbers}")
        enregistrer_menu()
def quit():
    sys.exit()

def enregistrer_menu():
    # Enregistrer les options du menu dans un fichier texte
    with open("menu.txt", "a") as file:
        file.write("\nMenu:\n")
        file.write("1. Ajouter un élément à la fin de la liste\n")
        file.write("2. Insérer un élément à un index spécifique\n")
        file.write("3. Supprimer un élément à un index donné\n")
        file.write("4. Supprimer un élément par sa valeur\n")
        file.write("5. Quitter le programme\n")
        file.write(f"Liste actuelle : {numbers}\n")
        file.write("-" * 50 + "\n")

def menu():
    while True:
        print("\nMenu:")
        print("1. Ajouter un élément à la fin de la liste")
        print("2. Insérer un élément à un index spécifique")
        print("3. Supprimer un élément à un index donné")
        print("4. Supprimer un élément par sa valeur")
        print("5. Quitter le programme")
        choice = input("Choisissez une option (1/2/3/4/5) : ")
        if choice == '1':
            Append()
        elif choice == '2':
            insert()
        elif choice=='3':
            pop()
        elif choice=='4':
            remove()
        elif choice == '5':
            print("Merci d'avoir utilisé le programme. À bientôt!")
            break  # Quitte la boucle et donc le programme
        else:
            print("Option invalide. Essayez à nouveau.")
            enregistrer_menu()
menu()

def lire_menu():
    try:
        with open("menu.txt", "r") as file:  # Ouvrir le fichier en mode lecture
            content = file.read()  # Lire tout le contenu du fichier
            print(content)  # Afficher le contenu dans la console
    except FileNotFoundError:
        print("Le fichier 'menu.txt' n'existe pas.")

# Appeler la fonction pour lire le fichier
lire_menu()
