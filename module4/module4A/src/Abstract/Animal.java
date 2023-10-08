package Abstract;

public abstract class Animal {
    public abstract void sound();  // abstract method( method without a body)
    public abstract void eat(); // abstract method( method without a body)
    public void horn(){         // concrete method
        System.out.println("I have a horn");
    }


}
