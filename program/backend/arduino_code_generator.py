'''
Generate Final Arduino Code Verify and Upload
'''

# import required Library
from backend.setup_function_generator import setup_and_header_generator
from backend.value_listener_variable_generator import value_listener_variable_generator
from backend.condition_generator import conditional_digital_output_codegenerator
from backend import command
import pandas as pd


def generate_and_upload(items_dict, condition_dict, board, port, name="example"):
    # generate setup function and header required
    initial_header, initial_setup, initial_function, usable_function = setup_and_header_generator(items_dict)
    # initial_header : import required library and special starting variable declaration on file header
    # initial_setup  : code in setup function of arduino code
    # initial_function : create function for each item in items_dict
    # usable_function : list of usable_function
    
    # declare value listening variable ( listen value from the function )
    variable_declaration, value_listener = value_listener_variable_generator(items_dict)
        # variable_declaration : code to declare used variable
        # value_listener : connect value_listener with value source ( function )


        # -------------------------------------------create seperate file --------------------------------------------
    condition_code = """
void loop(){
    """
    condition_code += value_listener
    print(condition_dict)
    condition_code += conditional_digital_output_codegenerator(pd.DataFrame.from_dict(condition_dict), items_dict)
    condition_code += """
}
    """
    # -----------------------------------------------------------------------------------------------------------
    
    # final Arduino Code starting empty string
    text = """
    """
    
    # adding code header to final Arduino code
    text += initial_header

        # declare required variable data type and name
    text += variable_declaration

        # adding void setup(){} to arduino code
    text += initial_setup

        # adding require function for each item to the code
    text += initial_function

        # adding void loop(){}
    text += condition_code
    
        # declare used board and filename
    arduino_code = command.Sketch(board, name)
    
    # create sketch -> compile -> upload 
    arduino_code.create_sketch()
    arduino_code.write_sketch(text)
    arduino_code.verify_sketch()
    arduino_code.upload_sketch()
