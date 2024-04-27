""" burgercombos_V4
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
    try:
        name = eg.enterbox("Enter the new combo name",  "Add new Combo").strip().lower()
        items = eg.multchoicebox("Pick items to include in combo", "Add new Combo",
                                ['beef burger', 'fries', 'large fries', 'fizzy drink',
                                'cheeseburger', 'smoothie'])
        confirm = eg.ynbox(f'Are these details correct: \n\nName: {name.capitalize()}\n'
                        f'Items: {", ".join(map(str, items)).capitalize()}', 'Add new Combo')
        if confirm:
            combos[name] = items
            eg.msgbox(f' Combo {name.capitalize()} added!')
            main()
        else:
            add()
    finally:
        main()


def remove():
    """remove combo"""
    while True:
        try:
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
                eg.msgbox("Please enter a valid combo", "Delete a combo")
        finally:
            main()


def menu():
    """lists combos and total"""
    msg = ""
    for combo, items in combos.items():
        total = 0
        msg += f"-- {combo.capitalize()} Combo --\n"
        for item in items:
            msg += (f"{item.capitalize()} : ${menu_items[item]}\n")
            total += menu_items[item]
        msg += f"Total = ${total:.2f}\n\n"
    eg.msgbox(msg, 'Menu')


def edit():
    """search for combo and edit"""
    name = eg.choicebox("Which combo would you like to edit?",
                        "Edit a Combo", (list(combos.keys())))
    if name in combos:
        choice = eg.buttonbox(f"You are editing the {name} combo\nWhat would you like to do?",
                              "Edit a combo", ("Change combo name", "Change combo items"))
        if choice == "Change combo name":
            new_name = eg.enterbox("What would you like the new name to be: ", "Change combo name")
            combos[new_name] = combos[name]
            del combos[name]
        elif choice == "Change combo items":
            changed_item = eg.choicebox("Which item would you like to change",
                                        "Change combo items", (combos['value']))
            new_item = eg.choicebox(f"Which item would you like to swap out {changed_item} for?",
                                    "Change combo items", (list(menu_items.keys())))
            combos[name].append(new_item)
            combos[name].remove(changed_item)
    else:
        print("Sorry, that combo does not exist.")


def main():
    """main code"""
    while True:
        choice = eg.buttonbox("What would you like to do?", 'Welcome',
                            ('Add new combo', 'Remove a combo', 'Display Menu',
                             'Edit a combo', 'Exit'))
        if choice == 'Add new combo':
            add()
        elif choice == 'Remove a combo':
            remove()
        elif choice == 'Display Menu':
            menu()
        elif choice == 'Edit a combo':
            edit()
        else:
            exit()

main()