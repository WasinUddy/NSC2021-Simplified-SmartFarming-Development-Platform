import json

def setup_and_header_generator(items_dict):
    used_items = []
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

    for item_ID in list(items_dict.keys()):
        
        # get item name 
        item_name = item_ID.split('-', 1)[0]

        # check weather the item has been used or not
        used_item_boolean = item_name in used_items
        if used_item_boolean is False:
            used_items.append(item_name)

        digital_pins = items_dict[item_ID]["Digital_pins"]
        analog_pins = items_dict[item_ID]["Analog_pins"]


        # open item json as python dictionary 
        with open(f"resources/items/{item_name}.json") as json_file:
            item_info_dictionary = json.load(json_file)

        

        if item_info_dictionary["function_list"] is not None:
            usable_function[item_ID] = item_info_dictionary["function_list"]

        # item has not been used

        # static code for each item
        if used_item_boolean is False:
            if item_info_dictionary["header1"] is not None:
                for header1 in item_info_dictionary["header1"]:
                    initial_header_1 += f"""

// Starting Header 1 of {item_name}
{header1}
// Ending Header 1 of {item_name}

"""
        
            if item_info_dictionary["code_function"] is not None:
                for code_function in item_info_dictionary["code_function"]:
                    initial_function += f"""

// Starting Functino of {item_name}
{code_function}
//Ending Function of {item_name}

"""
        if item_info_dictionary["header2"] is not None:
            for header2 in item_info_dictionary["header2"]:
                
                # Decorating header that associate with custom pin
                # replace CUSTOM ID 
                header2 = header2.replace(item_info_dictionary["custom id key"], item_ID)

                # Dual pin system
                if item_info_dictionary["custom pin key"][0] is not None:
                    if digital_pins != []:
                        header2 = header2.replace(item_info_dictionary["custom pin key"][0], str(digital_pins[0]))
                        if item_info_dictionary["custom pin key"][1] is not None:
                            header2 = header2.replace(item_info_dictionary["custom pin key"][1], str(digital_pins[1]))

                    if analog_pins != []:
                        header2 = header2.replace(item_info_dictionary["custom pin key"][0], str(analog_pins[0]))
                        if item_info_dictionary["custom pin key"][1] is not None:
                            header2 = header2.replace(item_info_dictionary["custom pin key"][1], str(analog_pins[1]))
                
                # Single pin system
                if item_info_dictionary["custom pin key"][1] is not None:
                    if digital_pins != []:
                        header2 = header2.replace(item_info_dictionary["custom pin key"][1], str(digital_pins[0]))
                    if analog_pins != []:
                        header2 = header2.replace(item_info_dictionary["custom pin key"][1], str(analog_pins[0]))

                initial_header_2 += f"""
//Starting header 2 of {item_ID}
{header2}
//Ending header 2 of {item_ID}
"""
                
                if item_info_dictionary["no PINMODE"] is False:

                             # PinMode Setting in void setup(){}
                    if item_info_dictionary["PINMODE"]["INPUT"] != 0:
                        initial_setup += f"""
// pinMode of {item_ID}
pinMode({digital_pins[0]}, INPUT);
"""
            
                    if item_info_dictionary["PINMODE"]["OUTPUT"] != 0:
                        initial_setup += f"""
// pinMode of {item_ID}
pinMode({digital_pins[0]}, OUTPUT);
"""   
                
                if item_info_dictionary["code_in_setup"] is not None:
                    for code_in_setup in item_info_dictionary["code_in_setup"]:
                        code_in_setup = code_in_setup.replace(item_info_dictionary["custom id key"], item_ID)
                        if digital_pins != []:
                            code_in_setup = code_in_setup.replace(item_info_dictionary["custom pin key"][0], str(digital_pins[0]))
                            if item_info_dictionary["custom pin key"][1] is not None:
                                code_in_setup = code_in_setup.replace(item_info_dictionary["custom pin key"][1], str(digital_pins[1]))

                        if analog_pins != []:
                            code_in_setup = code_in_setup.replace(item_info_dictionary["custom pin key"][0], str(analog_pins[0]))
                            if item_info_dictionary["custom pin key"][1] is not None:
                                code_in_setup = code_in_setup.replace(item_info_dictionary["custom pin key"][1], str(analog_pins[1]))
                
                         # Single pin system
                         if item_info_dictionary["custom pin key"][1] is not None:
                            if digital_pins != []:
                                code_in_setup = code_in_setup.replace(item_info_dictionary["custom pin key"][1], str(digital_pins[0]))
                            if analog_pins != []:
                                code_in_setup = code_in_setup.replace(item_info_dictionary["custom pin key"][1], str(analog_pins[0]))
                        

                        initial_setup += f"""
{code_in_setup}
"""

    initial_setup += """
}
"""
    
    header = f"""
{initial_header_1}

{initial_header_2}
"""

        return header, initial_setup, initial_function, usable_function


        