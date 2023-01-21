import base64
from baseconv import base
import pyfiglet

def doozy():
    ascii_art = pyfiglet.figlet_format("doozy")
    print(ascii_art)

doozy()

def detect_base_encoding(encoded_string):
    """
    Detects the type of base encoding used for a given encoded string.
    """
    try:
        base64.b64decode(encoded_string)
        return "base64"
    except:
        pass
    try:
        base64.b32decode(encoded_string)
        return "base32"
    except:
        pass
    try:
        base64.b16decode(encoded_string)
        return "base16"
    except:
        pass
    try:
        base.decode(encoded_string, 58)
        return "base58"
    except:
        pass
    try:
        base.decode(encoded_string, 85)
        return "base85"
    except:
        pass
    try:
        base.decode(encoded_string, 91)
        return "base91"
    except:
        pass
    return "Unknown"

encoded_string = input("Enter the encoded string: ")
base_encoding = detect_base_encoding(encoded_string)
print("The base encoding is:", base_encoding)
