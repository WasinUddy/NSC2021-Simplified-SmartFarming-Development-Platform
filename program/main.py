from frontend.gui import Gui
import os
from backend.scrapper import check_library
# Set Environment Path

g = Gui()

print(check_library())
while g.running:
    g.run()
