print("today is a good day to learn python")
print('Python is fun')
print("Python's string are easy to use")
print('We can even include "quotes" in strings')
print("Hello" + " world")
greeting = "Hello"
name = "Brian"
print(greeting + name)

# If we want a space, we can add that too
print(greeting + " " + name)

parrot = "Norweigen Blue"

age = 30
print(age)

print(type(greeting))
print(type(age))

age_in_words = "2 years"
print(name + f" is {age} years old.")
print(type(age_in_words))

print(f"Pi is approximately {22 / 7:12.50f}")

pi = 22 / 7 

print(f"Pi is approximately {pi:12.50f}")

# print(name + " is " + age  + " years old.")
print(type(age_in_words))


print(parrot[0:6]) #Norweg

print(parrot[1:7])
print(parrot[3:5])
print(parrot[0:9])
print(parrot[:9])
# slice the word 'blue'
print(parrot[10:14])
print(parrot[10:])

print(parrot[:6])
print(parrot[6:])

print(parrot[:6] + parrot[6:])
print(parrot[:])


letters = 'abcdefghijklmnopqrstuvwxyz'

print(parrot[-4:2])
print(parrot[-4:-2])
print(parrot[-4:12])

print(parrot[-14:-8])

# steps in a slice

football = "Chicago Bears"

print(football[0:6:2])
print(football[0:6:3])

number = "9,223;372:036 854,775;807"

seperators = number[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])
