a = 12 
b = 3

print(a + b) # 15
print(a - b) #9 
print(a * b) #36
print(a / b) # 4
print(a // b) # 4 Integer Division: rounded down towards minus infinity
print(a % b)  # 0 modulo: The remainder after the integer division

print()

print(a + b / 3 - 4 * 12)
print(a + (b / 3) - (4 * 12))
print((((a + b) / 3) - 4) * 12)
print(((a + b) / 3 - 4) * 12)

c = a + b
d = c / 3
e = d - 4
print(e * 12)

print()

print(a / (b * a ) / b)
