def temp_celsius(celsius):
    fahrenheit = int(round((9 * int(celsius)) / 5 + 32))
    return fahrenheit

def temp_fahrenheit(fahrenheit):
    celsius = int(round((fahrenheit - 32) * 5 / 9))
    return celsius
