def celsius_to_fahrenheit(celsius):
    fahrenheit = round((9 * celsius) / 5 + 32)
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = round((fahrenheit - 32) * 5 / 9)
    return celsius
