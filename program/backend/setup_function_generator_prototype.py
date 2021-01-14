# import required Library
import json 

def setup_and_header_generator(items_dict):
    used_item = []
    usable_function = {}

# -----------------------Create starting String-----------------------
    initial_header = """

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

        # adding static code for item into the code
        if used_item is not True:
            # add header 1 static header
            if item_dictionary["header1"] is not None:
                for header_1 in item_dictionary["header1"]:
                    initial_header += header_1
            
            # add code_function static function
            if item_dictionary["code_function"] is not None:
                for code_function in item_dictionary["code_function"]:
                    initial_function += code_function


        # PinMode Setting in void setup(){}
        if item_dictionary["PINMODE"]["INPUT"] != 0:
            for input_pins in items_dict[f"{item_name}_{item_ID}"]["Digital_pins"]:
                initial_setup += f"""
pinMode({input_pins}, INPUT);
"""
        if item_dictionary["PINMODE"]["OUTPUT"] != 0:
            for output_pins in item_dict[f"{item_name}_{item_ID}"]["Digital_pins"]:
                initial_setup += f"""
pinMode({output_pins}, OUTPUT);
"""



                

        
        
