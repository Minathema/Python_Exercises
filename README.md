Just some exercises based on practicepython.org

#100_years_old

Asks for the user's name and age, and for a random number.
Then prints "(name) you will turn 100 years old in the year (year))" ,
where (name) is the user's name and (year) is the calculated year when they will turn 100 years old.
This prints as many times as the random number which the user picked.



#even_odd_divide

Firstly requests a number and checks whether it is even or odd, and if it is a multiple of 4.
Then it requests two numbers and checks if the second number divides evenly into the first one.
In all cases above, an appropriate message is printed.



#less_than_number

There is a given list   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
Firstly the script prints all the elements of the list that are less than 5.
Then it requests a number and prints a new list with the elements of the list a that are less than that number.



#divisors

Requests a number, then prints all the divisors of that number.



#list_overlap

Firstly generates two lists that are randomly selected to have from 5 to 20 elements.
Those elements are randomly selected numbers from 1 to 50.
Then prints a list of the elements that the two lists have in common after the quote 'The common numbers are:' .
If there are no common numbers, it prints 'There are no common numbers' .



#palindrome

Requests a sentence, then prints whether it is a palindrome or not.



#even_numbers

There is a given list a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
It prints a new list containing the even numbers of the list a .



#rock_paper_scissors

A simple game of Rock-Paper-Scissors.
It requests a number of rounds.
For each round, firstly Player 1 and then Player 2 take their pick. For each round, the console prints who wins.
When all rounds have taken place, the console prints which player had the most wins and therefore wins the game.
It is also possible that the game ends in a draw.
Lastly, the game asks if the players would like to start another game. If "yes", the same process begins, otherwise the console prints "End of Game" and the game stops.



#guess_number

Generates a random number from 1 to 9.
Firstly, prints 'You can stop the game by typing "exit"'
Then requests that the user guesses the secret number. Then prints if that number is lower or higher than the secret number and asks for another guess.
The game ends when the user finds the secret number -and prints an appropriate message- or when the user types "exit".
When the game ends, it also prints the number of guesses that the user took.



#prime_number

Requests a number, then prints if that number is prime or not.



#list_start_end

A list a = [12,25,53,94,5,26] is passed as argument.
Prints a new list containing the first and last elements of the list a.



#fibonacci

Asks the user how many numbers of the Fibonacci sequence they would like, then prints them.



#remove_duplicates

Generates a list of 20 random numbers ranging from 0 to 40.
Then prints another list containing the elements of the first one, minus the duplicates.



#reverse_word_order

Requests a phrase, then prints the words of that phrase in reverse order.



#password_generator

Prints that the new password should contain at least 4 characters.
Then requests the number of characters that the user wants, until that number is equal to or higher than 4.
Generates and prints the new password, after it makes sure that it contains at least 1/4 symbols, 1/4 lower letters, 1/4 capital letters and 1/4 numbers.



#cows_and_bulls

A game of Cows and Bulls.
Firstly prints a welcome message, then generates a random 4 digit number and asks the user to guess it.
For every right number in the right position, it prints 1 cow.
For every right number in the wrong position, it prints 1 bull.
The game ends when the users guesses the correct number. An appropriate message is printed, along with the number of guesses that the user took.



#binary_search

Two arguments are passed, the_list = [2,5,6,7,8,9,10,11,13,14,15]  and  num = 13
Uses binary search to check whether num is on the_list or not and prints the result in the form of a boolean.
