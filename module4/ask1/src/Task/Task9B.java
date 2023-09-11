package Task;

import java.util.Scanner;

public class Task9B {
    public static void main(String[] args) {
        // // Option 1: while loop
        // Scanner scanner = new Scanner(System.in);
        // String userInput = "";

        // while(!userInput.equalsIgnoreCase("testify")){
        //     System.out.println("Try again!");
        //     userInput = scanner.nextLine();
        // }

        // //Option 2: while loop with continue & break statement
        // Scanner scanner = new Scanner(System.in);
        // String userInput = "";

        // while(true){
        //     if(!userInput.equalsIgnoreCase("testify")){
        //     System.out.println("Try again!");
        //     userInput = scanner.nextLine();
        //     continue;
        //     }else if(userInput.equalsIgnoreCase("testify")){
        //         System.out.println("You are out of the loop");
        //         break;
        //     }
        // }

        String userInput;
        // Option 3: do while loop
        do{
            System.out.println("Try again!");
            Scanner scanner = new Scanner(System.in);
            userInput = scanner.nextLine();
        } while(!userInput.equalsIgnoreCase("testify"));
    }
}
