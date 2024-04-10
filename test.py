# pylint: skip-file
import easygui as eg


name = 'value'
items = ['beef burger', 'fries', 'fizzy drink']
confirm = eg.ynbox(f"Are these details correct: \n Name: {name.capitalize()}\n Items: {", ".join(map(str, items)).capitalize()}", "Add new Combo")
print(confirm)