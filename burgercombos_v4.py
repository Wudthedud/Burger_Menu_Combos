""" burgercombos_V3
adds easygui
"""
import easygui as eg

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


def add():
    """add new combo"""
    name = eg.enterbox("Enter the new combo name",  "Add new Combo").strip().lower()
    items = eg.multchoicebox("Pick items to include in combo", "Add new Combo",
                             ['Beef burger', 'Fries', 'Large fries', 'Fizzy drink',
                              'Cheeseburger', 'Smoothie'])
    confirm = eg.ynbox(f'Are these details correct: \n Name: {name.capitalize()}\n'
                       f'Items: {", ".join(map(str, items)).capitalize()}', 'Add new Combo')
    if confirm == 'yes':
        combos[name] = items
        eg.msgbox(f'{name} combo added!')
    else:
        add()

def remove():
    """remove combo"""
    while True:
        name = eg.enterbox("Enter combo to delete",  "Delete Combo").strip().lower()
        if name in combos:
            if eg.ynbox(f'Are you sure you want to delete {name.capitalize()}?', 'Delete Combo'):
                del combos[name]
                eg.msgbox(f'{name} combo deleted!')
                break
            else:
                eg.msgbox(f'{name} deletion cancelled!')
                break
        else:
            print('Please enter a valid combo')

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
        if eg.ynbox('Would you like to edit this combo?', 'Edit Combo'):
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
            pass
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
