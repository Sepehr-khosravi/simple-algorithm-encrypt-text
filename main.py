words = ['a' , 'b' , 'c' , 'd' ,'e' , 'f' , 'g' , 'h' , 'i' ,'j' , 'k' , 'l' ,'m' ,'n' , 'o' ,'p' ,'q' ,'r' ,'s' ,'t' ,'u' ,'v' , 'w' ,'x' ,'y' , 'z']

numbers = []
for a in range(26):
    numbers.append(222 + a)


encryptObject= {}

for b in range(26):
    encryptObject[words[b]] = numbers[b]


text = input("Enter your text :")

splitText = list(text)

array = []

for c in range(len(splitText)):
    array.append(splitText[c].lower())

code= []

for d in range(len(array)):
    code.append(encryptObject[array[d]])


encyptCode = ""


for f in range(len(code)):
    encyptCode += str(code[f])

print(encyptCode)


