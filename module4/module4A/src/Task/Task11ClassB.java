package Task;

public class Task11ClassB {
    public static void main(String[] args) {
        
        Task11ClassA myNameVariable = new Task11ClassA();

        myNameVariable.firstName = "Udeme";
        myNameVariable.lastName = "Jalekun";

        myNameVariable.myFullName(myNameVariable.firstName, myNameVariable.lastName);
    }
}
