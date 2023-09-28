package Task;

/* You are required to build the blueprint for your company's login page. 
From the discussions with the product team, all login pages will have a username field, 
password field, forgot password field, and sign-in button while other elements like 
remember me checkbox, continue to homePage, OAuth button will not be applicable to all 
login pages. with your knowledge of Abstract classes,
Create a class that others developers will have to inherit from
*/

public abstract class Task17Ai {
    public abstract void userName();
    public abstract void userPassword();
    public void other(boolean isCheckbox, boolean continueHome, boolean OAuth){
        System.out.println("Apply the necessary fields");
    }

}
