def vowel(text):
    vowels = "a", "e", "i", "o", "u"
    let = ([letter for letter in text if letter in vowels])
    print("Vowels:", end=' ')
    print(*let, sep=',')

vowel("Umuzi")
