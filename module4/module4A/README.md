## Getting Started

Welcome to the VS Code Java world. Here is a guideline to help you get started to write Java code in Visual Studio Code.

## Folder Structure

The workspace contains two folders by default, where:

- `src`: the folder to maintain sources
- `lib`: the folder to maintain dependencies

Meanwhile, the compiled output files will be generated in the `bin` folder by default.

> If you want to customize the folder structure, open `.vscode/settings.json` and update the related settings there.

## Dependency Management

The `JAVA PROJECTS` view allows you to manage your dependencies. More details can be found [here](https://github.com/microsoft/vscode-java-dependency#manage-dependencies).


# Java PL Notes
## Lesson 3
Notes:
- type main+enter to generate the public static void main(String[] args{}
- type sout+enter to generate System.out.println(newString);

package Task;

public class StringAndConcat {

    public static void main(String[] args) {
        // String and string concat

        String bird = "hummingbird";
        String adjective = " is a beautiful bird";
        String newString = (bird + adjective);
        
        System.out.println(newString);

        //String and primitive concat
        String movieName  = "matrix";
        int parts = 4;
        boolean isReleased = false;

        System.out.println(movieName + ":" + parts + isReleased);

        //.concat() method
        movieName.concat(parts + "");

        System.out.println(movieName.concat(parts + ""));

    }
}
## Lesson 4
- Basic Arithmetic Operator: +, -, *, /
- Incremental/decremental Operator: ++,--
- Compound Assignment Operators: +=, -=, /+, *=
Eg of basic operators

package Task;

public class Task1 {

    public static void main(String[] args) {
        double age = 20
        double age1 = 30
    
	    System.out.println(age/age1);

        //incremental/decremental
        age++ //20+1 = 21

        //compound assignment operator 
        age += age1
        System.out.println(age);
    }
}

## Lesson 5
- Conditional, Relational & Logical Statements
- Conditional Statements: If, else, elseIf, switch
- Relational Operators: ==, !=, <, >, <=, >=
- Logical operators: logical AND (&&), logical OR(||), logical(!)

## Lesson 6
- String Operations: lowercase, uppercase,
String word = "orGaniZation"

To convert a string to lowercase use the syntax: var.toLowerCase 
i.e System.out.println(word.toLowerCase());

To get the length of a string: System.out.println(word.length())

To get the index: System.out.println(word.indexOf("G"))

To get the char of an index: System.out.println(word.charAt(6));

To slice out a part of a string (substring): System.out.println(word.substring(0,5));
// This will produce the word "orGan" as 0, indicates the starting index & 5 indicates the index to avoid. i.e stop at the index before it which is 4

System.out.println(word.charAt(word.lenght()-1)); // Answer is 'n'

## Lesson 7: Arrays
- When declaring an array, the size of the array is fixed
- ArrayList: In arraylists the size of the array can be adjusted (added or removed)


package Task;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;

public class Task7 {
    public static void main(String[] args) {
        int [] array1 = new int [5];
        array1[0] = 10;
        array1[1] = 5;
        array1[4] = 4;

        System.out.println(Arrays.toString(array1));

        String [] fruits = {"Mango", "Orange", "Pear"};

        System.out.println(Arrays.toString(fruits));

        int [] [] doubleDimension = new int [2] [3];
        doubleDimension [0] [0] = 20;
        doubleDimension [0] [1] = 30;

        System.out.println(Arrays.deepToString(doubleDimension));
        
    }
}


## Lesson 8: Scanner Class 
Scanner class is used to read Java user input of primitive datatype like double, string, int,etc. To create an object in the scanner class we use the predefined object 'System.in'.
To read numerical values of a certain data type, the function to be used is nextDT()
So for next integer use: nextInt()
for strings : nextLine()

public class Lesson8 {
    public static void main(String[] args) {
        Scanner userInput = new Scanner(System.in);
        System.out.println("Welcome. Kindly enter your year of birth.");
        short dob = userInput.nextShort();
        short presentYear = 2023;
        int customerAge = presentYear - dob;
        System.out.println("You are " + customerAge + "years old");

        if (customerAge < 18) {
        System.out.println("You are too young to bet");
        } else if(customerAge >= 18){
        System.out.println("Welcome! You are qualified");
        }

    }

}
## Lesson 9A: Loops
Used to execute statements repeatedly until boolean is false. 
Types of loops are for loop (fixed iterations), while loop(non-fixed iterations), do-While loop(non-fixed iterations).

For loop has 2 syntax. 
syntax 1 is: for(initializing statement;testing condition;increment/decrement){
    //code to be executed
}
Syntax 2 which is used for the for each loop:
for (<datatype> <variable name>:<collectionname>){
    //statements:
}
Example 

public class Lesson9A {
    public static void main(String[] args) {
        // for increment
        for (int i = 0; i < 10; i ++){
            System.out.println("Student " + i);
        }


        // for decrement
        for (int i = 10; i > 0; i --){
            System.out.println("Student " + i);
        }
    }
}

## Lesson 9B: While & do-while loop

while loop is recommended when loop count is not fixed
do-while is recommended when the loop is to run at least once

public class Lesson9B {
    public static void main(String[] args) {
        // // while loop
        // Scanner scanner = new Scanner(System.in);
        // String userInput = "";

        // while(!userInput.equalsIgnoreCase("exit")){
        //     System.out.println("Welcome! type \"exit\" to exit this loop");
        //     userInput = scanner.nextLine();
        // }

        // //while loop with continue & break statement
        // Scanner scanner = new Scanner(System.in);
        // String userInput = "";

        // while(true){
        //     if(!userInput.equalsIgnoreCase("exit")){
        //     System.out.println("Welcome! type \"exit\" to exit this loop");
        //     userInput = scanner.nextLine();
        //     continue;
        //     }else if(userInput.equalsIgnoreCase("exit")){
        //         System.out.println("You are out of the loop");
        //         break;
        //     }
        // }

        String userInput;
        // do while loop
        do{
            System.out.println("Welcome! type \"exit\" to exit this loop");
            Scanner scanner = new Scanner(System.in);
            userInput = scanner.nextLine();
        } while(!userInput.equalsIgnoreCase("exit"));
    }
}

## Lesson 10: Java Methods
A method is a block of statement that has a name and return value.
It can be executed by calling (aka invoking)it from other places in the program
or by using annotations like in webautomation using TestNG.

There are 2 types of methods:
- Predefined methods: these are methods that are already defined in java class libraries
They are also known as in-built methods or standard library methods. 
eg length(), equals(), sqrt(), compareTo() etc
- User defined methods: method written by the programmer 

Structure of a method is: <access modifier> <return type> <name of the method>
(parameters){
    code to be executed
}

eg <access modifier> eg public   
<return type> eg void
<name of the method> eg main
(parameters) eg (String[] args)

public void myFullName (){
    System.out.println("My name is Shakespeare");
}

public void myAge (){
    System.out.println("I am 10 years old");
}

- methods start with small letters while classes start with capital letter
- In the main method, you need to create a method of the class to be able to access the properties of the class 
- Some methods do not have return values and so we use void to denote those. eg 
package Task;


public class Lesson10 {
    public static void main(String[] args) {
        //To access the properties of a class, we create an object of the class

        Lesson10 methodVar = new Lesson10();
        methodVar.printName();  // Invoke the method printName
        methodVar.myAge();     // Invoke the method printName
        int userAge = methodVar.ageCalculator(2000, 2023);
        System.out.println(userAge);
        
    }

    public void printName(){
        System.out.println("My name is Shakepeare");
    }

    public void myAge(){
        System.out.println("I am 10 years old");
    }
    public int ageCalculator(int dob, int presentYear){
        int age = presentYear - dob ;
        return age;  // we dont use 'void' for this clas since we have a return value
    }
}

- Methods with return values will make use of parameters to pass dynamic values and the keyword return. For such methods no return type of 'void' is not used 
eg the ageCalculator method above

## Lesson 11: Object Oriented Paradigm
- OOP is a paradigmn that makes use of the concept of classes and methods that structure software programs into simple, re-useable blocks of codes (classes) which is used to create individual instances of objects.
- The building blocks of OOP are COAM: classes, objects, attributes, methods
- Object: Single instance of a class
- 4 principles of OOP: Inheritance Encapsulation, Polymorphism, Abstraction
Inheritance" Child class inherits data and information from parent class
Encapsulation: Exposing only some information in the object
Abstraction: Exposing high level public methods for accessing an objects
Polymorphism: when many methods can do the same tasks, therefore allowing it take different forms

## Lesson 12: Access Level Modifiers
- Access level modifiers help restrict the scope of a class, constructor, variable, method or data member. They determine if other classes can use the fields or invoke a method
- 4 types of access modifiers: public, protected, default(no keyword required), private
- Public access modifiers have no restrictions
- Protected access modifiers the methods and data members are only accessible on the package level or by the subclasses of another package when inherited
- Default access modifier is when no access modifier is declared. The class,method, data member (just like protected access modifier)apply only within the same package
- Private access modifier have the accessible only within the specified class
- Classes are only available when the modifiers are either public or default
https://prnt.sc/5iEaXpG6U-Fq

## Lesson 13: Java Constructor
- A constructor is a special method that is called when an object is instantiated (the 'new' keyword is used)
- Structure of a constructure: public ClassName(parameter-list){
    Statements
}
- Constructors are methods without return value eg 'Void'
- We use the 'this' keyword when referencing a global variable that is of the same spelling as the parameter being passed in the constructor. Eg
 public class Human {
    
    String firstName;  // global variable

    public Human(String firstName){
        this.firstName = firstName;    //firstName in GV is same as that passed in params
    }                              //firstName of the left refers to the GV while                          //that on the right of the = refers to the class variable

}

if the variable names were different, then no need for 'this' keyword. i.e
public class Human {
    
    String fName;  // global variable


public Human(String firstName){
        fName = firstName;    
    }

## Lesson 14: Encapsulation
- This is the process of wrapping data and code as a single unit and making them private such that no external class can access it without using a public method. We can use setters & getters to access those hidden data

## Lesson 15: Inheritance
- The process by which 1 class acquires the properties and functionalities of another class. The child class uses the keyword 'extends' to implement inheritance.
- Types of inheritance:
Single inheritance (1-1 parent/child relationship),
Multilevels inheritance(father extends to child1 which extends to child2 i.e father-son-grandson)
Hierarchical inheritance: this is when more than 1 class extends the parent class
Multiple inheritance: This is when 1 child class extends more than 1 parent class. THIS TYPE OF INHERITANCE IS NOT SUPPORTED IN JAVA

## Lesson 16: Polymorphism
- Method overloading: A feature that allows a class have the same name if their parameter list is different.
Eg method add(int a, int b) and method add(int a, int b, int c)
- Ways to overload:
1. Number of parameters: add(int a, int b) and add(int a, int b, int c)
2. Datatype: add(int a, int b) and add(int a, float b)
3. Sequence of datatype of parameters: add(float a, int b) and add(int a, float b)
- Method overridding: a feature that allows a subclass or child to implement the same method that is provided by one of his superclasses or parent classes. Here, a child class gives its own implementation to a method that is already provided by the parent class.
The method of the child class is called the overriding method and the method of the parent class is called the overridden method

## Lesson 16B: Abstract Class
- A class declared using the 'abstract' keyword. The abstract class can have an abstract method (method without body) & concrete methods (regular methods with body)

## Lesson 17A: Interface
- Interfaces look like classes but are not. They have abstract methods (only method signature, no body). The class that implements interface must implement all methods of the interface. Java doesnt allow you extend more than 1 class, i.e have more than 1 parent, but you can implement many interfaces in Java.
- 'implements' is the keyword used by classes that use interface.
- Difference between abstract & interfaces https://prnt.sc/YPdsSVXiS-DV

## Lesson 17B: Error Handling
- An unwanted event that interrupts the program flow.
- Types of exceptions:
* Checked exception(checked at compile time eg IOException, SQLException)
* Unchecked exceptions (checked at runtime eg ArithmeticException & NullPointerExceptions.)
* Error (This means the system should crash instead of handling the error eg OutOfMemory, AssertionError, VirtulMachineError)
- Terminologies in Java exceptions: Try(Used to specify where an exception code should be put. It is used with either catch or finally), Catch(this block is used to handle the excpetion, preceeded by a try block), Finally(used to execute the necessary program code), Throw(used to throw an excepton), Throws(used to declare an exception & is used by method body)
- Hierarchy of exceptions https://prnt.sc/FlD56CniIdoQ

## Lesson 19: Keywords in JAVA
The final keyword is used for variables, methods and classes
- when used as a variables, the value of the variable cannot be changed except in a static block or inside a constructor

public static void main(String[] args) {
        final int ballSize = 17;
        ballSize = 23;    //flagged as we cannot reassign the value bcos of final keyword
        System.out.println("The size of the ball in cm is " + ballSize);
    }

We need to use a constructor of static block to be able to change this value
// A. With Constructor

public class Task19 {
    final int ballSize;
    

    public Task19(){       //constructors dont have body & is name of the class)
        ballSize = 23;
    }

// B. With static class

public class Task19 {
    int ballSize;
    

    public static void main(String[] args) { // using final with static class
        final int ballSize = 17;
        System.out.println("The size of the ball in cm is " + ballSize);
    }
    
}

- When used as a method, the method cannot be overridden
- When used as a class, the class cannot be extended

### This Keyword: 
Used when another variable within the current scope shares the same name and you want to use the instance member. Within a constructor, the this keyword can be used to call another constructor in the same class

### Super Keyword
Its used in subclasses to access the objects of the parent class

### Static keyword 
This is used for memory management. It can be used for variables, methods, nested classes, blocks. Static objects can be invoked without creating an object of the class
