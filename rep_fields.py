age = 24
print("My age is " + str(age) + " years") 

print("My age is {0} years".format(age))

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
.format(31, "Jan", "Mar", "May", "jul", "Aug", "Oct", "Dec"))

print("There are {0} in Jan, Mar, May, Jul, Aug, Oct, Dec".format(31))

print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, Jun: {1}, Jul: {2}, Aug: {2}, Sep: {1}, Oct: {2}, Nov: {1}, Dec: {1}"
    .format(28, 30, 31))

print("Hello, this is {0}. I am the new {1}".format("Robert", "Janitor"))

print()

print("""Jan: {2} 
Feb: {0} 
Mar: {2} 
Apr: {1} 
May: {2} 
Jun: {1} 
Jul: {2} 
Aug: {2} 
Sep: {1} 
Nov: {1} 
Oct: {2} 
Dec: {1}
""".format(28, 30, 31))



