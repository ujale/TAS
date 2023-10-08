package Task;

public class Task16BChild extends Task16BParent{
    public static void main(String[] args) {
        Task16BChild Suit = new Task16BChild();
        Suit.suits(14, "Italian", "Navy Blue", true);
    }

    public void suits(int size, String type, String color, boolean isMale){
        System.out.println("This is a classy pink french suit in size 12");
    }
}
