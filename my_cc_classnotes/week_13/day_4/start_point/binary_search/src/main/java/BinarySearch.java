import java.util.ArrayList;

public class BinarySearch {

    public static int find(ArrayList<Integer> listOfNumbers, int numberToFind) {
        // Set the left boundary of the search range to the first index of the list
        int left = 0;
        // Set the right boundary of the search range to the last index of the list
        int right = listOfNumbers.size() -1;

        // Continue searching as long as the left boundary is less than or equal to the right boundary
        while (left <= right){
        // Calculate the middle index of the search range
            int mid = (left + right) / 2;
            if (listOfNumbers.get(mid) == numberToFind){
                return mid;
            }
            else if (listOfNumbers.get(mid) < numberToFind){
                left = mid + 1;
            }
            else right = mid - 1;
        }
        // If the value at the middle index is equal to the target, we found it
        // Return the index of the target element
        // If the value at the middle index is less than the target, the target must be in the right half
        // Adjust the left boundary to search the right half of the list
        // If the value at the middle index is greater than the target, the target must be in the left half
        // Adjust the right boundary to search the left half of the list

        // If the while loop exits without finding the target element, return -1 to indicate it was not found
        return -1;
    }
}