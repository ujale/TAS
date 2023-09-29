package CodingChallenge;

//Reverse "TestifyAutomation" using recursion in Java 

public class Challenge7 {
    public static String reverse(String str) {
            // Base case: if the string is empty or has only one character, return it as is
            if (str == null || str.length() <= 1) {
                return str;
            }
            
            // Recursive case: reverse the substring excluding the last character
            String reversedSubstring = reverse(str.substring(0, str.length() - 1));
            
            // Concatenate the last character to the reversed substring
            return str.charAt(str.length() - 1) + reversedSubstring;
        }
    
        public static void main(String[] args) {
            String input = "TestifyAutomation";
            String reversed = reverse(input);
            System.out.println("Original String: " + input);
            System.out.println("Reversed String: " + reversed);
        }
}
