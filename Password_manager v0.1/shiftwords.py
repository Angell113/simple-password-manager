

 
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

 
# sleep(1000)
 
# while True:
#     text = input("Enter key: ")
#     key = int(text)
 
#     text = input("Enter printable character(s): ")
 
#     result = ascii_shift(key, text)
    
#     print("result:", result)
#     print()
#     break




# import base64

# base64_message = 'UHl0aG9uIGlzIGZ1bg=='
# base64_bytes = base64_message.encode('ascii')
# message_bytes = base64.b64decode(base64_bytes)
# message = message_bytes.decode('ascii')

# print(message)