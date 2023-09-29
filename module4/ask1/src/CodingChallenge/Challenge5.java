package CodingChallenge;

/* Create anagram buckets from a given input array of words:input is 
{"akka", "akak", "baab", "baba", "bbaa"} 
*/

import java.util.*;

public class Challenge5 {
    public static List<List<String>> groupAnagrams(String[] words) {
        Map<String, List<String>> anagramBuckets = new HashMap<>();

        for (String word : words) {
            char[] charArray = word.toCharArray();
            Arrays.sort(charArray);
            String sortedWord = new String(charArray);

            anagramBuckets.computeIfAbsent(sortedWord, k -> new ArrayList<>()).add(word);
        }

        return new ArrayList<>(anagramBuckets.values());
    }

    public static void main(String[] args) {
        String[] input = {"akka", "akak", "baab", "baba", "bbaa"};
        List<List<String>> anagramGroups = groupAnagrams(input);

        for (List<String> group : anagramGroups) {
            System.out.println(group);
        }
    }

}
