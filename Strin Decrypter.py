nondecryptedstr = list(input("Enter the string you want to decrypt:"))

data = {'a': 'v', 'b': 'w', 'c': 'x', 'd': 'y', 'e': 'z', 'f': 'a', 'g': 'b', 'h': 'c', 'i': 'd', 'j': 'e',
            'k': 'f', 'l': 'g', 'm': 'h', 'n': 'i', 'o': 'j', 'p': 'k', 'q': 'l', 'r': 'm', 's': 'n', 't': 'o',
            'u': 'p', 'v': 'q', 'w': 'r', 'x': 's', 'y': 't', 'z': 'u', 
           'A': 'V', 'B': 'W', 'C': 'X', 'D': 'Y', 'E': 'Z', 'F': 'A', 'G': 'B', 'H': 'C', 'I': 'D', 'J': 'E',
            'K': 'F', 'L': 'G', 'M': 'H', 'N': 'I', 'O': 'J', 'P': 'K', 'Q': 'L', 'R': 'M', 'S': 'N', 'T': 'O',
            'U': 'P', 'V': 'Q', 'W': 'R', 'X': 'S', 'Y': 'T', 'Z': 'U'}
key_list = list(data.keys())
val_list = list(data.values())
 
for i in nondecryptedstr:
    position = val_list.index(i)
    print("Your decrypted String is:")
    print(key_list[position],end="")
 
 

