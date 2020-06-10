answer = 5

print("Please guess number between 1 and 10")
guess = int(input())

# if guess != answer:
#   if guess < answer:
#     print("Please guess higher")
#   else:
#     print("Please guess lower")
#   guess = int(input())
#   if guess == answer:
#     print("Well done, you guessed it")
#   else:
#     print("Sorry, you have not guessed correctly")
# else:
#   print("You got it on the first try")

if guess == answer:
  print("You got it on the first try")
else:
  if guess < answer:
    print("Please guess higher")
  else:
    print("Please guess lower")
  guess = int(input())
  if guess == answer:
    print("Well done, you guessed it")
  else:
    print("Sorry, you have not guessed correctly")




# if guess < answer:
#   print("Please guess a higher number")
#   guess = int(input())
#   second_guess()
# elif guess > answer:
#   print("Please guess a lower number")
#   second_guess()
# else: 
#   print("Correct! {} is the number")


def second_guess():
  guess = int(input())
  if guess == answer:
    print("Well done, that's correct")
  else: 
    print("Nope, that's incorrect")