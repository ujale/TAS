package CodingChallenge;

// Write  Java  code  to  check  if  racecar  and  10801  is  a palindromes

public class Challenge1 {
    public static boolean isPalindrome(String str, int num) {
        // Remove spaces and convert the string to lowercase
        str = str.replaceAll("\\s+", "").toLowerCase();
            
        int left = 0;
        int right = str.length() - 1;
            
        while (left < right) {
            if (str.charAt(left) != str.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
            
        return true;
    }
    
    public static void main(String[] args) {
        String input = "racecar";
        int input2 = 10801;
        
        if (isPalindrome(input,input2)){
            System.out.println(input + " is a palindrome.");
            System.out.println(input2 + " is a palindrome.");
        } else {
            System.out.println(input + "and" + input2 + " are not a palindrome.");
        }
        
    }
}
    

