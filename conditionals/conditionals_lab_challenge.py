
#######################################################################################################
#                                Lab Challenge - Month of the Year
#
# Write a program that determines the month of the year based on the value of variable called month.
# The variable will be a number from 1 to 12 (1 is January, 2 is February, etc.).
# Use a print statement to write the month to the screen.
#
#######################################################################################################


month=3 #month index 3: April

My_list = ["January","February","March","April","May","June","July","August","September","October","November","December"]
if(month>=1 and month<=12):
    print(My_list[month-1])

#Output => March