package Task.OOP;

public class Human {   // Class
    
    String name; // global variable
    int age;

    public void aboutMe(String myName, int myAge){          // Method
        name = myName;      // myName & myAge are local variables passed within the method and we are instructing 
        age = myAge;      // the values passed should be saved to global variables

        System.out.println(name + " " + age);
    }

}


