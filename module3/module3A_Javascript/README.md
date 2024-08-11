# JS_Testify

This is a repository containing the notes from lessons learned during testify's JS course in TAS.
It also has slack integrations to my TAS private channel and the task-review channels (CICD task on JS)

It also has the webhook set for github on the public ip (accessible over the internet) hosted on digital ocean http://68.183.240.181:8080/

## Lesson 6
Statically typed programming languages are those whose type checks (errors, variables etc) are known at compile time(i.e before the program runs) while dynamically types languages are those whose checks are done at runtime. 
Examples of statically typed languages are Typescript, Java,C, C++ 
Examples of dynamically typed languages are Javascript, Python,PHP, Ruby, Perl

Javascript flavors
- Browser
- Server (Node js)
- Database (MongoDB)
- Desktop (electron)
- Mobile app (React Native)

## Lesson 8
install the following extensions on vs code: live server & emmet live
.js is the extension used for javascript files. HTMLis used to bring the js files to life on a browser which explain why 2 files are created.
An app.js file (for writing your js code) and an index.html file (for displaying this code on a browser). The emmet live extension helps with starter code (i.e a html boiler plate code when ! is entered into an html file).
Within the body of the html boiler plate, include a script tag <script></script>. 
There are 3 ways to write js code in the html file;
1. For external files include the link to the external file within the script tag i.e <script>src="link_to_external_file"</script> 
2. For js files within the same project folder containing the html files, use <script>src="name_of_js_file"</script>
3. Lastly, we can write the JS code directly in the script tag of the html file

To launch the js code on browser, right-click within the html file & click on live-server https://monosnap.com/file/pOx4ufNhfsU9GB4n8elav1MSoZ1P93

## Lesson 9: Variables
Variables are containers tha store values in the computer memory. Variables can declared and assigned a value. 
A variable that is declared without assigning a value is like an empty box. JS assigns it a default value of 'undefined'
Syntax of variables: <Variable_keyword> <variable_name> or  <keyword> <variable_name> <operator> <value>
variable keywords are : const(values are not subject to change), var(old method of naming variables, values are subject to change), let(values are subject to change)
eg const subject;  // declared variable
const subject = "Chemistry" // declared & assigned variable

## Lesson 10: Naming Variables
Rules for naming variables
1. Must not start with a number but can contain a number
2. Can start with _ or $
3. Must not contain - 
4. Is case sensitive

Best Practice
1. variables should be descriptive of the values they hold
2. Written in camel case

## Lesson 13: Data types
1. Primitive Data types: String, Number(Integers & float), Boolean, Null, Undefined, NAN
2. Composite Data types: Arrays, Functions, Objects