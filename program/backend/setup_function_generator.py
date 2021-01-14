# import required library
import json


def setup_and_header_generator(items_dict):

    used_item = []
    usable_function = {}

    initial_header = """
"""
    initial_setup = """
void setup()
{
"""
    initial_function = """

    """

    for item_name_and_ID in list(items_dict.keys()):

        item_name = item_name_and_ID.split('_', 1)[0]
        item_ID = item_name_and_ID.split('_', 1)[1]

        with open(f"resources/items/{item_name}.json") as json_file:
            item_dictionary = json.load(json_file)

        if item_name not in used_item:
            used_item.append(item_name)
            try:
                if item_dictionary["header1"] is not None:
                    for header1 in item_dictionary["header1"]:
                        initial_header += header1
            except KeyError:
                pass

            try:
                if item_dictionary["code_function"] is not None:
                    for function in item_dictionary["code_function"]:
                        initial_function += function
            except KeyError:
                pass



        if item_dictionary["PINMODE"]["INPUT"] > 0:
            input_pins = items_dict[f"{item_name}_{item_ID}"]["Digital_pins"][0]

            try:
                if item_dictionary["no PINMODE"] is not True:
                    initial_setup += '\n'


            except:
                pass

            try:
                for setup_code in item_dictionary["code_in_setup"]:
                    initial_setup += '\n'
                    initial_setup += setup_code.replace(
                        item_dictionary["custom id key"], f"{item_name}_{item_ID}"
                    ).replace(item_dictionary["custom pin key"][0],
                              str(items_dict[f"{item_name}_{item_ID}"]["Digital_pins"][0]))
            except KeyError:
                pass




        if item_dictionary["PINMODE"]["OUTPUT"] > 0:
            output_pins = items_dict[f"{item_name}_{item_ID}"]["Digital_pins"][0]
            try:
                if item_dictionary["no PINMODE"] is not True:
                    initial_setup += '\n'
                    initial_setup += f"""
pinMode({output_pins}, OUTPUT);
"""

            except:
                pass
                try:
                    for setup_code in item_dictionary["code_in_setup"]:
                        initial_setup += '\n'
                        initial_setup += setup_code.replace(
                            item_dictionary["custom id key"], f"{item_name}_{item_ID}"
                        ).replace(item_dictionary["custom pin key"][1],
                                  str(items_dict[f"{item_name}_{item_ID}"]["Digital_pins"][0]))
                except KeyError:
                    pass

        try:
            for header2 in item_dictionary["header2"]:

                if "input" in header2:
                    header2 = header2.replace(item_dictionary["custom pin key"][0], str(input_pins))
                if "output" in header2:
                    header2 = header2.replace(item_dictionary["custom pin key"][1], str(output_pins))

                header2 = header2.replace(item_dictionary["custom id key"], f"{item_name}_{item_ID}")
                initial_header += '\n'
                initial_header += header2
        except KeyError:
            pass

        try:
            usable_function[f"{item_name}_{item_ID}"] = item_dictionary["function_list"]
        except KeyError:
            pass

    initial_setup += """
}
    """

    return initial_header, initial_setup, initial_function, usable_function

