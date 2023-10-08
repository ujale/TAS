package Task;

import java.util.Scanner;

/* Write a code that asks the user for age and that accepts the Integer value.
Handle the error that is encountered when the users tries to enter a name instead of age
*/
public class Task18 {
    public static void main(String[] args) {
        try {
        Scanner age = new Scanner(System.in);
        int myAge = age.nextInt();
        System.out.println("I am " + myAge + "years old" );

        } catch (Exception ageException) {
            // TODO: handle exception
            System.out.println("This is not a valid age" );
        }
    }
    
}
