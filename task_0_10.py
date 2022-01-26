from collections import Counter


def common(str1, str2):
    dict1 = Counter(str2)
    dict2 = Counter(str1)

    commonDict = dict1 & dict2

    if len(commonDict) == 0:
        print(-1)

    commonChars = (commonDict.elements())
    commonChars = commonChars
    print("Common letters: " + ', '.join(commonChars))


if __name__ == "__main__":
    str1 = 'house'
    str2 = 'computers'
    common(str1, str2)

