# for i in range(1, 13):
#   print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
#   print("*" * 80) 

name = input("Please enter your name: ")
age = int(input("What is your age, {0} ".format(name)))


if age >= 18: 
  print("Congratulations {}, you can vote for the lesser of two evils".format(name))
else:
  print("Sorry {}, you're going to have to wait ".format(name) + str(18 - age) + " more years to throw away your vote")