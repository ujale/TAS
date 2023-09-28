package Keywords;

public class SuperKeywordChild extends SuperKeywordParent{
    String name = "Angela";

    public void printName(){
        System.out.println("My Parent name is " + super.name); //to call the variable in this child class, remove super. But to ref that of ths prent use the super.<var name>
    }

    public static void main(String[] args) {
        SuperKeywordChild object = new SuperKeywordChild();
        object.printName();
    }
}
