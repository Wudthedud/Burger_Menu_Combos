# pylint: skip-file
import easygui as eg
combos = {
    'value' : ['beef burger', 'fries', 'fizzy drink'],
    'cheezy' : ['cheeseburger', 'fries', 'fizzy drink'],
    'super' : ['cheeseburger', 'large fries', 'smoothie']
}


print(combos['value'])

def edit():
    """search for combo and edit"""
    name = eg.choicebox("Which combo would you like to edit?",
                        "Edit a Combo", (list(combos.keys())))
    if name in combos:
        choice = eg.buttonbox(f"You are editing the {name} combo\nWhat would you like to do?",
                              "Edit a combo", ("Change combo name", "Change combo items""Add menu items"))
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
        elif choice == "Add menu items":
            new_item = eg.enterbox("Enter the new menu item:", "Add menu items")
            price = eg.integerbox(f"Enter the price of {new_item}", {"Add menu items"})
            menu_items[new_item] = price
            eg.msgbox(f"{new_item} added, here are all the items available:\n {menu_items}", "Menu items")
    else:
        print("Sorry, that combo does not exist.")
