
#######################################################################################################
#                                Conditionals - Lab Exercise 2 & 3
#
#  Use the variable x as you write this program. x will represent a positive integer.
#
#  Write a program that determines if x is divisible by 5.
#  If yes, print _ is divisible by 5, where the blank is the value of x. If no, print _ is not divisible by 5,
#  where the blank is the value of x.
#
#  Expected Output
#  If x is 50, then the output would be: 50 is divisible by 5 and even.
#  If x is 37, then the output would be: 37 is not divisible by 5 or it is odd.
#######################################################################################################

x = 50
if (x % 5 == 0 and x % 2 == 0):
  print(str(x) + " is divisible by 5 and even")

else:
  print(str(x) + " is not divisible by 5 or it is odd")

# Output => 50 is divisible by 5 and even

x = 37
if (x % 5 == 0 and x % 2 == 0):
  print(str(x) + " is divisible by 5 and even")

else:
  print(str(x) + " is not divisible by 5 or it is odd")

# Output => 37 is not divisible by 5 or it is odd

