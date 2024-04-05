""" burger_combos_V1
Initial price dictionary and combos"""

#menu
menu_items = {
    'beef burger' : 5.69,
    'fries' : 1.00,
    'large fries'  :2.00,
    'fizzy drink' : 1.00,
    'cheeseburger' : 6.69,
    'smoothie' : 2.00
}

#current combos
combos = {
    'value' : ['beef burger', 'fries', 'fizzy drink'],
    'cheezy' : ['cheeseburger', 'fries', 'fizzy drink'],
    'super' : ['cheeseburger', 'large fries', 'smoothie']
}

#lists combos nad total
for combo, items in combos.items():
    total = 0
    print(f"-- {combo.capitalize()} Combo --")
    for item in items:
        print(f"{item.capitalize()} : ${menu_items[item]}")
        total += menu_items[item]
    print(f"Total = ${total:.2f}")
    