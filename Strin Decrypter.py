rawstr = input("Enter the string you want to decrypt:")

def shiftDict(i):
    i = i % 26
    alpha = str("ABCDEFGHIJKLMNOPQRSTUVWXYZ ")
    return dict(zip(alpha, alpha[i:] + alpha[:i]))


key = 26 - rawstr.strip("=--=")[1]
nonDstring = list(rawstr.strip("=--=")[0])
data = shiftDict(key)
Dstring = ""
for i in nonDstring:
    Dstring += data.get(i)

print("The decrypted string is " + Dstring)


 
 

