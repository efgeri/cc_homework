package org.example;

import java.util.ArrayList;

public class Main {

    public static String reverseString(String string) {
        String reversed = "";
        for (int i = string.length() - 1; i >= 0; i--) {
            reversed += string.charAt(i);
        }
        return reversed;
        }

    public static int findHighest(ArrayList<Integer> numbers) {
        Integer highest = numbers.get(0);
        for (int i = 1; i < numbers.size(); i++) {
            if (numbers.get(i) > highest) {
                highest = numbers.get(i);
            }
        }
        return highest;
    }

    public static void main(String[] args) {
        System.out.println("Reversed string: " + reverseString("Reverse this!"));

        ArrayList<Integer> numbers = new ArrayList<>();
        numbers.add(7);
        numbers.add(1);
        numbers.add(9);
        numbers.add(14);
        numbers.add(3);
        System.out.println("The highest number in this list is: " + findHighest(numbers));
    }
}