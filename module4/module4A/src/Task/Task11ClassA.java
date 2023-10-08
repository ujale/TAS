package Task;

public class Task11ClassA {
    
    String firstName;  // global variable
    String lastName;   // global variable

    public void myFullName(String fName, String lName){
        firstName = fName;                      // the 
        lastName = lName;
        System.out.println(firstName + " " + lastName);  // We choose to print out the global variable
    }

}
