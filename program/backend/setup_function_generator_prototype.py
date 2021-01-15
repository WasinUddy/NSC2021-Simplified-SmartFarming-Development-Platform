# import required Library
import json 

def setup_and_header_generator(items_dict):
    used_item = []
    usable_function = {}

# -----------------------Create starting String-----------------------
    initial_header_1 = """

"""

    initial_header_2 = """

"""
    
    initial_setup = """
void setup()
{

"""
    initial_function = """

"""
# -------------------------------------------------------------------

    for item_name_and_ID in list(items_dict.keys()):

        

        # Get Item name and ID
        item_name = item_name_and_ID('_', 1)[0]
        item_ID = item_name_and_ID('_', 1)[1]
    
        # check weather the item has been used
        used_item = item_name in used_item
        if used_item is False:
            used_item.append(item_name)
        
        # open item json as python dictionary 
        with open(f"resources/items/{item_name}.json") as json_file:
            item_dictionary = json.load(json_file)

        usable_function[item_name_and_ID] = item_dictionary["function_list"]

        # adding static code for item into the code1
        if used_item is not True:
            # add header 1 static header
            if item_dictionary["header1"] is not None:
                for header_1 in item_dictionary["header1"]:
                    initial_header_1 += f"""
{header_1}
"""
            # add code_function static function
            if item_dictionary["code_function"] is not None:
                for code_function in item_dictionary["code_function"]:
                    initial_function += f"""
{code_function}
"""
        input_pins = items_dict[f"{item_name}_{item_ID}"]["Digital_pins"]
        output_pins = items_dict[f"{item_name}_{item_ID}"]["Digital_pins"]

        if item_dictionary["header2"] is not None:
            for header2 in item_dictionary["header2"]:
                header2 = header2.replace(item_dictionary["custom id key"], item_name_and_ID)
                # custom input pins
                if item_dictionary["custom pin key"][0] is not None:
                    header2 = header2.replace(item_dictionary["custom pin key"][0], input_pins[0])
                # custom output pins
                if item_dictionary["custom pin key"][1] is not None:
                    header2 = header2.replace(item_dictionary["custom pin key"][1], output_pins[0])

                initial_header_2 += f"""
{header2}
"""

        if item_dictionary["no PINMODE"] is not False:

            # PinMode Setting in void setup(){}
            if item_dictionary["PINMODE"]["INPUT"] != 0:
                
                for input_pin in input_pins:
                    initial_setup += f"""
pinMode({input_pin}, INPUT);
"""
            if item_dictionary["PINMODE"]["OUTPUT"] != 0:
                
                for output_pin in output_pins:
                    initial_setup += f"""
pinMode({output_pin}, OUTPUT);
"""
        # Extra stuff in void setup(){}
        for code_in_setup in item_dictionary["code_in_setup"]:
            code_in_setup = code_in_setup.replace(item_dictionary["custom id key"], item_name_and_ID)
            if item_dictionary["PINMODE"]["INPUT"] != 0:
                code_in_setup = code_in_setup.replace(item_dictionary["custom pin key"][0], input_pins[0])
            if item_dictionary["PINMODE"]["OUTPUT"] != 0:
                code_in_setup = code_in_setup.replace(item_dictionary["custom pin key"][1], output_pins[0])

            initial_setup += f"""
{code_in_setup}
"""
    
    header = f"""
{initial_header_1}

{initial_header_2}
"""
    return header, initial_setup, initial_function, usable_function



                

        
        
