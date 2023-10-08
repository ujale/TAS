package CodingChallenge;

// Write  a  Javacode  to  check  for  the Prime  numbers between 1-100

public class Challenge4 {
    public static void main(String[] args) {
            System.out.println("Prime numbers between 1 and 100 are:");
            
            // Loop through numbers from 2 to 100
            for (int i = 2; i <= 100; i++) {
                boolean isPrime = true;
                
                // Check if the current number is prime
                for (int j = 2; j < i; j++) {
                    if (i % j == 0) {
                        isPrime = false;
                        break;
                    }
                }
                
                // If the number is prime, print it
                if (isPrime) {
                    System.out.print(i + " ");
                }
            }
        }
}
