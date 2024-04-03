""" burger_combos_V2
adds user actions such as adding or deleting combos
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

#add new combo
def add_combos():
    name = input("Enter the new combo name: \n")
    items = []
    while True:
        item = input("\n\nEnter the an item for the combo, [x] to exit \n").lower().strip()
        if item == "x":
            break
        if item in menu_items:
            items.append(item)
            print("Items added to combo")
        else:   
            print("The item is not one of the menu items")
    for item in items:
        if item not in menu_items:
            return True 
        else:
            pass
    combos[name] = items
    print(combos)

#remove combo
def remove():
    try:
        del combos[name.lower().strip()]
        return False
    except:
        print('Please enter a valid combo')
        return True
        
        
#lists combos and total
def menu():
    for combo, items in combos.items():
        total = 0
        print(f"-- {combo.capitalize()} Combo --")
        for item in items:
            print(f"{item.capitalize()} : ${menu_items[item]}")
            total += menu_items[item]
        print(f"Total = ${total:.2f}")

#search for combo and edit
def search():
    name = input('Enter combo to search for: ').lower().strip()
    if name in combos:
        print(f"-- {name.capitalize()} Combo --")
        for item in combos[name]:
                print(f"{item.capitalize()} : ${menu_items[item]:.2f}")
        edit = input('Are all details correct? [Y/N] \n').lower()
        if edit == 'no' or edit == 'n':
            for i in range(3):
                print(f'[{i + 1}] {combos[name][i].capitalize()}')
            print(f'[4] Change combo name ("{name.capitalize()}")')
            print(f'[5] Exit')
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
    choice = int(input('Would you like to [1] Add a new combo, [2] Remove a combo, or [3] Edit a combo? \n'))
    if choice == 1:
        add_combos()
    if choice == 2:
        remove()

add_combos()