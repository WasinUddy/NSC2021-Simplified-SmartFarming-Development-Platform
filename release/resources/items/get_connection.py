def get_connection(item_ID, items_dict):
    I2C_pins = items_dict[item_ID]['I2C']
    Digital_pins = items_dict[item_ID]["Digital_pins"]
    Analog_pins = items_dict[item_ID]["Analog_pins"]

    if I2C_pins is True and Digital_pins != []:
        data = {
            "TYPE": "I2C_INT",
            "INT": Digital_pins[0]
        }
        return data

    if I2C_pins is True and Digital_pins == []:
        data = {
            "TYPE": "I2C_NOINT",
        }
        return data

    if Digital_pins != []:
        data = {
            "TYPE": "Digital_pins",
            "PIN": Digital_pins[0]
        }
        return data
    
    if Analog_pins != []:
        data = {
            "TYPE": "Analog_pins",
            "PIN", Analog_pins[0]
        }
        return data

        
        
