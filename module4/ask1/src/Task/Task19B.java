package Task;

public class Task19B extends Task19 {
    String ballColour = "Green";

    public static void main(String[] args) {
        Task19B object = new Task19B();
        object.ballProperty();
    }

    public void ballProperty(){       //constructors dont have body & is name of the class)
        System.out.println("The color of the ball is " + ballColour);
    
    }
}
