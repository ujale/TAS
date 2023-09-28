package Task;

/* OVERRIDING: Create two methods in a parent class with arguements.
write a print statement in the method body, Overide the 2 methods in the child class 
and write a diffreent print statement in the body of the overriding method
*/


public class Task16BParent {
    public void suits(int size, String type, String color, boolean isMale){
        System.out.println("This is a male french suit");
    }

    public void occassion(String typeOfEvent, int duration){
        System.out.println("This is a 2-day Exhibition");
    }
}
