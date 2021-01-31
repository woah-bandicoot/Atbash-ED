""" A simple Atbash Encoder and Decoder.
Version: 1.0(Console)
Created by: Red Bandicoot
Licence: Free

Note: This program was created as a first project,
so if so any tip or advice about programming is appreciated :)"""

# Program menu created
def menu():
    print("[1] Encoder")
    print("[2] Decoder")
    print("[0] Exit the program.")

# Encode funtion create, only encrypt letters from A to Z
def encode(encode_text):
    encode_text = encode_text.upper()
    c_encode_text = list(encode_text)
    ciphertext = ''
    
    for character in c_encode_text:
        # Matching the character from ASCII
        ascii_character = ord(character)
        
        # Encoding only latin alphabet
        if ascii_character >= 65 and ascii_character <= 90:
            position = ascii_character - 65
            position = 25 - position
            ascii_character = position + 65
            character = chr(ascii_character)
        
        ciphertext = ciphertext + character
    
    print('[',ciphertext,']')

    
# Decode func created, only decrypt letters from A to Z
def decode(decode_text):
    decode_text = decode_text.upper()
    c_decode_text = list(decode_text)
    ciphertext = ''
    
    for character in c_decode_text:
        # Matching the character from ASCII
        ascii_character = ord(character)
        
        # Decoding only latin alphabet
        if ascii_character >= 65 and ascii_character <= 90:
            position = ascii_character - 65
            position = 25 - position
            ascii_character = 65 + position
            character = chr(ascii_character)
        
        ciphertext = ciphertext + character
    
    print('[',ciphertext,']')

# main() func for management
def main():
    while True:
        try:
            menu()
            option = int(input("Enter your option: "))
        except:
            print("Invalid input, please try again.")
            continue
        
        if option not in [0, 1, 2]:
            print(option, "is not an option.")
            continue
        
        elif option == 1:
            print("Encoding option has been chosen.")
            encode_text = input("Enter the text to be encoded:")
            encode(encode_text)
            continue
        
        elif option == 2:
            print("Decoding option has been chosen.")
            decode_text = input("Enter the text to be decoded:")
            decode(decode_text)
            continue
        else:
            break

if __name__ == "__main__":
    main()
