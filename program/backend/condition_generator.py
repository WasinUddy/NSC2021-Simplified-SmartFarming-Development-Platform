''' 
create conditional output for digital output device (LED, Relay, etc)
'''
# import required Library
# input_output_seperator use to seperate input and output devce in items dictionary
from backend.input_output_seperator import input_output_seperator

def conditional_digital_output_codegenerator(input_dataframe, items_dict):

        # Get List of Digitat Output devices
    INPUTs, Digital_OUTPUTs, Analog_OUTPUTs= input_output_seperator(items_dict)
    
    # clearing unused variable
    del INPUTs, Analog_OUTPUTs
    
    # creating index for item_id -> used output digital pin
    pin_index = {}
    
    # iterate through every single digital output device one by one 
    for Digital_OUTPUT in Digital_OUTPUTs:

                # defined unique item id
                # item id -> {item_name}_{number}
        item_id = f'{Digital_OUTPUT.split("_")[0]}_{Digital_OUTPUT.split("_")[1]}'

                # added data to pin_index
        pin_index[item_id] = items_dict[item_id]['Digital_pins'][0]

        # create starting empty string condition code
    condition_code = """
"""

        # iterate through row of condition_dataframe
    for index, row in input_dataframe.iterrows():

            # create condition comment to identified starting of conditon
        condition_code += f"""
//Start of Condition : {index}
        """

        condition_code += f"""
if ({row["INPUT"]} {row["CONDITION"]} {row["VALUE"]})
"""
        condition_code += """{"""

        condition_code += f"""
digitalWrite({pin_index[row["OUTPUT"]]}, HIGH);
        """
        condition_code += """
}else{
"""

        condition_code += f"""
digitalWrite({pin_index[row["OUTPUT"]]}, LOW);
        """

        condition_code += """
}
"""

        condition_code += f"""
//End of Condition : {index}
"""

    return condition_code

