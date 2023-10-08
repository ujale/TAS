package Abstract;

public class Goat extends Animal{
    public static void main(String[] args) {
        Goat africanGoat = new Goat();
        africanGoat.horn();
        africanGoat.sound();
        africanGoat.eat();
    }

    @Override
    public void sound(){
        System.out.println("Bleats");
    }

    @Override
    public void eat(){
        System.out.println("Eats grass");
    }

}
