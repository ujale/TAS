package Task;

public class StringAndConcat {

    public static void main(String[] args) {
        // String and string concat

        String bird = "hummingbird";
        String adjective = " is a beautiful bird";
        String newString = (bird + adjective);
        
        System.out.println(newString);

        //String and primitive concat
        String movieName  = "matrix";
        int parts = 4;
        boolean isReleased = false;

        System.out.println(movieName + ":" + parts + isReleased);

        //.concat() method
        movieName.concat(parts + "");

        System.out.println(movieName.concat(parts + ""));

    }
}
