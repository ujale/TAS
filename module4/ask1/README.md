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

