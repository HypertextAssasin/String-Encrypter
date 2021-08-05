from random import randint

nonEstring=list(input("Enter a word: "))

def shiftDict(i):
    i = i % 26
    alpha = str("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    return dict(zip(alpha, alpha[i:] + alpha[:i]))

Estring=[]
key = randint(1,26)
data = shiftDict(key)
print(nonEstring)
for i in nonEstring:
    Estring.append(data[i])
print('unEncrypted:',nonEstring)
print('paste these letters in decrypter \nEncrypted: ',Estring + "=-=" + str(key))
