import random
a = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
b = int(input('какой длины пароль?'))
key = ''
for i in range(b):
    key = key + random.choice(a)
print(key)