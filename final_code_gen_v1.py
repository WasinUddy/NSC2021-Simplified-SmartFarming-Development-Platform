from backend.setup_function_generator import setup_and_header_generator
from backend.value_listener_variable_generator import value_listener_variable_generator
from backend.condition_generator import condition_code_generator_digital_output
from backend import command
item_dict = {'DHT11_0':
                 {
                     'I2C': False,
                     'SPI': None,
                     'Serial': None,
                     'Digital_pins': [0],
                     'Analog_pins': []
                 },
            'DHT11_1':
                {
                    'I2C': False,
                    'SPI': None,
                    'Serial': None,
                    'Digital_pins': [1],
                    'Analog_pins': []},
            'DHT11_2':
                {'I2C': False,
                 'SPI': None,
                 'Serial': None,
                 'Digital_pins': [2],
                 'Analog_pins': []
                 },
            'relay_0':
                {'I2C': False,
                 'SPI': None,
                 'Serial': None,
                 'Digital_pins': [3],
                 'Analog_pins': []
                 },
            'relay_1':
                {'I2C': False,
                 'SPI': None,
                 'Serial': None,
                 'Digital_pins': [4],
                 'Analog_pins': []}
}

condition_dict = {'OUTPUT':
                      ['relay_0', 'relay_0', 'relay_1', 'relay_1', 'relay_0', 'relay_0'],
                  'INPUT':
                      ['DHT11_0_Temperature', 'DHT11_0_Humidity', 'DHT11_1_Temperature', 'DHT11_1_Humidity', 'DHT11_2_Humidity', 'DHT11_2_Humidity'],
                  'CONDITION': ['>', '==', '>', '<', '==', '=='],
                  'VALUE': ['1', '2', '3', '4', '5', '6']
                  }

initial_header, initial_setup, initial_function, usable_function = setup_and_header_generator(item_dict)
variable_declaration, _ = value_listener_variable_generator(item_dict)
del _
import pandas as pd
condition_code = """
void loop(){
"""
condition_code += condition_code_generator_digital_output(pd.DataFrame.from_dict(condition_dict), item_dict)
condition_code += """
}
"""
text = """
"""
text += initial_header

text += variable_declaration

text += initial_setup

text += initial_function

text += condition_code


arduino_code = command.Sketch("arduino:avr:nano", "COM11", "first")
arduino_code.create_sketch()
arduino_code.write_sketch(text)
arduino_code.verify_sketch()
arduino_code.upload_sketch()

