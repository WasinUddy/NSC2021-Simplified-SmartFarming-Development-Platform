from frontend.gui import Gui
import os
from backend.scrapper import check_library
# Set Environment Path
check_library()
g = Gui()


while g.running:
    g.run()
