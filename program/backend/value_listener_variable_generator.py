# import required library
import json


def value_listener_variable_generator(item_dict):
    # get all keys from item dictionary items_id
    item_dict_keys = item_dict.keys()
		
		# create starting empty string for declaring value listener variable
    value_listener_variable_declaration = """

    """
		
		# create starting empty string for listening to value from the function
    value_listener_variable = """

"""
		
		# create empty list for storing all value listener variable
    all_value_listener_variable = []
    
    #iterate through all items_dict key ( item_id )
    for item in item_dict_keys:
    		# extract only the name from item_id
        name = item.split("_")[0]
				
				# loading item_json to dictionary
        with open(f"resources/items/{name}.json") as json_file:
            name_dict = json.load(json_file)

				# filtering out other option than Sensor Input away
        if "Sensor Input" != name_dict["TYPE"]: continue

				# get all function type that are usable for each item 
        all_function = name_dict["function_list"].keys()
        
        # iterate through all usable function
        for function in all_function:
        		
        		# declare variable with variable type
            value_listener_variable_declaration += f"""
{name_dict["var type"][function]} {item}_{function};
"""					
						# append variable name in to list all_value_listener_variable
            all_value_listener_variable.append(f"{item}_{function}")
            
            # listener to value used in void loop(){}
            
            value_listener_variable += f"""
{item}_{function} = {name_dict["function_list"][function].replace(name_dict["custom id key"], item)}
            """

    return value_listener_variable_declaration, value_listener_variable













