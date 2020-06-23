#  python -m doctest -v .\using_modules\helpers\src\helpers\strings.py
def extract_upper(phrase):
    """
    extract_upper takes a string and returns a list containing
    only the uppercase characters from the string

    >>> extract_upper("Hello There, BOB")
    ['H', 'T', 'B', 'O', 'B']
    """
    return list(filter(str.isupper, phrase))

def extract_lower(phrase):
    return list(filter(str.islower, phrase))

if __name__ == "__main__":
    print("HELLO FROM HELPERS")