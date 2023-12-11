import java.util.ArrayList;

public class Runner {
    public static void main(String[] args) {
        ArrayList<Integer> myListOfNumbers = new ArrayList<>();
        myListOfNumbers.add(1);
        myListOfNumbers.add(3);
        myListOfNumbers.add(5);
        myListOfNumbers.add(7);
        myListOfNumbers.add(9);

        int myNumberToFind = 1;
        int result = BinarySearch.find(myListOfNumbers, myNumberToFind);
        if (result != -1) {
            System.out.println("Found the number at index " + result);
        } else {
            System.out.println("The number is not in the array");
        }
    }
}
