import base64

s = open("D:/Github/transmission.b64", "r").readline()
print(len(s))
#print(base64.b64decode(s))
for c in range(len(s)-16):
    sample = s[c:c+16]
    fail = False
    for i in range(16):
        if sample.count(sample[i]) != 1:
            fail = True
            break
    if fail == False:
        print(base64.b64decode(sample))

#Curtisisland


