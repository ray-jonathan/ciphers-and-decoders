letters = 'abcdefghijklmnopqrstuvwxyz'
secret = [1, 0, 3]

def translate(index, master):
    return master[index]

def map_over(collection, master, how):
    result = ""
    for item in collection:
        result += how(item, master)
    return result

# give your functions "verb" names
def decode(number_list, master_list):
    #configuation came in as arguments
    result = ''

    #do the translation
    #for each item in number_list...
    for item in number_list:

    #find that index in master_list...
        # letter = master_list[item]
    #put that character in result
        # result += letter
        result += translate(item, master_list)
    #return the result
    return result

decoded_message = decode(secret, letters)
print(decoded_message)




print(map_over(secret, letters, translate))