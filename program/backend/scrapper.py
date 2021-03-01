import requests
import os 
import json



def checkInternetRequests(url='http://www.google.com/', timeout=3):
    try:
        #r = requests.get(url, timeout=timeout)
        r = requests.head(url, timeout=timeout)
        return True
    except requests.ConnectionError as ex:
        print(ex)
        return False

def check_library():
    directory = 'resources/items'
    items_file = []
    for filename in os.listdir(directory):
        if filename.endswith(".json"): 
            items_file.append(os.path.join(directory, filename)) 
        else:
            continue


    directory = 'resources/boards'
    board_file = []
    for filename in os.listdir(directory):
        if filename.endswith(".json"): 
            board_file.append(os.path.join(directory, filename)) 
        else:
            continue

    for json_file in items_file:
        with open(json_file) as jsons:
            item_info_dictionary = json.load(jsons)

        for lib in item_info_dictionary["Library"]:
            os.system(f'arduino-cli lib install {lib}')


    