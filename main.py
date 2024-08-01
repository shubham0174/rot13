
text = input("Enter your encrypted text: ")
result = ''
for i in text:
    if not i.isalpha() or i.isdigit(): 
        result += i
        continue
    value = ord(i)
    if value < 78: value += 13
    elif value <= 90: value -= 13
    elif value < 110: value += 13
    elif value <= 122: value -= 13 
    result += chr(value)
print("Here your decrypted text: ",result)