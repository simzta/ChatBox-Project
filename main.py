
def greet_user():
    
    print("Welcome to the Burgur Place!")
    name = input("Input your name user: ")
    age = input(f'Hello {name}, enter your age: ')
    conversation_lobby()



interactive_list = ['1. See menu ','2. Order', '3. Exit']

interactive_menu = ['1. Burger','2. Fries','3. Soda']

def conversation_lobby():
    while True:
        print("\n".join(interactive_list))
        list_choice = input("How may I help you: ")
        print(list(list_choice))



def list(list_choice):

    if list_choice == "1":
        return "\n".join(interactive_menu)
    
    if list_choice == "2":
        print("\n".join(interactive_menu))
        menu_choice = input("What would you like to order: ")
        print("Ok, you ordered.") 
     
    if list_choice == "3":
        print("OK! Thank you for visiting Burgur Place.")
        SystemExit


greet_user()
