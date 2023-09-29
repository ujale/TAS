package CodingChallenge;

/* Using  Java  Code,  check  for  Anagrams  in  these  strings:
"Despite commuting at the peek hour, she was able to keep to time"
*/

import java.util.*;

public class Challenge6 {
    public static void main(String[] args) {
        String input = "Despite commuting at the peek hour, she was able to keep to time";
        String[] words = input.split("\\s+");

        Map<String, List<String>> anagramGroups = new HashMap<>();

        for (String word : words) {
            // Remove spaces and convert to lowercase
            String sortedWord = sortString(word.toLowerCase());

            // Add the word to its anagram group
            anagramGroups.computeIfAbsent(sortedWord, k -> new ArrayList<>()).add(word);
        }

        // Print anagram groups
        for (List<String> group : anagramGroups.values()) {
            if (group.size() > 1) {
                System.out.println("Anagrams: " + String.join(", ", group));
            }
        }
    }

    private static String sortString(String input) {
        char[] charArray = input.toCharArray();
        Arrays.sort(charArray);
        return new String(charArray);
    }

}
