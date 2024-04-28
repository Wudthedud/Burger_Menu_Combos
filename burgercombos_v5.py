""" burgercombos_V5
adds error correction
"""
import sys
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
        while True:
            name = eg.enterbox("Enter the new combo name",  "Add new Combo").strip().lower()
            if name != "":
                break
            eg.msgbox("Please input a name", "Edit combo")
        if name in combos:
            if eg.ynbox(f"{name.capitalize()} is already a combo, would you like to edit it?"):
                edit(name)
            else:
                main()
        else:
            while True:
                try:
                    items = eg.multchoicebox("Pick items to include in combo", "Add new Combo",
                                            list(menu_items.keys()))
                    confirm = eg.ynbox(f'Are these details correct: \n\nName: {name.capitalize()}\n'
                                       f'Items: {", ".join(map(str, items)).capitalize()}',
                                       'Add new Combo')
                    break
                except TypeError:
                    eg.msgbox("Please select at least one item")
            if confirm:
                combos[name] = items
                eg.msgbox(f' Combo {name.capitalize()} added!')
                main()
            else:
                add()
    except AttributeError:
        main()


def remove():
    """remove combo"""
    try:
        name = eg.choicebox("Enter combo to delete", "Delete combo", list(combos.keys()))
        if eg.ynbox(f'Are you sure you want to delete {name.capitalize()}?', 'Delete Combo'):
            del combos[name]
            eg.msgbox(f'{name.capitalize()} combo deleted!')
        else:
            eg.msgbox(f'{name.capitalize()} deletion cancelled!')
    except AttributeError:
        main()


def menu():
    """lists combos and total"""
    for combo, items in combos.items():
        total = 0
        print(f"-- {combo.capitalize()} Combo --")
        for item in items:
            print(f"{item.capitalize()} : ${menu_items[item]}")
            total += menu_items[item]
        print(f"Total = ${total:.2f}")
    msg = ""
    for combo, items in combos.items():
        total = 0
        msg += f"-- {combo.capitalize()} combo --\n"
        for item in items:
            msg += (f"{item.capitalize()} : ${menu_items[item]}\n")
            total += menu_items[item]
        msg += f"Total = ${total:.2f}\n\n"
    msg += "-" * 20
    msg += "\n\n\nMenu also printed to python console"
    eg.msgbox(msg, 'Menu')


def edit(name):
    """search for combo and edit"""
    try:
        total = 0
        msg = f"--{name.capitalize()} combo--\n"
        for item in combos[name]:
            msg += (f"{item.capitalize()} : ${menu_items[item]}\n")
            total += menu_items[item]
        msg += f"Total = ${total:.2f}\n\n"
        msg += "-" * 20

        choice = eg.buttonbox(f"{msg}\nWhat would you like to do?\n", "Edit a combo",
                              ("Change combo name", "Change combo items", "Go back"))
        if choice == "Change combo name":
            while True:
                new_name = eg.enterbox("What would you like the new name to be: ",
                                       "Change combo name")
                if new_name != "":
                    break
                eg.msgbox("Please input a name", "Edit combo")
            msg = "Is this correct:\n\n"
            msg += f"--{new_name.capitalize()} combo--\n"
            for item in combos[name]:
                msg += (f"{item.capitalize()} : ${menu_items[item]}\n")
                total += menu_items[item]
            msg += f"Total = ${total:.2f}\n\n"
            msg += "-" * 20
            if eg.ynbox(msg, "Edit combo"):
                combos[new_name] = combos[name]
                del combos[name]
                eg.msgbox("Edit complete", "Edit a combo")
            else:
                eg.msgbox("Edit cancelled", "Edit a combo")
                edit(name)
        elif choice == "Change combo items":
            changed_item = eg.choicebox("Which item would you like to change",
                                        "Change combo items", (combos[name]))
            if changed_item is None:
                edit(name)
            new_item = eg.choicebox(f"Which item would you like to swap out {changed_item} for?",
                                    "Change combo items", (list(menu_items.keys())))
            combos[name].append(new_item)
            combos[name].remove(changed_item)
            msg = "Is this correct:\n\n"
            msg += f"--{name.capitalize()} combo--\n"
            for item in combos[name]:
                msg += (f"{item.capitalize()} : ${menu_items[item]}\n")
                total += menu_items[item]
            msg += f"Total = ${total:.2f}\n\n"
            msg += "-" * 20
            if eg.ynbox(msg, "Edit combo"):
                eg.msgbox("Edit complete", "Edit a combo")
            else:
                eg.msgbox("Edit cancelled", "Edit a combo")
                combos[name].append(changed_item)
                combos[name].remove(new_item)
        elif choice == "Go back":
            main()
    except AttributeError:
        main()

def main():
    """main code"""
    while True:
        choice = eg.buttonbox("What would you like to do?", 'Welcome',
                            ('Add new combo', 'Remove a combo', 'Display Menu',
                             'Find/Edit a combo', 'Exit'))
        if choice == 'Add new combo':
            add()
        elif choice == 'Remove a combo':
            remove()
        elif choice == 'Display Menu':
            menu()
        elif choice == 'Find/Edit a combo':
            name = eg.choicebox("Which combo would you like to find?",
                                "Find/Edit a Combo", (list(combos.keys())))
            edit(name)
        elif choice == "Exit":
            sys.exit()

main()
