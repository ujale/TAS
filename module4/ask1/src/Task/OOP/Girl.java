package Task.OOP;

public class Girl {
    public static void main(String[] args) {
        Human lolaVariable = new Human();  // This Object 'lolaVariable' acts as a key into the Human class
        lolaVariable.name = "Lola";
        lolaVariable.age = 12;

        lolaVariable.aboutMe(lolaVariable.name, lolaVariable.age);  // The object 'lolaVariable' is calling the method 'aboutMe' in class A
    }

    // Lesson 14: Inheritance
// package Task;

// public class Task14b {
//     public static void main(String[] args) {
//         Task14 lola = new Task14();
//         lola.setThroat("long throat");
//         String lolaThroat = lola.getThroat();
//         System.out.println(lolaThroat);
//         int lolaLegs = lola.getLegs();
//         System.out.println("Lola has " + lolaLegs);
//     }
}





