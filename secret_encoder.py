# letters = 'abcdefghijklmnopqrstuvwxyz'
# secret = [1, 0, 3]

# def translate(index, master):
#     return master[index]
    
# def map_over(collection, master, how):
#     result = ""
#     for item in collection:
#         result += how(item, master)
#     return result

# print(map_over(secret, letters, translate))

###############################

# letters = 'abcdefghijklmnopqrstuvwxyz'
# secret = input("What's your secret? ")

# def encode(message, master):
#     result = []
#     for item_index in message:
#         encoded_letter = master.find(item_index)
#         result.append(encoded_letter)
#     return result

# print(encode(secret, letters))

################################

# letters = 'abcdefghijklmnopqrstuvwxyz'
# secret = input("What's your secret? ")

# def translate(index, master):
#     return master.index(index)

# def map_over(collection, master, how):
#     result = []
#     for item_index in collection:
#         result.append(how(item_index, master))
#     return result


# print(map_over(secret, letters, translate))


####################
# Aquino's version #
####################
letters = 'abcdefghijklmnopqrstuvwxyz'
secret = input("What's your secret? ")

def convert_letter_to_number (a_letter, master):
    #find a_letter in master
    return master.index(a_letter)
    #save the index
    #then return it

def encode(message, master):
    result = []
    for letter in message:
        result.append(convert_letter_to_number(letter, master))
    return result

print(encode(secret, letters))