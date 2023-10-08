package Keywords;

public class Subkeyword extends Keywords{
    public static void main(String[] args) {
        Subkeyword object = new Subkeyword();
        object.eat();
        object.eats(); //new method
    }

    // @Override
    // public void eat(){    // cant call the eat() of the keyword class cos final cannot be overridden
    //     System.out.println("Child wants to eat");
    // }

    public void eats(){    // the only way this can be called is to rename the method to a new one i.e from eat to eats
        System.out.println("Child wants to eat");
    }

}
