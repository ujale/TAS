package Polymorphism;

public class Father {
    public void playGuitar(){

    }

    public void playSoccer(int type, boolean condition){
        System.out.println("Father enjoys playing soccer");
    }

    public void playSoccer(int type, boolean condition, float number){
        System.out.println("Father enjoys playing soccer");
    }

    public void playSoccer(boolean condition, float number, int type){
        System.out.println("Father enjoys playing soccer");
    }
    /*
     * The playSoccer methods show the different examples of overload
     */
}
