def vowels_in_string(string):
    vowels = "AaEeIiOoUu"
    vowels_in_str = ({letter for letter in string.lower() if letter in vowels})
    print("Vowels:", end=' ')
    print(*vowels_in_str, sep=',')
