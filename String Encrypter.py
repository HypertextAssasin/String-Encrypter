from random import randint

nonEstring=list(input("Enter a word: "))

def shiftDict(i):
    i = i % 26
    alpha = str("abcdefghijklmnopqrstuvwxyz")
    return dict(zip(alpha, alpha[i:] + alpha[:i]))

Estring=[]
key = randint(1,26)
data = shiftDict(key)
print(nonEstring)
print(data)
for i in nonEstring:
    Estring.append(data[i])
print('unEncrypted:',nonEstring)
Estr = ''
for letter in Estring:
  Estr +=letter
print('paste these letters in decrypter \nEncrypted: ',Estr + "=-=" + str(key))
