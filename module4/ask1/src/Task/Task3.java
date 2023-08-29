package Task;

public class Task3 {
    public static void main(String[] args) {
        // string to primitive concat

        int age = 16;
        String phrase = "My age is: ";
        String sentence = (phrase + age);
        
        System.out.println(sentence);

        // string to string concat

        String ageInWords = "Sixteen years old";
        String phrase2 = "I am ";
        String sentence2 = (phrase2 + ageInWords);
        
        System.out.println(sentence2);

        // .concat method

       phrase.concat(age + "");
        
        System.out.println(phrase.concat(age + ""));


    }
    
}
