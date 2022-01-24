def temp_celc(cel):
    fer = int(round((int(cel) - 32) * 5 / 9))
    return fer

def temp_fer(fer):
    cel = int(round((9 * int(fer)) / 5 + 32))
    return cel
