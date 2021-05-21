
####################################################################################################################
#                                            Lab Exercise 2
#
#  Write a program that takes a list called my_list (it could be a list of any data type)
#  and prints the list three times if the length of the list is less than 5.
#  If the length of my_list is greater than or equal to 5, then print the list one time.
#  Expected Output
#  If my_list = ['hi', 'hello'] then you will print ['hi', 'hello', 'hi', 'hello', 'hi', 'hello']
#  If my_list = [65, 111, 2, 81, 65, 32] then you will print [65, 111, 2, 81, 65, 32]
#
####################################################################################################################

my_list=[1,2,3]
if len (my_list) < 5:
  print(my_list * 3)
else:
  print(my_list)

# Output => [1, 2, 3, 1, 2, 3, 1, 2, 3]