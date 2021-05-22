####################################################################################################################
#                                            Lab Exercise 1
#
# Write a recursive function called recursive_power that takes two integers as parameters.
# The first parameter is the base and the second parameter is the exponent.
# Return the base parameter to the power of the exponent.
#
#  Expected Output:
#  If the function call is recursive_power(5, 3), then the function would return 125
#  If the function call is recursive_power(4, 5), then the function would return 1024
#
####################################################################################################################

#  If the function call is recursive_power(4, 5)
def recursive_power(n1,n2):
  #base case
  if n2 == 0:
    return 1
  else:
    return n1*recursive_power(n1,n2-1)

print(recursive_power(4, 5))

# Output => 1024

#  If the function call is recursive_power(5, 3)
def recursive_power(n1,n2):
  #base case
  if n2 == 0:
    return 1
  else:
    return n1*recursive_power(n1,n2-1)

print(recursive_power(5, 3))

# Output => 125

# ALTERNATIVE SOLUTION:

total = 1
base = 5
exponent = 3

for i in range(exponent):
    total = total*base
print(total)

# Output => 125