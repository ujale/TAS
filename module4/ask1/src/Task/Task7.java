package Task;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;

public class Task7 {
    public static void main(String[] args) {
        
        String [] [] doubleDimension = new String [4] [3];
        doubleDimension [0] [0] = "Banana";
        doubleDimension [0] [1] = "Mango";
        doubleDimension [0] [2] = "Pineapple";
        

        System.out.println(Arrays.deepToString(doubleDimension));
    }
}
