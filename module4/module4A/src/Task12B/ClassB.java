package Task12B;

import Task12A.ClassA;

public class ClassB {
    public static void main(String[] args) {
        ClassA newEverywhere = new ClassA();
        newEverywhere.everyWhere();
        ClassB restrictAccess = new ClassB();
        restrictAccess.restrictedMethod();
    } 

    private void restrictedMethod(){
        System.out.println("This method can only be accessed within this Class B");
    }
}


