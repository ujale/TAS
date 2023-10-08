package Task;

import java.util.Scanner;

public class Task8 {
    public static void main(String[] args){
        Scanner userInput = new Scanner(System.in);
        System.out.println("Enter the value for principal.");
        double principal = userInput.nextDouble();
        System.out.println("Enter the percentage value for rate");
        double rate = userInput.nextDouble();
        System.out.println("Enter the value for duration in years.");
        double time = userInput.nextDouble();
        double simpleInterest = principal * rate * time;
        System.out.println("The simple interest is " + simpleInterest);
        
    }

}
