package Task;


public class Task17Aii extends Task17Ai{
    public static void main(String[] args) {
        Task17Aii user = new Task17Aii();
        user.userName();
        user.userPassword();
        user.other(true, false, true);
    }

    @Override
    public void userName(){
        System.out.println("Enter your username");
    }

    @Override
    public void userPassword(){
        System.out.println("Enter your password");
    }

}
