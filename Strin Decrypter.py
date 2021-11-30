rawstr = input("Enter the string you want to decrypt:")

def shiftDict(i):
    i = i % 26
    alpha = str("abcdefghijklmnopqrstuvwxyz")
    return dict(zip(alpha, alpha[i:] + alpha[:i]))


key = 26 - int(rawstr.split("=-=")[1])
nonDstring = list(rawstr.split("=-=")[0])
data = shiftDict(key)
Dstring = ""
for i in nonDstring:
    Dstring += data.get(i)

print("The decrypted string is " + Dstring)


 
 

