import json
def word2vec(item_name, max_length):
    SENSORNAME = ['ALCD','DHT11','DHT12','DHT22','DS1B820','hc-sr04','MH-RD','relay']
    item_name = [x for x in SENSORNAME if str(x) in item_name][0]
    with open(f"resources/items/{item_name}.json") as json_file:
            sentence = json.load(json_file)["Description"]
    word_length = len(sentence)
    word_list = []
    for i in range(0, word_length, max_length):
        word_list.append(sentence[i:i+max_length])

    return word_list


'''
def word2vec(sentence, max_length):
    word_list = sentence.split(' ')
    vector = []
    
    for i in range(0, len(sentence), max_length):
        splited_temporary_sentence = sentence[i:i+max_length].split(' ')
        
        previous_word = None
        this_line = []    
        print(splited_temporary_sentence)
        for index, splited_word in enumerate(splited_temporary_sentence):
            
            if index==0 and splited_word=="":
                continue
            
            # print(index, splited_word)
            if splited_word not in word_list:
                previous_word = splited_word
                #print(previous_word)
            else:
                this_line.append(splited_word)
                
            if previous_word is not None:
                
                
        #print(this_line)

'''
