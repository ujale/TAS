package Task.OOP;

public class Human {   // Class
    
    String name; // global variable
    int age;

    public void aboutMe(String myName, int myAge){          // Method
        name = myName;      // myName & myAge are local variables passed within the method and we are instructing 
        age = myAge;      // the values passed should be saved to global variables

        System.out.println(name + " " + age);
    }

//     // Lesson 14: Encapsulation
// package Task;

// public class Task14 {
//     private String throat;
//     private int legs = 2;
//     private String stomach;
//     String mouth;
    
//     public String getThroat(){
//         return throat;
//     }
    
//     public void setThroat(String throat){
//         this.throat = throat;
//     }
    
//     public int getLegs(){
//         return legs;
//     }
    
//     public String getStomach(){
//         return stomach;
//     }
    
//     public void setStomach(String stomach){
//         this.stomach = stomach;
//     }
    
//     public String getMouth(){
//         return mouth;
//     }
    
//     public void setMouth(String mouth){
//         System.out.println(mouth);
//     }
// }
    


}


