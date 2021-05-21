
####################################################################################################################
#                                            Lab Exercise 5
#
# Write a program that takes a list called numbers that has an even length.
# Your program should should insert an '*' between each element of the list. Then print the modified list.
#
#  Expected Output:
#  If numbers = [1, 2, 3, 4] then you will print: [1, '*', 2, '*', 3, '*', 4]
#  If numbers = [0, 0, 0, 0, 0, 0] then you will print: [0, '*', 0, '*', 0, '*', 0, '*', 0, '*', 0]
#
####################################################################################################################


num = [1, 2, 3, 4]
for i in range(len(num) + len(num) - 2):
    if i % 2 != 0:
        num.insert(i, "*")

print(num)

# Output => [1, '*', 2, '*', 3, '*', 4]

num = [0, 0, 0, 0, 0, 0]
for i in range(len(num) + len(num) - 2):
    if i % 2 != 0:
        num.insert(i, "*")

print(num)

# Output => [0, '*', 0, '*', 0, '*', 0, '*', 0, '*', 0]

# ALTERNATIVE SOLUTION

numbers = [1, 2, 3, 4]

length = len(numbers)
i = 0

while i < length:
  if i % 2 != 0:
    numbers.insert(i, '*')
    length += 1
  i += 1

print(numbers)

# Output => [1, '*', 2, '*', 3, '*', 4]