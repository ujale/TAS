package Abstract;

// Class used to show implementation of interface for multiple extensions

public class Lion implements Carnivore, Mammals{
    public static void main(String[] args) {
        Lion leo = new Lion();
        leo.sound();
        leo.eat();
        leo.giveBirth();
    }

    @Override
    public void sound(){
        System.out.println("Lions roar");
    }

    @Override
    public void eat(){
        System.out.println("Lions eats flesh");
    }

    
    public void giveBirth(){
        System.out.println("Lions gives birth to their young alive");
    }
}
