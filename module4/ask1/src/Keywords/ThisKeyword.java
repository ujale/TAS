package Keywords;

public class ThisKeyword {
    
    String name;
    int age;

    public ThisKeyword(){
        this("Angela", 12);
    }

    public ThisKeyword(String name, int age){
        System.out.println("This is constructor 2");
    }

    public static void main(String[] args) {
        ThisKeyword name = new ThisKeyword();
    }
}
