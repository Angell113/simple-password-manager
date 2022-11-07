

 
def ascii_shift_minus(key, text):
    result = ""
    for letter in text:
        ascii = ( ord(letter) - key - 32 ) % 94 + 32
        result = result + chr(ascii)
    return result



def ascii_shift_plus(key, text):
    result = ""
    for letter in text:
        ascii = ( ord(letter) + key - 32 ) % 94 + 32
        result = result + chr(ascii)
    return result

 
