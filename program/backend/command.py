'''
Class for Arduino Board and Arduino Sketch object
'''
# import require library
import os
from backend.MS_windows_serial_scanner import ms_windows_serial_scanner
from backend.arduino_port_finder import arduino_port_finder
import json

# defined Board object
class Board:

    def __init__(self, board, programmer):
        self.board = board
        self.programmer = programmer
		
		
    def burn_bootloader(self):
        os.system(f"arduino-cli burn-bootloader -b {self.board} -P {self.programmer}")

    def clean_cache(self):
        os.system(f"arduino-cli cache clean")


class Sketch:

    def __init__(self, board, sketch):
        self.board = board
        self.port= arduino_port_finder(ms_windows_serial_scanner())
        self.sketch = sketch



    def create_sketch(self):
        os.system(f"arduino-cli sketch new {self.sketch}")

    def verify_sketch(self):
        os.system(f"arduino-cli compile -b {self.board} {self.sketch}")

    def upload_sketch(self):

        os.system(f"arduino-cli upload -p {self.port} --fqbn {self.board} {self.sketch}")

    def write_sketch(self, text):
        with open(f"{self.sketch}/{self.sketch}.ino", "wt") as ino:
            ino.truncate(0)
            code = text
            ino.write(code)






