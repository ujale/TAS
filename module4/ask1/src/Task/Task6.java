package Task;

public class Task6 {
    public static void main(String[] args) {
        String word = "DEMOCRACY";
        StringBuilder reversed = new StringBuilder(word).reverse();
        String reversedString = reversed.toString();

        System.out.println(reversedString);
        System.out.println(reversedString.substring(4,8));
    }
}
