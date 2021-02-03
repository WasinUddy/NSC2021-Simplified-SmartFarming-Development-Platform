def word2vec(sentence, max_length):
    word_length = len(sentence)
    word_list = []
    for i in range(0, word_length, max_length):
        word_list.append(sentence[i:i+max_length])

    return word_list

