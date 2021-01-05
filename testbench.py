input_dataframe = {'name': ['q', 'qs'], 'OUTPUT': ['DHT11_0_Temperature', 'DHT11_0_Humidity'], 'INPUT': ['16x2-I2C-LCD_0', '16x2-I2C-LCD_0'], 'row': ['1', '2']}
item_dict = {'16x2-I2C-LCD_0': {'I2C': True, 'SPI': None, 'Serial': None, 'Digital_pins': [], 'Analog_pins': []}, 'DHT11_0': {'I2C': False, 'SPI': None, 'Serial': None, 'Digital_pins': [0], 'Analog_pins': []}}


from backend.analog_output_codegenerator import noncondition_code_generator

noncondition_code_generator(input_dataframe, item_dict)