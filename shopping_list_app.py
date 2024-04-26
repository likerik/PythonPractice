import sys #Libreria sys para salir del programa al seleccionar opcion 7

#Crear el menu principal
def mainMenu():
    while True:
        print()
        print('''### SHOPPING LIST ###
            
        Select a number for the action that you would like to do:

        1. View shopping list
        2. Add item to shopping list
        3. Remove item from shopping list
        4. Check if item is on shopping list
        5. How many items on shopping list
        6. Clear shopping list
        7. Exit
        ''')

        selection = input("Make your selection: ") #Solicitar al usuario la eleccion de su preferencia

        #Determina la accion a realizar basado en la seleccion del usuario
        if selection == "1":
            displayList()
        elif selection == "2":
            addItem()
        elif selection == "3":
            removeItem()
        elif selection == "4":
            checkItem()
        elif selection == "5":
            listLenght()
        elif selection == "6":
            clearList()
        elif selection == "7":
            print("Exiting, BYE!")
            print()
            sys.exit()
        else:
            print("You did not make a valid selection.")

shopping_list = ["apples", "bananas", "carrots", "potatoes"] #Agregando algunos items a la lista de compra

#Muestra todos los items a la lista de compra/Define la funcion para la opcion 1 del menu
def displayList():
    print()
    print("--- SHOPPING LIST ---")
    for i in shopping_list:
        print("* " + i)

#Agrega un item a la lista de compras/Define la funcion de la opcion 2 del menu
def addItem():
    print()
    print("--- ADDING ITEM ---")
    item = input("Enter the item you wish to add to the shopping list: ")
    shopping_list.append(item)
    print(item + " has been added to the shopping list.")

#Elimina un item de la lista de compras/Define la funcion para la opcion 3 del menu
def removeItem():
    print()
    print("--- REMOVING ITEM ---")
    item = input("Enter the item you wish to remove from the shopping list: ")
    shopping_list.remove(item)
    print(item + " has been removed from the shopping list.")

#Valida si algun item se encuentra dentro de la lista de compras/Define la funcion para la opcion 4 del manu
def checkItem():
    print()
    print("--- CHECKING ITEM ---")
    item = input("What item would you like to check on the shopping list: ")
    if item in shopping_list:
        print("Yes " + item + " is on the shopping list.")
    else:
        print("No " + item + " is not in the shopping list.")

#Muestra el numero de items que se encuentran en la lista
def listLenght():
    print("There are ", len(shopping_list), " items on the shopping list")
    print()

#Borra todos los items que se encuentran en la lista
def clearList():
    shopping_list.clear()
    print("The shopping list is now empty.")
    print()

#Ejecuta la funcion del menu principal en la que se ejecuta la app
mainMenu()