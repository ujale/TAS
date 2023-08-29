package Task;


public class Task2 {
    public static void main(String[] args){
//      byte from -128 to 127
//      short from -32,768 to 32,767
//      int from -2, -148, -483, 648 to 2, 148, 483, 648
//      long from -9, -223, -372, -036, -854, -775, -808 to 9, 223, 372, 036, 854, 775, 808
//      float from 6 to 7 decimal digits
//      double from 15 decimal digits
//      char single letters 'a', 'b'
//      boolean true, false

        byte age = -127;
        short money = 32_767;
        long soMuchMoney = -213456750l;
        float area = 12345678.90f;
        double biggerArea = 123456789.67;
        char option = 'a'; // single quotation
        System.out.println(area);
        System.out.println(age);
        System.out.println(money);
        System.out.println(soMuchMoney);
        System.out.println(biggerArea);
        System.out.println(option);
    }
}

