import json
import numpy as np


class table_0:

    def __init__(self):
        self.table = {'items': [], 'amount': []}

    def __add_data__(self, added_data):
        item, quantity = added_data
        if item in self.table['items']:
            item_index = self.table['items'].index(item)
            self.table['amount'][item_index] += quantity
        else:
            self.table['items'].append(item)
            self.table['amount'].append(quantity)


class FirstTable:

    def __init__(self):
        self.table = {'items': [], 'amount': [], 'used_digital_pins': [], 'used_analog_pins': []}

    def add_data(self, added_data):
        item, quantity = added_data
        if item in self.table['items']:
            item_index = self.table['items'].index(item)
            self.table['amount'][item_index] += quantity
            item_json_filename = f'resources/items/{item}.json'
            with open(item_json_filename) as json_file:
                item_dict = json.load(json_file)
            if item_dict["PIN"]["Digital"] != 0:
                self.table['used_digital_pins'][item_index] += item_dict["PIN"]["Digital"] * quantity
                self.table['used_analog_pins'][item_index] += 0
            if item_dict["PIN"]["Analog"] != 0:
                self.table['used_analog_pins'][item_index] += item_dict["PIN"]["Analog"] * quantity
                self.table['used_digital_pins'][item_index] += 0

        else:
            item_json_filename = f'resources/items/{item}.json'
            with open(item_json_filename) as json_file:
                item_dict = json.load(json_file)
            self.table['items'].append(item)
            self.table['amount'].append(quantity)
            self.table['used_digital_pins'].append(item_dict["PIN"]["Digital"] * quantity)
            self.table['used_analog_pins'].append(item_dict["PIN"]["Analog"] * quantity)


l = []
f = FirstTable()
f.add_data(('DHT11', 2))
f.add_data(("DHT12", 2))
L = []
for item in f.table:
    l.append(f.table[item])

a = np.transpose(np.array(l))
print(a)
