def find_common_letters(first_word, second_word):
    common_chars = ({letter for letter in first_word.lower() if letter in second_word.lower()})
    print("Common Letters:", end=' ')
    print(*common_chars, sep=',')
