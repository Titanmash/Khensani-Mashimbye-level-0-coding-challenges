def temp_fahrenheit(celsius):
    fahrenheit = round((9 * celsius) / 5 + 32)
    return fahrenheit

def temp_celsius(fahrenheit):
    celsius = round((fahrenheit - 32) * 5 / 9)
    return celsius
