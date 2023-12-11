package org.example;

import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello world!");
        List<Integer> output = Stream.of(1, 2, 3, 4, 5, 6, 7)
                .peek(str -> System.out.println("Original: " + str))
                .map(result -> result *2)
                .peek(str -> System.out.println("Double: " + str))
                .collect(Collectors.toList());
    }
}