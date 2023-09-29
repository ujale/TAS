package CodingChallenge;

// Find two numbers of which the product is maximum in an array

public class Challenge3 {
    public static void main(String[] args) {
            int[] numbers = {0, 2, 3, 4, 5, 6, 7, 8, 9};
            
            if (numbers.length < 2) {
                System.out.println("Array should contain at least two numbers");
                return;
            }
    
            int max1 = Integer.MIN_VALUE; // Initialize max1 to the smallest possible integer
            int max2 = Integer.MIN_VALUE; // Initialize max2 to the smallest possible integer
    
            for (int num : numbers) {
                if (num > max1) {
                    max2 = max1; // Move the current max1 to max2
                    max1 = num; // Update max1 with the new maximum number
                } else if (num > max2) {
                    max2 = num; // Update max2 with the new second maximum number
                }
            }
    
            int maxProduct = max1 * max2;
    
            System.out.println("The two numbers with the maximum product are: " + max1 + " and " + max2);
            System.out.println("The maximum product is: " + maxProduct);
        }
    
}
