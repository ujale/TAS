package Task;

public class Task15Child extends Task15Parent{
    static Task15Child movieType = new Task15Child();
    public void thriller(){
        System.out.println("I love suspense");
    }

    public void comedy(){
        System.out.println("I love humory");
    }

    public static void main(String[] args) {
        Task15Parent parent = new Task15Parent();
        parent.cooking();
        parent.reading();
        parent.singing();
        movieType.thriller();
        movieType.comedy();
    }

    
}
