def common_letters(first_word, second_word):
    let = ({letter for letter in first_word.lower() if letter in second_word.lower()})
    print("Common Letters:", end=' ')
    print(*let, sep=',')

common_letters("house","computers")
