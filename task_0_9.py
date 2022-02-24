def vowel(text):
    vowels = "AaEeIiOoUu"
    let = ({letter for letter in text.lower() if letter in vowels})
    print("Vowels:", end=' ')
    print(*let, sep=',')
    
vowel("Umuzi")
