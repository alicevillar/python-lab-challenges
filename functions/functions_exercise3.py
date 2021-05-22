
####################################################################################################################
#                                      Functions - Lab Exercise 3
#
# Write a function called search_list that takes a list and a search term as parameters.
# If the search term is located in the list, return the index of the matching element.
# The function should work even if there is a difference in capitalization.
#  If the search term is not in the list, return -1.
#
#  Expected Output:
#  If the function call is search_list(["dog", "fish", "cat"], "Cat"), the the function would return 2
#  If the function call is search_list(["water", "Toy", "house"], "toy"), then the function would return 1
# If the function call is search_list(["box", "car", "hat"], "mouse"), the the function would return -1
#
####################################################################################################################


def search_list(my_list, search_term):
  for i in range(len(my_list)):
    search_term = search_term.lower()
    my_list[i] = my_list[i].lower()

    if my_list[i] == search_term:
      return i
  return -1

