// //Lesson 8
// alert("Hello World!")


//Lessons 9-10
//const subject = "JavaScript";
//subject = "JavaScript";

// const age = 28

// const myAge = 31
// const $myFavoriteSubject = "JavaScript"
// const _studentScore = 29
// // const favoriteColor1 = "White"
// // const favoriteColor2 = "Red"

// //alert(subject)
// // alert(age)
// // alert($myFavoriteSubject)
// // alert(_studentScore)
// // alert(favoriteColor2)
// // alert(MYAGE) //wont run because of the case sensitive rule of JS

// //instead of using alerts to display our JS code we can use the browser console
// console.log(_studentScore)
// console.log(myAge)

// //Lesson 11: Three keywords for naming variables
// let age = 21
// age = 65

// var favoriteColor = 'Burgundy'
// favoriteColor = 'Teal'

// console.log(age)
// console.log(favoriteColor)

// //Lesson 12: Data Types
// const score = 49.6

// console.log(typeof(score))

// //Lesson 13: Primitive datatypes- Numbers & Strings
// const score = 15
// const totalScore = 20
// const percentageScore = (score / totalScore) * 100

// const name = 'Udeme'
// let favFood = 'Fried Rice'
// const sentence = "My name is " + name + " and my favorite food is " + favFood

// console.log(score + " marks")
// console.log("The student's percentage score is " + percentageScore + "%")
// console.log(sentence)
// console.log(sentence[3])

// //Task for lesson 13
// const day = 'Monday'
// const position = 1
// const output = 'Today is ' + day + '. ' + 'It is the ' + position + 'st day of the week.'

// console.log(output)

// //Lesson 14: Primitive datatypes- Boolean, null, undefined
// const isBritish = false
// const userDetails = null
// let country

// console.log(typeof(userDetails))
// console.log(country)

//Lesson 15: Operators- Assignment, Arithmetic
//Assignment operators are not the same as equality sign and this is the symbol for it = 
//Arithmetic operators symbols are addition (+), subtraction (-), division (/), multiplication (*), and modulus (%)

// //Lesson 16: Comparison operators- <, >, ==, ===, >=, <=
// const compare = 4 > 3
// const compareAnother = 5 < -5
// const compare3 = 5 >= 5
// const compare4 = 12 <= 4.5
// const equality = 12.0 == 12 //they are equal in value
// const equality2 = '2' == '3' //not equal in value 
// const strongEquality = 15.0 === '15'  //the value are equal but 1 is an integer while the other is a string
// const strongEquality2 = '1.25' === '1.52' // equal in type but not value
// const strongEquality3 = true === true
// const notAnumber = 4 * 'eggs'
// const age = 11
// const age1 = 11

// console.log(compare)
// console.log(compareAnother)
// console.log(compare3)
// console.log(compare4)
// console.log(equality)
// console.log(equality2)
// console.log(strongEquality)
// console.log(strongEquality2)
// console.log(strongEquality3)
// console.log(notAnumber)
// console.log(15 >= age)
// console.log(age1 >= age)

// //Lesson 17: Logical operators &&, ||, !
// const userName = 'Victory'
// const age = 12
// //const logic = age === 12 && userName === 'Victory' //its TRUE if both sides of the expression is true
// const logic = age === '12' || userName === 'Victory' //Its TRUE if 1 of both sides is true
// const logic2 = age === '12' || userName === 'Victory1' // False because both expressions are false

// console.log(logic)
// console.log(!logic2)  /* because the Not operator ! is placed infront of the variable, the answer of the express which should be false os now true. 
//                       it because the opposite of the actual answer.i.e not false = true */

//Lesson 18: Conditional Statements
//IF Statements
// const age = 21

// if(age >= 18) {
//     console.log('Congratulations! You are eligible to vote.')
// }

// //IF- Else statement
// const age = 21

// if(age >= 18) {
//     console.log('Congratulations! You are eligible to vote.')
// } else {
//     console.log('You are too young to vote.')
// }

// //Lesson 19: if..else..if statements
// const age = 79

// if(age >= 18 && age <= 65){
//     console.log('You are eligible to vote!')
// } else if(age > 65){
//     console.log('You are too old to vote!')
// } else{
//     console.log('You are too young to vote!')
// }

// //Task 6(New)
// const side1 = 6
// const side2 = 2
// const side3 = 2

// if(side1 === side2 && side2 === side3 && side1 === side3){
//     console.log('Equilateral triangle')
// }else if(side1 === side2 || side2 === side3 || side1 === side3){
//     console.log('Isosceles triangle')
// }else{
//     console.log('Scalene triangle')
// }

// //Lesson 20: Switch statements
// switch case statements are used for problems that require multiple if else if statements
// const day = 'Tuesday'

// switch(day){
//     case 'Friday':
//         console.log('TGIF!')
//         break
//     case 'Saturday':
//         console.log('Yeh! The weekend is here')
//         break
//     case 'Sunday':
//         console.log('Happy Sunday!')
//         break
//     default:
//         console.log('Go to work')
// }


// //Lesson 21: LOOPS: While loops
// //The syntax of while loop is made up of 3 things: the starting value, the condition for when to stop & a way to get to the next iteration
// let star = 1  //starting point

// while(star <= 100){                 // condition for when to stop
//     if(star === 1){
//         console.log(star + ' star')
//     }else{
//         console.log(star + ' stars')
//     }
//     star = star + 1   //way to get to the next iteration
// }

//Lesson 22: For loops 
// Its syntax has the same 3 content as for while loop but in this case all the 3 elements
// are writing on the same line after the 'for' keyword
// for(let star = 0; star <=10; star = star + 1){
//     if(star === 1 || star === 0){
//         console.log(star + ' star')
//     }else{
//         console.log(star + ' stars')
//     }
    
// }

// for(let number = 0; number <=10; number = number + 1){
//     if(number % 2 === 0){
//         console.log(number + ' is an even number')
//     }else{
//         console.log(number + ' is an odd number')
//     }
    
// }

// for(let star = 0; star <=10; star = star + 1){
//         switch(star){
//             case 0 || 1:
//                 console.log(star + ' star')
//                 break
//             // case 1:
//             //     console.log(star + ' star')
//             //     break
//             default:
//                 console.log(star + ' stars')

//         }
        
// }

// for(let star = 1; star <=10; star = star + 1){
//     if(star === 1){
//         console.log(star + ' Star')
//     }else{
//         console.log(star + ' Stars')
//     }
// }

// // Task 6: show the odd numbers between 1-20 using for loop
// for(let number = 0; number <= 20; number = number + 1){
//     if(number % 2 !== 0){
//         console.log(number + " is an odd number")
//     }
// }

//Lesson 23: Functions
// function MyFunction(){  //function declaration
//     console.log('My first function')
// }

// MyFunction(); //Function call

// function greetings(name){
//     console.log("Good morning, " + name)
// }

// greetings("Ben")

// function addNumbers(firstNumber, secondNumber){
//     const sum = firstNumber + secondNumber;
//     console.log(sum);
// }
// addNumbers(30, 40)

//Lesson 24: Functions 2; Return value
// function addNumbers(firstNumber, secondNumber){
//     const sum = firstNumber + secondNumber;
//     return(sum)
// }
// const moreOp = addNumbers(13.3, 10.5) + 20
// //console.log(moreOp) OR writen as below
// console.log(addNumbers(13.3, 10.5) + 20)

//We use arrays when we want to return multiple values
// function addNumbers(firstNumber, secondNumber){
//     const sum = firstNumber + secondNumber;
//     const product = firstNumber * secondNumber
//     return[sum, product]
// }
// console.log(addNumbers(3, 5))

// function converter(dollars){
//     //assuming the naira to dollar rate is 410 : 1
//     const naira = dollars * 410;
//     return naira;
// }
// nairaValue = converter(20);
// console.log(nairaValue);

// //Exercise given within the lesson: Write a function to convert celsius to farenheit
// //formula for conversion is (celsius * 1.8) + 32 = fahrenheit
// function tempconverter(celsius){
//     const fahrenheit = (celsius * 1.8) + 32;
//     return fahrenheit;
// }
// const fahrenheitValue = tempconverter(36);
// console.log(fahrenheitValue);

// //Task 7: Area of a rectangle
// //formula of area of rectangle is Lenght * width
// function area(lenght, width){
//     const areaOfRectangle = lenght * width;
//     return areaOfRectangle;
// }
// rectangleArea = area(9,4)
// console.log(rectangleArea);

//Lesson 25: Scope
// Global scope are variables that can be accessed anywhere in the code  and not restricted to a function. 
//Its usually bad coding practice
// const myName = "Ben"  // an example of a global scope variable

// function greetings(){
//     console.log("Goodmorning " + myName)
// }
// greetings();

// //Function scope are variables that are accessed only within the function its assigned to. 
// //We can also have a function within a function
// function greet(){
//     const myName = "Ben"  // an example of a function scope variable
//     console.log("Goodmorning " + myName)
// }
// greet();

// function anothergreet(){      // the variable myName is out of scope in this function (another greet) & cant be called
//     console.log('Good evening ' + myName)
// }
// anothergreet();

// //You can call a function scope variable for functions within a function
// function greet(){
//     const myName = "Ben"  // an example of a function scope variable
//     console.log("Goodmorning " + myName)
//     function innergreet(){      // an example of a function within a function
//         console.log('Good evening ' + myName)
//     }
//     innergreet();
// }
// greet();

// //Lesson 26: Function Expression
// //Functions can be declared (accessed anywhere in code due to hoisting) or expressed (accessed only after being initialised)
// function greet(name){  //declared function
//     console.log('Hello ' + name)
// }
// greet("Nick");

// const myGreet = function (name){  //expressed function
//     console.log('Hello ' + name)
// }
// myGreet("Ned")

// //Lesson 27: Callback functions
// //callback function is a function that is passed into another function as an argument (value of the input)
// //Method 1 of using call back
// function greeting(greet){
//     greet();
// }

// greeting(function(){
//     console.log("Good morning")
// })

// //Method 2 of using callback. This method is much neater
// function greeting(greet){
//     greet();
// }

// function callback(){
//     console.log("Good evening")
// }

// greeting(callback);

// //Lesson 28: Intro to Array
// const myArray = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
// const numArray = [ 1, 2, 5]
// const emptyArray = []

// console.log(myArray.length)
// console.log(numArray)
// console.log(emptyArray)

// //Lesson 29: Assessing elements of an array
// const myWeekArray = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
// const thirdElement = myWeekArray[2]
// myWeekArray[2] = 20

// const emptyArray = []
// emptyArray[0] = 'first element'
// emptyArray[1] = 'second element'
// emptyArray[2] = 'third element'
// emptyArray[4] = 'fifth element'

// console.log(myWeekArray)
// console.log(myWeekArray[10])
// console.log(thirdElement)
// console.log(emptyArray)

// //task 9
// const friends = ['Onene', 'Tayo', 'Peju', 'Becky', 'Eno']
// const bestFriend = friends[4]

// console.log(friends)
// console.log(bestFriend)

//Lesson 30: array methods: Pop and push
//pop removes the last element in the array while push is used to add the last element to the array

// const emptyArray = []
// const notEmpty = ['Monday', 'Tuesday', 'Wednesday']

// emptyArray.push('First element', 'Second element', true, 341, null)
// notEmpty.push('Thursday', undefined)
// console.log(emptyArray)
// console.log(notEmpty)

// const weekDays = ['Monday', 'Tuesday', 'Wednesday']

// weekDays.pop()
// weekDays.pop()
// weekDays.pop()
// console.log(weekDays)

//Lesson 31: unshift and shift
//unshift is similar to push but adds to the beginning of the array while shift, just like pop removed from the beginning of the array

// const breakfastItems = ['tea', 'bread', 'butter', 'eggs']

// //breakfastItems.unshift('coffee', 'water')
// breakfastItems.shift()
// console.log(breakfastItems)

//Lesson 32: Slice method
//slice method allows us to remove elememts from any other place in the array apart from the front of back
// we can remove any number of elements from the array. 
//It contains 2 arguments: start index & end index (last element excluded)

// const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

// const som = months.slice(2, 5)
// const neg = months.slice(0, -3)
// //console.log(months.slice(2, 5))
// console.log(som)
// console.log(neg)
// //Exercise: show April - August and August - Dec
// const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

// const firstExercise = months.slice(3, 8)  //April - August
// const firstExerciseAnotherMethod = months.slice(3, -4)
// const secondExercise = months.slice(7, 13)  //August - Dec

// console.log(firstExercise)
// console.log(firstExerciseAnotherMethod)
// console.log(secondExercise)

//Lesson 32: Splice Method
// This method modifies the original array and can have between 2-3 arguments
//first argument is start index, 2nd is number of elements to be removed, 3rd (optional) is the elements to be added
// const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

// console.log(months, months.splice(3, 9))  //This allows us log multiple (2)results on console at once 
// console.log(months, months.splice(2, 0, 'My custom month'))
//exercise
//  const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
// // //remove jan-march
//  console.log(months.splice(0,3))
// //month.splice(4,2) a) what does it return b)what's the modified value
// console.log(months.splice(4,2), months)


// //Excerpts from live session: Arrow function side note
// const greeting = () => {
//     console.log('Good evening')
// }
// greeting();

// //non arrow function AKA Anonymous function
// function greet(){
//     console.log('good evening')
// }
// greet();

//LESSON 33: indexOf and lastIndexOf
// const months = ['Apr', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

// console.log(months.indexOf('Aug'))
// console.log(months.indexOf('Monday')) //None existing number in the array returns -1
// console.log(months.indexOf('Apr')) //multiple occurrences of an element will return index of the first occurence
// console.log(months.lastIndexOf('Apr')) //gives the last index of a multiple occurring element

// //Lesson 35: Intro to Objects
// const myObject = {name: 'CAR', color: 'Pink', price: 2500000}
// const door ={
//     isOpen: false,
//     material: 'wood',
//     height: 15
// }

// //2 ways of accessing the property of objects: Dot notation and bracket notation
// //Dot notation syntax is console.log(variable name.key)
// console.log(door.material)
// console.log(myObject.price)

// //Bracket notation syntax is console.log(variable name('key'))
// console.log(door('isOpen'))

//Task12: Write an object literal for books
// const books = {
//     title: 'Peter Pan',
//     description: 'A story book for children',
//     numberOfPages: 56,
//     author: 'William Mcguire',
//     reading: true
// }


// //Lesson 36: Object Methods
// //when the value of an object's key is a function, then we call it a Method
// const myObject = {name: 'CAR', color: 'Pink', price: 2500000}
// const door ={
//     isOpen: false,
//     material: 'wood',
//     height: 15,
//     toggleOpenAndClose: function(){
//         if(door.isOpen === true){
//             door.isOpen = false
//         }else{
//             door.isOpen = true
//         } 
//     }
// }
// door.toggleOpenAndClose()
// console.log(door.isOpen)

// const person = {
//     name: 'Nick',
//     age: 34,
//     siblings: ['Richard', 'Wendy', 'Ken'],
//     addSibling: function(name){
//         person.siblings.push(name)
//     }
// }
// person.addSibling('Henry')
// person.hairColor = 'Black' // dynamic way of adding a new parameter to an object
// console.log(person)

//Task 13 
// const books = {
//     title: 'Peter Pan',
//     description: 'A storybook for kids',
//     numberOfPages: 35,
//     author: 'William Gerround',
//     reading: true,
//     toggleReadingStatus: function (){
//         if(books.reading === false){
//             books.reading = true
//         }else{
//             books.reading = true
//         }
//     }
// }
// books.toggleReadingStatus()
// console.log(books.reading)

// //Lesson 37: Complex Data Structure
// const person = {
//     name: 'Nick',
//     age: 34,
//     siblings: [
//         {
//             name: 'Richard',
//             age: 30
//         },
//         {
//             name: 'Wendy',
//             age: 29
//         },
//         {
//             name: 'Ken',
//             age: 23
//         }
//     ],
//     addSibling: function(name){
//         person.siblings.push(name)
//     }
// }
// person.addSibling({
//     name: 'Henry',
//     age: 10
// })
// person.hairColor = 'Black' // dynamic way of adding a new parameter to an object
// console.log(person)

//Task 14
// const books = [
//         {
//             title: 'Peter Pan',
//             description: 'Storybook',
//             numberOfPages: 12,
//             author: "William murphy",
//             reading: false
//         },
//         {
//             title: 'Famous 5',
//             description: 'Adventure',
//             numberOfPages: 15,
//             author: "Benjamin Thomas",
//             reading: true
//         },
//         {
//             title: 'Gulliver travel',
//             description: 'Mystery',
//             numberOfPages: 32,
//             author: 'Gordon Brown',
//             reading: true
//         },
//         {
//             title: 'Book of Moses',
//             description: 'Religious',
//             numberOfPages: 19,
//             author: 'Moses Peter',
//             reading: false
//         }
//     ]
//     for(let i = 0; i<= books.length; i++){
//         if(books[i].reading === true){
//             console.log(books[i])
//         }
//     }



// //Lesson 38: JSON (Javascript Object Notation)
// const myObject = {
//     name: 'Vehicle',
//     type: 'car',
//     color: 'black'    
// }
// const json = JSON.stringify(myObject) //this converts a regular js object to JSON
// console.log(json)

// JSON.parse(json)  // this is used to convert JSON to regular js object 
// console.log(JSON.parse(json))

//Lesson 42:Intro to node js
// node js is js on the server. 
//create an empty project on desktop and open in vscode
//initiate node js (npm init) in terminal and a package.json file will be created
//create a new file within your project and give the same name as the entry point (main)in your package.json file eg index.js
//write your js code within this file
//type node <name of the js file> to run the code in terminal

