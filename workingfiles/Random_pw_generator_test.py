# from datetime import time, datetime
# import time
import random


length=6

letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
ln=['letter','number']
key = []

for i in range(length):
    pick=random.choice(ln)
    if pick == 'letter':
        key.append(random.choice(letters))
    elif pick == 'number':
        key.append(random.choice(numbers))

fullkey = "".join(key)
print(fullkey)


letterstest="".join(letters)
print(letterstest)