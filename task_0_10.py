def common_letters(first_word, second_word):
    first_word = set(first_word)
    second_word = set(second_word)
    print("Common letters:", end=' ')
    print(','.join(first_word.intersection(second_word)))
    
