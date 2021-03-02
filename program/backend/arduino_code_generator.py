'''
Generate Final Arduino Code Verify and Upload
'''

# import required Library
from backend.setup_function_generator import setup_and_header_generator
from backend.value_listener_variable_generator import value_listener_variable_generator
from backend.condition_generator import conditional_digital_output_codegenerator
from backend.analog_output_codegenerator import analog_output_codegenerator
from backend import command
import pandas as pd


def generate_and_upload(items_dict, condition_dict, noncondition_dict, board, name="example"):
    # generate setup function and header required
    initial_header, initial_setup, initial_function, usable_function = setup_and_header_generator(items_dict)
    # initial_header : import required library and special starting variable declaration on file header
    # initial_setup  : code in setup function of arduino code
    # initial_function : create function for each item in items_dict
    # usable_function : list of usable_function
    if noncondition_dict is not None:
        noncondition_code = analog_output_codegenerator(noncondition_dict)
    else:
        noncondition_code = None
    # declare value listening variable ( listen value from the function )
    variable_declaration, value_listener = value_listener_variable_generator(items_dict)
        # variable_declaration : code to declare used variable
        # value_listener : connect value_listener with value source ( function )


        # -------------------------------------------create seperate file --------------------------------------------
    condition_code = f"""
{value_listener}

{conditional_digital_output_codegenerator(pd.DataFrame.from_dict(condition_dict), items_dict)}
"""
    if noncondition_code is None:
        loopcode = f"""
void loop() {'{'}
{condition_code}
{'}'}
""" 

    else:
        loopcode = f"""
void loop() {'{'}
{condition_code}

{noncondition_code}
{'}'}
"""
    # -----------------------------------------------------------------------------------------------------------
    
    # final Arduino Code starting empty string
    text = f"""
{initial_header}

{variable_declaration}

{initial_function}

{initial_setup}

{loopcode}
    """
    arduino_code = command.Sketch(board, name)
    
    # create sketch -> compile -> upload 
    arduino_code.create_sketch()
    arduino_code.write_sketch(text)
    arduino_code.verify_sketch()
    arduino_code.upload_sketch()

