package Polymorphism;

// Overload and override

public class Son extends Father{
    public static void main(String[] args) {
        Son Matt = new Son();

        Matt.playSoccer(2, true);
    }
    /*
     * the son inherits the attributes of the father here
     */

    public void playSoccer(int type, boolean condition){
        System.out.println("Son plays soccer");
    }
    /*
     * this overrode the father method
     */
    
}
