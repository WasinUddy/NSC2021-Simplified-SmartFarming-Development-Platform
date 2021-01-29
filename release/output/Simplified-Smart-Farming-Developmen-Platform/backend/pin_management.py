import json


def pin_management(board, item_sets):
        # defined items dictionary
    items_dict = {}

        # loading Board specification from json file
    board_json_path = f"resources/Boards/{board}.json"
    with open(board_json_path) as json_file:
        board_dictionary = json.load(json_file)
        del json_file

        # loading different type of pin in to each variable
    communication_pins = board_dictionary["Communication_pins"]
    digital_pins = set(board_dictionary["Digital_pins"])
    analog_pins = set(board_dictionary["Analog_pins"])
    
    # special pin Serial and SPI
    serial_used = 0
    SPI_used = 0

        # iterate through item_sets
    for item_set in item_sets:

            # unpack item_set
        item, quantity = item_set[0], int(item_set[1])

                # load json of the item
        item_json_path = f"resources/items/{item}.json"
        with open(item_json_path) as json_file:
            item_info_dictionary = json.load(json_file)
        
        # adding up through quantity of item
        for i in range(quantity):

                # default individual element of items_dict unmodified
            item_items_dict = {
                "I2C": False,
                "SPI": None,
                "Serial": None,
                "Digital_pins": [],
                "Analog_pins": []
            }
            
            # Using I2C pin
            if item_info_dictionary["PIN"]["I2C"] is True:
                    # removing I2C pin from usable digital and analog pins
                digital_pins -= set(communication_pins["SDA"])
                digital_pins -= set(communication_pins["SCL"])

                analog_pins -= set(communication_pins["SDA"])
                analog_pins -= set(communication_pins["SCL"])

                                # Changing Boolean of I2C to True
                item_items_dict["I2C"] = True

                        # Using SPI pin
            if item_info_dictionary["PIN"]["SPI"] is True:
                SPI_used += 1
                assert SPI_used > board_dictionary["SPI"], "Nathan MAX SPI ERROR"
                ss = f"SS{SPI_used - 1}"
                
                # removing SPI pin from usable digital and analog pins
                digital_pins -= set(communication_pins[ss])
                digital_pins -= set(communication_pins["MOSI"])
                digital_pins -= set(communication_pins["MISO"])
                digital_pins -= set(communication_pins["SCK"])

                analog_pins -= set(communication_pins[ss])
                analog_pins -= set(communication_pins["MISO"])
                analog_pins -= set(communication_pins["SCK"])
                
                # defined SS pin
                item_items_dict["SPI"] = ss

                        # Using Serial pins
            if item_info_dictionary["PIN"]["Serial"] is True:
                serial_used += 1
                assert serial_used > board_dictionary["Serial"], "Nathan MAX SERIAL ERROR"
                
                # defined Serial port number
                TX_name = f"TX{serial_used}"
                RX_name = f"RX{serial_used}"
                
                # removing Seria pin from usable digital and analog pins
                digital_pins -= set(communication_pins[TX_name])
                digital_pins -= set(communication_pins[RX_name])

                analog_pins -= set(communication_pins[TX_name])
                analog_pins -= set(communication_pins[RX_name])
                
                # defined Serial pin
                item_items_dict["Serial"] = f"{TX_name}, {RX_name}"

                        # Using Digital pins
            if item_info_dictionary["PIN"]["Digital"] != 0:
                digital_pins = list(digital_pins)
                try:
                    item_items_dict["Digital_pins"] = digital_pins[0:item_info_dictionary["PIN"]["Digital"]]
                except IndexError:
                    print("Nathan MAX Digital ERROR")
                    raise IndexError
                # decrease avalible digital pins
                digital_pins = set(digital_pins) - set(digital_pins[0:item_info_dictionary["PIN"]["Digital"]])

                        # Using Analog pins
            if item_info_dictionary["PIN"]["Analog"] != 0:
                try:
                    item_items_dict["Analog_pins"] = analog_pins[0:item_info_dictionary["PIN"]["Analog"]]
                except IndexError:
                    print("Nathan MAX Analog ERROR")
                    raise IndexError
                # decreade avaliabe Analog pins
                analog_pins = set(analog_pins) - set(analog_pins[0:item_info_dictionary["PIN"]["Analog"]])

                        # Generate Item ID
            item_id = f"{item}_{i}"
            # Adding modfied element to items_dict
            items_dict[item_id] = item_items_dict

    return items_dict
