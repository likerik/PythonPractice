def viewlist(shopping_list):
    print(shopping_list)

def additem(shopping):
    



def main ():
    
    shopping_list = []
    
    while True:
        menu = """
        select a number for the action you would like to do.

        1. view shopping list
        2. add item to shopping list
        3. remove item from shopping list
        4. check if item is on shopping list
        5. how many items on shopping list
        6. clear shopping list
        7. exit
        """

        option = input(menu)

        if option == '1':
            viewlist(shopping_list)
        if option == '2':
            pass
        if option == '3':
            pass
        if option == '4':
            pass
        if option == '5':
            pass
        if option == '6':
            pass
        if option == '7':
            break
        

if __name__ == '__main__':
    main()
