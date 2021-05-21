
####################################################################################################################
#                                 Functions - Lab Exercise 1
#
# Write a function called avg that takes two parameters. Return the average of these two parameters.
# If the parameters are not numbers, return the string, Please use two numbers as parameters.
#
#  Expected Output
#  If the function call is avg(10,25), then the function would return 17.5
#  If the function call is avg(10, "cat"), then the function would return Please use two numbers as parameters
#
####################################################################################################################

# If the function call is avg(10,25):
def avg(n1,n2):
  if type(n1)==type("Hello") or type(n2)==type("Hello"):
    return "Please use two numbers as parameters"
  return (n1+n2)/2

print(avg(10,25))
# Output => 17.5

# If the function call is avg(10, "cat"):
def avg(n1,n2):
  if type(n1)==type("Hello") or type(n2)==type("Hello"):
    return "Please use two numbers as parameters"
  return (n1+n2)/2

print(avg(10, "cat"))

# Output => Please use two numbers as parameters
