
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
