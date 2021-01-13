#import library
import json

def input_output_seperator(items_list):

        # defined item seperator list
    INPUT = []
    Digital_OUTPUT = []
    Analog_OUTPUT = []
    
    # iterate through all id
    for item_id in items_list.keys():

                # load dictionary for each item
        with open(f"resources/items/{item_id.split('_', 1)[0]}.json") as json_file:
            item_dictionary = json.load(json_file)

                # Seperate INPUT OUTPUT
        if "Input" in item_dictionary["TYPE"]:
            all_data_type = item_dictionary["var type"].keys()
            for data_type in all_data_type:
                INPUT.append(f'{item_id}_{data_type}')

        if "Digital Output" == item_dictionary["TYPE"]:
            Digital_OUTPUT.append(item_id)

        if "Analog Output" == item_dictionary["TYPE"]:
            Analog_OUTPUT.append(item_id)

    return INPUT, Digital_OUTPUT, Analog_OUTPUT
