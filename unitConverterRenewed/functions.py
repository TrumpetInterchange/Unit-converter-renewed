"""
A module with functions
"""
import conversion as cv
def init():
    """
    Startup sequence. Prints fancy texts.

    Args: none

    Returns: none
    """
    title = 'U N I T _ C O N V E R T E R'
    stars = '***************************'
    print(f'{stars}\n{stars}\n{title}\n{stars}\n{stars}')

def isFloat(input:str):
    """
    Checks if the input has correct type. Must be used with input().

    Args:
        input: the user input from input() that you want to convert to float

    Returns:
        True: returns it when it converts to float successfully
        False: when it fails to convert to float

    Raises:
        TypeError: when it fails to convert input to float
    """
    try:
        float(input)
    except:
        return False
    return True

def isIntger(input:str):
    """
    Checks if the input has correct type. Must be used with input().

    Args:
        input: the user input from input() that you want to convert to integer

    Returns:
        True: returns it when it converts to integer successfully
        False: when it fails to convert to integer

    Raises:
        TypeError: when it fails to convert input to ineger
    """
    try:
        int(input)
    except:
        return False
    return True

def layout():
    """
    Lays out a list that contains what to convert

    Args:
        none
    
    Returns:
        none
    """
    order = 1
    print('What do you want to convert?')
    for i in cv.values:
        print(f'{order}. {i}')
        order = order + 1

def tempLayout():
    """
    Lays out how to convert a tempreature unit to another

    Args:
        none

    Returns:
        none
    """
    order = 1
    print('How do you want to convert?')
    for i in cv.temp_conversion:
        print(f'{order}. {i}')
        order = order + 1

def notValidResponse(type:str):
    """
    Prints "Not a valid response. Try again.

    Args:
        type: Enter the data type you want to make the user repond correctly.

    Returns:
        none
    """
    print(f'Not a valid reponse. Please enter a valid {type}.')