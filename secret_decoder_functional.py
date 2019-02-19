letters = 'abcdefghijklmnopqrstuvwxyz'
secret = [1, 0, 3]

def translate(index, master):
    return master[index]
    
def map_over(collection, master, how):
    result = ""
    for item in collection:
        result += how(item, master)
    return result

print(map_over(secret, letters, translate))