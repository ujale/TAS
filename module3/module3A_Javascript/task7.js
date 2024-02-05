//Module 2, Task 6: Using for loop, show all the odd numbers between 1-20
/* Write a Javascript program that checks if a given number, number is odd or even. 

If the number is odd, print to the console: number is odd. If  the number is even, print to the console: number is even 

Hint: An even number is divisible by 2. Hence, for an even number, the expression, 
number % 2 === 0 will evaluate to true

Steps

Initialize a variable, number and assign it any number of your choice.

Write an if statement check if number is divisible by 2 (HINT: use the modulus operator)

Log the string number is even to the console if the number is divisible by 2

Add an else block

Inside the else block, log number is even to the console

You can test your code by assigning different values to the number variable in step 1 
*/

for(let number = 0; number <= 20; number = number + 1){
    if(number % 2 !== 0){
        console.log(number + " is an odd number")
    }
}
