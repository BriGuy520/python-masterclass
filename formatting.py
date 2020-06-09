for i in range(1, 13):
  print("No. {0} squared is {1} and cubed is {2}"
  .format(i, i ** 2, i ** 3))

print()

for i in range(1, 15):
  print("No. {0:2} squared is {1:3} and cubed is {2:3}"
  .format(i, i ** 2, i ** 3))

print()

for i in range(1, 13):
  print("No, {0:2} squared is {1:<3} and cubed {2:<4}"
  .format(i, i ** 2, i ** 3))

print()

for i in range(1, 13):
  print("No. {0:2} squared is {1:>3} and cubed {2:^5}"
  .format(i, i ** 2, i ** 3))

print()

print("Pi is approximately {0:12}".format(22/7))
print("Pi is approximately {0:12f}".format(22/7))
print("Pi is approximately {0:12.50f}".format(22/7))
print("Pi is approximately {0:52.50f}".format(22/7))
print("Pi is approximately {0:62.50f}".format(22/7))
print("Pi is approximately {0:<72.50f}".format(22/7))
print("Pi is approximately {0:<72.54f}".format(22/7))

print()

for i in range(1, 13):
  print("No. {} squared is {} and cubed {:4}"
  .format(i, i ** 2, i ** 3))

print()
print()

print("This is the calculation for 33/7: {0}".format(33/7))
print("This is the calculation for 33/7: {0:3f}".format(33/7))
print("This is the calculation for 33/7: {0:6f}".format(33/7))
print("This is the calculation for 33/7: {0:12.50f}".format(33/7))
print("This is the calculation for 33/7: {0:6.5f}".format(33/7))
print("This is the calculation for 33/7: {0:6.2f}".format(33/7))
print("This is the calculation for 33/7: {0:8.50f}".format(33/7))
