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


# Notes
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
    System.out.println("My name is Shakespear");
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

        Task10 methodVar = new Task10();
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
        return age;
    }
}

- Methods with return values will make use of parameters to pass dynamic values and the keyword return. For such methods no return type of 'void' is not used 
eg the ageCalculator method above