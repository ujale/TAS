package CodingChallenge;

// Reverse the position of words in "I am the best AutomationTester" using recursion:

public class Challenge2 {
    public static void main(String[] args) {
            String input = "I am the best Automation Tester";
            String reversed = reverseWords(input);
            System.out.println(reversed);
        }
    
        public static String reverseWords(String input) {
            // Base case: If the input is empty or contains only spaces, return it as is.
            if (input.isEmpty() || input.trim().isEmpty()) {
                return input;
            }
    
            // Find the position of the first space.
            int spaceIndex = input.indexOf(' ');
    
            if (spaceIndex == -1) {
                // If there are no more spaces, return the input string as is.
                return input;
            } else {
                // Split the input into the word before the space and the rest of the string.
                String word = input.substring(0, spaceIndex);
                String restOfString = input.substring(spaceIndex + 1);
    
                // Recursively reverse the rest of the string.
                String reversedRest = reverseWords(restOfString);
    
                // Concatenate the reversed rest with the word and a space.
                return reversedRest + " " + word;
            }
        }
}
