# Lesson3: String & concatenation

# Escape sequence eg \', \", \n, \t, \v, \\, \b, \r

article = "This is an article\na multiline article\n\t the period will be removed from this line.\b\n I want to see what this sequence does\r"
print(article)

# Raw string
anotherArticle = r"This is an article\na multiline article\n\t the period will be removed from this line.\b\n "
print(anotherArticle)

# Concatenation
group = "wood"
attr = "pecker"
bird = group + attr
print(bird)

# Lesson 4: Basic Arithmetic Operators
print('Arithmetic operators\n') # They are + - / * ** // %
result = 4 + 6
print(result)

result = 10 / 2
print(result)

result = 10 % 5
print(result)

result = 10 ** 3
print(result)

result = 10 // 5
print(result)

print('Compound operators\n') # They are += -= /= *= **= //=

result = 4
result += 3
print(result)

result = 4
result -= 3
print(result)

result = 4
result *= 3
print(result)

result = 4
result /= 2
print(result)

result = 4
result %= 3
print(result)

result = 4
result **= 3
print(result)

result = 4
result //= 3
print(result)

# Lesson 5: Conditional and Relational operators
# Conditional operators: if, if else and elif
# Relational operators are also known as comparison operators: <, >, <=, >=, ==, !=
print("if statement\n")
age = 10

if age == 10:
    print("You are young")

print("if-else statement\n")
age = 20
if age <= 10:
    print("You are young")
else:
    print("You are not too young")

print("elif statement\n")
age = 20
if age <= 10:
    print("You are too young")
elif age == 18:
    print("You can vote")
elif age == 12:
    print("You are now a teen")
elif age != 12:
    print("You are not 12 years")
else:
    print("You are not too young")

# lesson 6: Conditional and logical operators
print("\nLogical operators are \n: and , or, not")

# lesson 7: Loops( For and while loops)

print('\nFor loop')
# iterate sequence
fruits = ["Apples", "Mango", "pear"]
for fruit in fruits:
    print("Fruit:", fruit)

# another example
name = "python"
for ch in name:
    print("character", ch)

# iterate number
number = 5
for i in range(number):
    print("number", i)


# while loop
print("\n While loop\n")
number = 10

while number > 0:
    print("Number is:", number)
    number -= 1

# Lesson 8: Break, Continue and Else statements
print("\n Break\n")

number = 5
for i in range(number):
    if i == 3:
        break
    print("for: Number", i)

print("\nanother method with the variable directly & not its index\n")
for number in range(number):
    if number == 3:
        break
    print("for: Number", number)

while number > 0:
    if number == 3:
        break
    print("while: Number:", number)
    number -= 1


print("\ncontinue\n")
number = 5
for i in range(number):
    if i == 3:
        continue
    print("for: Number", i)

while number > 0:
    if number == 3:
        number -= 1
        continue
    print("while: Number:", number)
    number -= 1

print("\n else statement and continue\n")

number = 10
for i in range(number):
    if i == 3:
        continue
    print("for: Number", i)
else:
    print("end of loop")

while number > 0:
    if number == 3:
        number -= 1
        continue
    print("while: Number:", number)
    number -= 1
else:
    print("end of loop")


print("\n else statement and break\n")

number = 10
for i in range(number):
    if i == 3:
        break
    print("for: Number", i)
else:
    print("end of loop")

while number > 0:
    if number == 3:
        number -= 1
        break
    print("while: Number:", number)
    number -= 1
else:
    print("end of loop")