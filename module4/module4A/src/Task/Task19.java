package Task;

/*
 * FINAL: create 3 variables of a class A, ballSize, ballColour, ballTexture. and make it impossible to change the value the ballSize in any method in that class

STATIC: I want to use the value of a variable in one class in another class at runtime. I also want to access the variable without creating an object of its class. Help me implement this

SUPER: Class B is extending Class A, Class B has a variable String name = "Anderson" while Class A has the same varible name and type is an attribute "Ronke". Print out the value of Class A and class B in your main method using the object of only One class. (Dont create two objects).

THIS https://i.imgur.com/aRkRDPa.png You have a class with a method printName. write a code in the printName method that will print the instance member which is "Delta" and whatever name the user enter when invoking the method
 */

public class Task19 {
    int ballSize;
    
    String ballColour;
    String ballTexture;
    

    public void ballProperty (){       //constructors dont have body & is name of the class)
        //ballSize = 23;
        ballColour = "White";
        //ballTexture = "Smooth";
        System.out.println("The color of the ball is " + ballColour);
    
    }


    public static void main(String[] args) { // using final with static class
        final int ballSize = 17;
        System.out.println("The size of the ball in cm is " + ballSize);
    }
    
}
