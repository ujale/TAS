package Task;

public class Task13ClassA {
    String brand;
    int wheels;
    boolean canFly;

    public Task13ClassA(String brand){
        this.brand = brand;
    }

    public Task13ClassA(String brand, int aWheels){
        this.brand = brand;
        wheels = aWheels;
    }

    public Task13ClassA(String brand, int aWheels, boolean canFly){
        this.brand = brand;
        wheels = aWheels;
        this.canFly = canFly;

    }
}
