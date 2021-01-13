#import required library
import os

# iterate through avaliable Board in folder
def get_board_list():

        # get all board name
    for (dirpath, dirnames, filenames) in os.walk('resources/Boards'):
        pass
   
    return [filename.replace(".json", "") for filename in filenames]

# iterate through avaliable item in folder
def get_item_list():
        # get all item name
    for (dirpath, dirnames, filenames) in os.walk('resources/items'):
        pass

    return [filename.replace(".json", "") for filename in filenames]
