
#######################################################################################################
#                               Conditionals - Lab Exercise 4
#
#  Use the variable x as you write this program. x will represent a string.
#  Write a program using the elif keyword  that determines if x is a primary color (red, blue, or yellow).
#  If yes, print _ is primary color, where the blank is the value of x.
#  If no, print _ is not a primary color, where the blank is the value of x.
#
#   Expected Output:
#   If x is red, then the output would be: red is a primary color.
#   If x is teal, then the output would be: teal is not a primary color.
#
#######################################################################################################

x='blue'
if x == "red":
    print("x is red is a primary color")
elif x == "blue":
    print("blue is a primary color")
elif x == "yellow":
    print("yellow is a primary color")

# Output => blue is a primary color

#######################################################################################################
#                                 Conditionals -  Lab Exercise 5
#
#  Use the variable x as you write this program. x will represent a string.
#  Write a program that determines if x is a vowel (a, e, i, o, and u ).
#  If yes, print _ is a vowel, where the blank is the value of x.
#  If no, print _ is not a vowel, where the blank is the value of x.
#
#   Expected Output:
#   If x is a, then the output would be: a is a vowel.
#   If x is z, then the output would be: z is not a vowel.
#
#######################################################################################################

x='a'
if x in 'aeiouAEIOU':
    print(x, "is a vowel")
else:
    print(x, "is not a vowel")

# Output => a is a vowel

x='z'
if x in 'aeiouAEIOU':
    print(x, "is a vowel")
else:
    print(x, "is not a vowel")

# Output => z is not a vowel

#######################################################################################################################
# ALTERNATIVE SOLUTION:
#######################################################################################################################

x='a'
if x == "a" or x == "e" or x =="i" or x == "o" or x == "u" or x == "A" or x == "E" or x =="I" or x == "O" or x == "U":
    print(x + " is a vowel")
else:
    print(x + " is not a vowel")

# Output => a is a vowel
