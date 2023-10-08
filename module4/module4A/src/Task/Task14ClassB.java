package Task;

public class Task14ClassB {
    public static void main(String[] args) {
        Task14ClassA shape = new Task14ClassA();
        shape.setLength(5);
        int squareLength = shape.getLength();
        System.out.println("The length of the square is " + squareLength);

        shape.setBreadth(5);
        int squareBreadth = shape.getBreadth();
        System.out.println("The breadth of the square is " + squareBreadth);
        int shapeSides = shape.getShapeSides();
        System.out.println("A square has " + shapeSides + " sides");

        int areaOfSquare = squareLength * squareBreadth;
        System.out.println("The area of the square of length " + squareLength + " and breadth " + squareBreadth + " is " + areaOfSquare);
    }
}
