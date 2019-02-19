# Given a string, print the Caesar Cipher (or ROT13) of that string. 
# Use your solution to decipher the following text: 
# "lbh zhfg hayrnea jung lbh unir yrnearq"

alphabet = ("abcdefghijklmnopqrstuvwxyz"*2).upper()

def caesar_cipherize(cryptex):
    cipher = ""
    for letter in cryptex:
        if letter == " ":
            ciphered_letter = letter
        else:
            letter = int(alphabet.find(letter)) + 13
            ciphered_letter = alphabet[letter]
        cipher += ciphered_letter
    return cipher.capitalize()

def un_caesar_cipherize(cryptex):
    cipher = ""
    for letter in cryptex:
        if letter == " ":
            ciphered_letter = letter
        else:
            letter = int(alphabet.find(letter)) - 13
            ciphered_letter = alphabet[letter]
        cipher += ciphered_letter
    return cipher.capitalize()

answer = input("Would you like to CODE or DECODE a message? ").upper()
if answer == "CODE":
    code = input("What would you like to code? ").upper()
    return (caesar_cipherize(code))
elif answer == "DECODE":
    decode = input("What would you like to decode? ").upper()
    return (un_caesar_cipherize(decode))
else:
    return ("I didn't catch that. Try again please." )
