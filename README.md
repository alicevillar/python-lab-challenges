# Python Lab Challenges
 
Solved Python Lab Challenges from CODIO platform (www.codio.com). These exercises were part of Module 1 (Launching into Computer Science") assignments of my MSc at the University of Essex, UK. 
  
 
## Summary 
* 1 Lists
* 2 Conditionals
* 3 Functions
* 4 Recursion


## 1. LISTS 

#### Lab Exercise 1

```
  Write a program that takes a list of integers called numbers and replaces each element greater than 10 with a '*'.
  Print the new version of numbers.
  => Expected Output:
  - If numbers = [30, 1, 20, 4] then you will print ['*', 1, '*', 4]
  - If numbers = [5, 9, 11, 23] then you will print [5, 9, '*', '*']
```
 | Lists: Exercise 1 | [Solution](https://github.com/alicevillar/Python_Lab_Challenges/blob/main/lists/lists_exercise1.py)   
 
#### Lab Exercise 2

```
  Write a program that takes a list called my_list (it could be a list of any data type) and prints the list three times if the length of the list is less than 5. 
  If the length of my_list is greater than or equal to 5, then print the list one time.
  Expected Output
  - If my_list = ['hi', 'hello'] then you will print ['hi', 'hello', 'hi', 'hello', 'hi', 'hello']
  - If my_list = [65, 111, 2, 81, 65, 32] then you will print [65, 111, 2, 81, 65, 32]
```
 | Lists: Exercise 2 | [Solution](https://github.com/alicevillar/Python_Lab_Challenges/blob/main/lists/lists_exercise2.py)   

#### Lab Exercise 3 
 
 ```
   Write a program that takes a list called strings that contains a random selection of strings.
   Your program should print the first string when arranged in alphabetical order.
   => Expected Output:
   - If strings = ['luck', 'cat', 'kid', 'house'] then you will print cat
   - If strings = ['duck', 'dddd', 'mouse', 'kite'] then you will print dddd
```
 | Lists: Exercise 3 | [Solution](https://github.com/alicevillar/Python_Lab_Challenges/blob/main/lists/lists_exercise3.py)   
 
 #### Lab Exercise 4 
 
 ```
 Write a program that takes a list called numbers that contains integers in a sequence
 (the sequence is always increasing, never decreasing).
 Your program should add the next two numbers in the sequence, and then print the list.
  => Expected Output:
  - If numbers = [1, 2, 3, 4] then you will print [1, 2, 3, 4, 5, 6]
  - If numbers = [-5, -4, -3, -2] then you will print [-5, -4, -3, -2, -1, 0]
```
  | Lists: Exercise 4 | [Solution](https://github.com/alicevillar/Python_Lab_Challenges/blob/main/lists/lists_exercise4.py)   

 #### Lab Exercise 5 
 
 ```
 Write a program that takes a list called numbers that has an even length.
 Your program should should insert an '*' between each element of the list. Then print the modified list.
 => Expected Output:
  - If numbers = [1, 2, 3, 4] then you will print: [1, '*', 2, '*', 3, '*', 4]
  - If numbers = [0, 0, 0, 0, 0, 0] then you will print: [0, '*', 0, '*', 0, '*', 0, '*', 0, '*', 0]
```
 | Lists: Exercise 5 | [Solution](https://github.com/alicevillar/Python_Lab_Challenges/blob/main/lists/lists_exercise5.py)   


## 2. CONDITIONALS 

#### Lab Exercise 1
 ```
  Use the variable x as you write this program. x will represent a positive integer. Write a program that determines if x is between 0 and 25 or between 75 and 100.
  If yes, print the message:_ is between 0 and 25 or 75 and 100, where the blank would be the value of x.
  The program should do nothing if the value of x does not fit into either range.
  => Expected Output:
  - If x is 8, then the output would be: 8 is between 0 and 25 or 75 and 100.
  - If x is 80, then the output would be: 80 is between 0 and 25 or 75 and 100.
  - If x is 50, then the output would be blank (your program does not print anything).
```
 | Conditionals: Exercise 1 | [Solution](https://github.com/alicevillar/Python_Lab_Challenges/blob/main/conditionals/conditionals_exercise1.py)   

 #### Lab Exercise 2
 ```
   Use the variable x as you write this program. x will represent a positive integer.
 
   Write a program that determines if x is divisible by 5.
   If yes, print _ is divisible by 5, where the blank is the value of x. If no, print _ is not divisible by 5,
   where the blank is the value of x.
   => Expected Output:
   - If x is 50, then the output would be: 50 is divisible by 5 and even.
   - If x is 37, then the output would be: 37 is not divisible by 5 or it is odd.
```
 | Conditionals: Exercise 2 | [Solution](https://github.com/alicevillar/Python_Lab_Challenges/blob/main/conditionals/conditionals_exercise2.py)   

 #### Lab Exercise 3

 ```
  Use the variable x as you write this program. x will represent a string.
  Write a program using the elif keyword  that determines if x is a primary color (red, blue, or yellow).
  If yes, print _ is primary color, where the blank is the value of x.
  If no, print _ is not a primary color, where the blank is the value of x.
  => Expected Output:
   - If x is red, then the output would be: red is a primary color.
   - If x is teal, then the output would be: teal is not a primary color.
```
 | Conditionals: Exercise 3 | [Solution](https://github.com/alicevillar/Python_Lab_Challenges/blob/main/conditionals/conditionals_exercise3.py)   
 
  #### Lab Exercise 4

 ```
   Use the variable x as you write this program. x will represent a string.
   Write a program that determines if x is a vowel (a, e, i, o, and u ).
   If yes, print _ is a vowel, where the blank is the value of x.
   If no, print _ is not a vowel, where the blank is the value of x.
   => Expected Output:
   - If x is a, then the output would be: a is a vowel.
   - If x is z, then the output would be: z is not a vowel.
```
  | Conditionals: Exercise 4 | [Solution](https://github.com/alicevillar/Python_Lab_Challenges/blob/main/conditionals/conditionals_exercise4.py)   

  #### Lab Challenge - Month of the Year

 ```
  Write a program that determines the month of the year based on the value of variable called month.
  The variable will be a number from 1 to 12 (1 is January, 2 is February, etc.).
  Use a print statement to write the month to the screen.
```
  | Conditionals: Lab Challenge | [Solution](https://github.com/alicevillar/Python_Lab_Challenges/blob/main/conditionals/conditionals_lab_challenge.py)   


## 3. FUNCTIONS 

#### Lab Exercise 1

 ```
  Write a function called avg that takes two parameters. Return the average of these two parameters.
  If the parameters are not numbers, return the string, Please use two numbers as parameters.
  => Expected Output
   - If the function call is avg(10,25), then the function would return 17.5
   - If the function call is avg(10, "cat"), then the function would return Please use two numbers as parameters
```
  | Functions: Exercise 1 | [Solution](https://github.com/alicevillar/Python_Lab_Challenges/blob/main/functions/functions_exercise1.py)   

#### Lab Exercise 2

 ```
  Write a function called odds_or_evens that takes a boolean and a list of integers as parameters.
  If the boolean parameter is True, return a list of only even numbers.
  If the boolean parameter is False, return a list of only odd numbers.
   Expected Output:
   - If the function call is odds_or_evens(True, [13, 22, 8, 31]), the the function would return [22, 8]
   - If the function call is odds_or_evens(False, [13, 22, 8, 31]), the the function would return [13, 31]
```
   | Functions: Exercise 2 | [Solution](https://github.com/alicevillar/Python_Lab_Challenges/blob/main/functions/functions_exercise2.py)   

#### Lab Exercise 3

 ```
  Write a function called search_list that takes a list and a search term as parameters.
  If the search term is located in the list, return the index of the matching element.
  The function should work even if there is a difference in capitalization.
  If the search term is not in the list, return -1.
  => Expected Output:
   - If the function call is search_list(["dog", "fish", "cat"], "Cat"), the the function would return 2
   - If the function call is search_list(["water", "Toy", "house"], "toy"), then the function would return 1
  - If the function call is search_list(["box", "car", "hat"], "mouse"), the the function would return -1
```
  | Functions: Exercise 3 | [Solution](https://github.com/alicevillar/Python_Lab_Challenges/blob/main/functions/functions_exercise3.py)   

#### Lab Exercise 4

 ```
  Write a function called is_palindrome that takes a string as a parameter.
  The function will return True if the string is a palindrome( is the same forward and backward).
  => Expected Output:
  - If the function call is is_palindrome("level"), the the function would return True
  - If the function call is is_palindrome("house"), the the function would return False
```
  | Functions: Exercise 4 | [Solution](https://github.com/alicevillar/Python_Lab_Challenges/blob/main/functions/functions_exercise4.py)   

## 4. RECURSION 

#### Lab Exercise 1

 ```
  Write a recursive function called recursive_power that takes two integers as parameters.
  The first parameter is the base and the second parameter is the exponent.
  Return the base parameter to the power of the exponent.
  => Expected Output
   - If the function call is recursive_power(5, 3), then the function would return 125
   - If the function call is recursive_power(4, 5), then the function would return 1024
```
  | Recursion: Exercise 1 | [Solution](https://github.com/alicevillar/Python_Lab_Challenges/blob/main/recursion/recursion_exercise1.py)   

