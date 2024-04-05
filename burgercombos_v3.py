""" burger_combosV2
adds user actions such as adding or deleting combos, search and edit
"""

#intial combos
combos = {
    'value' : ['beef burger', 'fries', 'fizzy drink'],
    'cheezy' : ['cheeseburger', 'fries', 'fizzy drink'],
    'super' : ['cheeseburger', 'large fries', 'smoothie']
}

#menu prices
menu_items = {
    'beef burger' : 5.69,
    'fries' : 1.00,
    'large fries'  :2.00,
    'fizzy drink' : 1.00,
    'cheeseburger' : 6.69,
    'smoothie' : 2.00
}


def yn_check(question):
    """yes/no check"""
    choice = input(question).strip().lower
    while True:
        if choice == "y" or "yes":
            return True
        elif choice == "n" or "no":
            return False
        else:
            print("Please enter [Y] or [N]")


def add():
    """add new combo"""
    name = input("Enter the new combo name: \n").lower
    items = []
    while True:
        item = input("\n\nEnter the an item for the combo, [x] to exit \n").lower().strip()
        if item == "x":
            combos[name] = items
            print(f'{name} added with {combos[name]}')
            break
        if item in menu_items:
            items.append(item)
            print("Items added to combo")
        else:  
            print("The item is not one of the menu items")
    

def remove():
    """remove combo"""
    while True:
        name = input("Enter a combo to delete: \n").strip().lower()
        if name in combos:
            del combos[name.lower().strip()]
            print(f'{name.capitalize()} combo deleted')
            break
        else:
            print('Please enter a valid combo')
    print(combos)

def menu():
    """lists combos and total"""
    for combo, items in combos.items():
        total = 0
        print(f"-- {combo.capitalize()} Combo --")
        for item in items:
            print(f"{item.capitalize()} : ${menu_items[item]}")
            total += menu_items[item]
        print(f"Total = ${total:.2f}")


def edit():
    """search for combo and edit"""
    name = input('Enter combo to search for: ').lower().strip()
    if name in combos:
        print(f"-- {name.capitalize()} Combo --")
        for item in combos[name]:
            print(f"{item.capitalize()} : ${menu_items[item]:.2f}")
        edit = input('Are all details correct? [Y/N] \n').lower()
        if edit in ('no', 'n'):
            for i in range(3):
                print(f'[{i + 1}] {combos[name][i].capitalize()}')
            print(f'[4] Change combo name ("{name.capitalize()}")')
            print('[5] Exit')
            choice = int(input('Which item would you like to change: \n'))     
            if choice == 5:
                pass
            elif choice == 4:
                new_name = input('What would you like the combo to be called: \n').strip().lower()
                combos[new_name] = combos[name]
                del combos[name]
            elif choice >= 1 and choice <= 3:
                print(f'You are editing item [{choice}]: {combos[name][choice - 1].capitalize()}')
                new_item = input('What would you like the new item to be: \n')
                combos[name].insert(choice - 1, new_item)
                combos[name].pop(choice)
        else: 
            return False
    else:
        print("Sorry, that combo does not exist.")



def main():
    """main code"""
    choice = int(input('Would you like to [1] Add a new combo, [2] Remove a combo, '
                       '[3] Edit a combo, [4] List the menu, or [5] exit? \n'))
    if choice == 1:
        add()
    elif choice == 2:
        remove()
    elif choice == 3:
        edit()
    elif choice == 4:
        menu()
    else:
        exit()

main()
