# import required Library
import json 



def pretty(d, indent=0):
   for key, value in d.items():
      print('\t' * indent + str(key))
      if isinstance(value, dict):
         pretty(value, indent+1)
      else:
         print('\t' * (indent+1) + str(value))


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

    for item_name_and_ID in list(items_dict.keys()):
        if items_dict[item_name_and_ID]["Analog_pins"] != []:
            continue
        

        # Get Item name and ID
        item_name = item_name_and_ID.split('_', 1)[0]
        
    
        # check weather the item has been used
        used_item_bool = item_name in used_items
        if used_item_bool is False:
            used_items.append(item_name)
        
        # open item json as python dictionary 
        with open(f"resources/items/{item_name}.json") as json_file:
            item_dictionary = json.load(json_file)

        
        if item_dictionary["function_list"] is not None:
            usable_function[item_name_and_ID] = item_dictionary["function_list"]

        # adding static code for item into the code1
        if used_item_bool is not True:
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
        digital_pins = items_dict[item_name_and_ID]["Digital_pins"]
        
        
        

        if item_dictionary["header2"] is not None:
            for header2 in item_dictionary["header2"]:
                header2 = header2.replace(item_dictionary["custom id key"], item_name_and_ID)

                # Dual Input and Output
                # custom input pins
                if item_dictionary["custom pin key"][0] is not None:
                    header2 = header2.replace(item_dictionary["custom pin key"][0], str(digital_pins[0]))
                    # custom output pins
                    if item_dictionary["custom pin key"][1] is not None:
                        header2 = header2.replace(item_dictionary["custom pin key"][1], str(digital_pins[1]))
                
                # Solo pin mode
                if item_dictionary["custom pin key"][1] is not None:
                        header2 = header2.replace(item_dictionary["custom pin key"][1], str(digital_pins[0]))


                initial_header_2 += f"""
{header2}
"""

        if item_dictionary["no PINMODE"] is False:

            # PinMode Setting in void setup(){}
            if item_dictionary["PINMODE"]["INPUT"] != 0:
                initial_setup += f"""
pinMode({digital_pins[0]}, INPUT);
"""
            
            if item_dictionary["PINMODE"]["OUTPUT"] != 0:
                initial_setup += f"""
pinMode({digital_pins[0]}, OUTPUT);
"""
        # Extra stuff in void setup(){}
        if item_dictionary["code_in_setup"] is not None:
            for code_in_setup in item_dictionary["code_in_setup"]:
                code_in_setup = code_in_setup.replace(item_dictionary["custom id key"], item_name_and_ID)

                # Dual Input and Output
                if item_dictionary["PINMODE"]["INPUT"] != 0:
                    code_in_setup = code_in_setup.replace(item_dictionary["custom pin key"][0], str(digital_pins[0]))
                    if item_dictionary["PINMODE"]["OUTPUT"] != 0:
                        code_in_setup = code_in_setup.replace(item_dictionary["custom pin key"][1], str(digital_pins[1]))

                # Solo pin
                if item_dictionary["PINMODE"]["OUTPUT"] != 0:
                        code_in_setup = code_in_setup.replace(item_dictionary["custom pin key"][1], str(digital_pins[0]))

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



                

        
        
