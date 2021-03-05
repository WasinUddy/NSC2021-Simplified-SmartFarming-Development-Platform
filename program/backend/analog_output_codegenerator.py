'''
Generate Code for Analog Output device I2C interface only
'''

# import required library
import json
import pandas as pd


def analog_output_codegenerator(input_dataframe):

    # defined Empty Starting String
    noncondition_code = """
    
"""

    # loading table dictionary in to Pandas DataFrame
    input_dataframe_pd = pd.DataFrame.from_dict(input_dataframe)

    # Iterate through row of DataFrame
    for index, row in input_dataframe_pd.iterrows():
        OUTPUT_DEVICE = row["OUTPUT"].split("_")[0]

        # Loading used item dictionary from json file
        with open(f"resources/items/{OUTPUT_DEVICE}.json") as json_file:
            item_dictionary = json.load(json_file)
            # clearing unused variable
        del json_file

        # creating Starting Unmodified Function
        unmodified_function = item_dictionary["function_list"]
        print(unmodified_function)
        header_name = row["name"]
        header_name = (f"'{header_name}'").replace("'", '"')

        # modified unmodified function
        unmodified_function = unmodified_function.replace(item_dictionary["custom id key"], row["OUTPUT"])
        unmodified_function = unmodified_function.replace("header", header_name)
        unmodified_function = unmodified_function.replace("value", row["INPUT"])
        unmodified_function = unmodified_function.replace("row", row["row"])

        # modified function to code
        noncondition_code += unmodified_function
        noncondition_code += "\n"

    return noncondition_code























