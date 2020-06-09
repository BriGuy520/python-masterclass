letters = 'abcdefghijklmnopqrstuvwxyz'

backwords = letters[25:0:-1]
print(backwords)
print(letters[25:0:-1] + letters[0])
print(letters[25::-1])
print(letters[::-1])

print(letters[16:13:-1])
print(letters[4::-1])
check = letters[25:17:-1]
print(len(check))
print(check)

print(letters[-4:])
print(letters[-1:])
print(letters[:1])
print(letters[0])

str1 = "unique lab"


print("=======================")
print(str1[3:6:1])
print(str1[::5])
print(str1[::6])
print(str1[5:10:2])


print("===================")

decode = "there is a secret message inside of this message. Can you find it?"

print(decode[:2:2])