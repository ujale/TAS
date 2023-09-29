package CodingChallenge;

/*Given a collection of 1 million integers, all ranging between1 to 9, sort them in Big O(n) timeJAVA CODING CHALLENGE
 */

public class Challenge9 {
    public static void countingSort(int[] arr) {
        int max = 9; // The maximum value in the range (1 to 9)
        int min = 1; // The minimum value in the range (1 to 9)
        int range = max - min + 1;
        
        // Create a counting array to store the count of each integer in the range
        int[] count = new int[range];
        
        // Count the occurrences of each integer in the input array
        for (int num : arr) {
            count[num - min]++;
        }
        
        int index = 0;
        
        // Reconstruct the sorted array from the counting array
        for (int i = min; i <= max; i++) {
            while (count[i - min] > 0) {
                arr[index++] = i;
                count[i - min]--;
            }
        }
    }
    
    public static void main(String[] args) {
        int[] arr = {4, 2, 2, 8, 3, 3, 1, 9, 6, 5};
        countingSort(arr);
        
        // Print the sorted array
        for (int num : arr) {
            System.out.print(num + " ");
        }
    }
    
}
