"""
A module with unit conversion formulas
"""

values = ['Tempreature','Velocity','Mass','Quit']

#Tempreature conversions

temp_conversion = [
    'Celsius to Fahrenheit',
    'Fahrenheit to Celsius',
    'Celsius to Kelvin',
    'Kelvin to Celsius',
    'Fahrenheit to Kelvin',
    'Kelvin to Fahrenheit'
    ]

def C2F(celsius:float):
    """
    Converts Celsius to Fahrenheit

    Args:
        celsius: Tempreature in Celsius that you want to convert to Fahrenheit

    Returns:
        fahrenheit: Tempreature in Fahrenheit that was converted from Celcius
    """
    fahrenheit = celsius*(9/5)+32
    return fahrenheit

def F2C(fahrenheit:float):
    """
    Converts Fahrenheit to Celsius

    Args:
        fahrenheit: Tempreature in Fahrenheit that you want to convert to Celsius

    Returns:
        celsius: Tempreature in Celsius that was converted from Fahrenheit
    """
    celsius = (fahrenheit-32)*(5/9)
    return celsius

def C2K(celsius:float):
    """
    Converts Celsius to Kelvin
    
    Args:
        celsius: Tempreature in Celsius that you want to convert to Kelvin

    Returns:
        kelvin: Tempreature in Kelvin that was converted from Celsius
    """
    kelvin = celsius + 273.15
    return kelvin

def K2C(kelvin:float):
    """
    Converts Kelvin to Celsius
    
    Args:
        kelvin: Tempreature in Kelvin that you want to convert to Celsius

    Returns:
        celsius: Tempreature in Celsius that was converted from Kelvin
    """
    celsius = kelvin - 273.15
    return celsius

def F2K(fahrenheit:float):
    """
    Converts Fahrenheit to Kelvin using F2C() and C2K()
    
    Args:
        fahrenheit: Tempreature in Fahrenheit that you want to convert to Kelvin

    Returns:
        kelvin: Tempreature in Kelvin that was converted from Fahrenheit
    """
    kelvin = C2K(F2C(fahrenheit))
    return kelvin

def K2F(kelvin:float):
    """
    Converts Kelvin to Fahrenheit using K2C() and C2F()
    
    Args:
        kelvin: Tempreature in Kelvin that you want to convert to Fahrenheit

    Returns:
        fahrenheit: Tempreature in Kelvin that was converted from Fahrenheit
    """
    fahrenheit = C2F(K2C(kelvin))
    return fahrenheit