package Task;

public class Task5 {
    public static void main(String[] args) {
        int number = 21;

        if(number % 3 == 0 && number % 5 ==0){
            System.out.println("FizzBuzz");
        }else if(number % 5 == 0){
            System.out.println("Buzz");
        }else if(number % 3 == 0){
            System.out.println("Fizz");
        }else{
            System.out.println( number + " is not divisible by 3 or 5");
        }
        
    }
}
