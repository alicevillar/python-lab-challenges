
####################################################################################################################
#                                            Lab Exercise 4
#
# Write a program that takes a list called numbers that contains integers in a sequence
# (the sequence is always increasing, never decreasing).
# Your program should add the next two numbers in the sequence, and then print the list.
#  Expected Output:
#  If numbers = [1, 2, 3, 4] then you will print [1, 2, 3, 4, 5, 6]
#  If numbers = [-5, -4, -3, -2] then you will print [-5, -4, -3, -2, -1, 0]
#
####################################################################################################################

numbers = [1, 2, 3, 4]
for i in range(2):
  numbers.append(numbers[-1]+1)
print(numbers)

# Output => [1, 2, 3, 4, 5, 6]

numbers = [-5, -4, -3, -2]
for i in range(2):
  numbers.append(numbers[-1]+1)
print(numbers)

# Output => [-5, -4, -3, -2, -1, 0]
