import json
def word2vec(item_name, max_length):
<<<<<<< HEAD
    
=======
>>>>>>> f18030c74d5045a1c912de0ff63b902eb5e750a5
    item_name = item_name.split('_')[0]
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
