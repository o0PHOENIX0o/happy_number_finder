# happy_number_finder
Finding the given number is a happy number or not using recursion method in python (including error handling)

a happy number is a number which eventually reaches 1 when replaced by the sum of the square of each digit.
for example 10,13,17,etc

process: let given number = 13
                          
                 {1}^2 + {3}^2 or (1*1 + 3*3)
                  ans = 10
                           again
                 {1}^2 + {0}^2  or (1*1 + 0*0)
                  ans = 1    
                     hence 13 is a happy number
