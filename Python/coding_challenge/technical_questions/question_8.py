# Create a program that prints out the even numbers in an array.
# Sample array:
# a. [1, 2, 3, 4, 5, 6]
# b. [ 34, 2, 9, 91, 19,401, 0 ]

def print_even_numbers(array_of_nums):

    for array_of_num in array_of_nums:
        if array_of_num % 2 == 0 and array_of_num != 0:
            print("This number " + str(array_of_num) + " " + "is an even number")


print_even_numbers([1, 2, 3, 4, 5, 6])
print_even_numbers([ 34, 2, 9, 91, 19,401, 0 ])