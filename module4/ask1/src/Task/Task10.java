package Task;

import java.util.Scanner;

public class Task10 {
    public static void main(String[] args) {
        //To access the properties of a class, we create an object of the class

        Task10 methodVar = new Task10();
        methodVar.printMessage();  // Invoke the method printName
    }

    public void printMessage(){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Type in \"Testify\" if you are here for a testify training");
        String purpose = scanner.next();

        if(!purpose.equalsIgnoreCase("Testify")){
        System.out.println("Sorry, you are not allowed to remain on this slack channel");
        purpose = scanner.nextLine();
        }else if(purpose.equalsIgnoreCase("testify")){
        System.out.println("Congratulations! You can stay on this slack channel");
        }
    }
}
