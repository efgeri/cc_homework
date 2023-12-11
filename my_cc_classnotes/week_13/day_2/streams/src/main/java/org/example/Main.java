package org.example;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Main {
    public static void main(String[] args) {
        List<String> names  = Arrays.asList("andrew", "roger", "claire", "toby", "geri");
        Stream.of("andrew", "roger", "claire", "toby", "geri");
        List<String> output = Stream.of("andrew", "roger", "claire", "toby", "geri")
                .peek(str -> System.out.println("Original: " + str))
                .map(String::toUpperCase)
                .peek(str -> System.out.println("UpperCase: " + str))
                .collect(Collectors.toList());

//        Same thing as above.
//        List<String> output = names.stream()
//                .peek(str -> System.out.println("Original: " + str))
//                .map(String::toUpperCase)
//                .peek(str -> System.out.println("UpperCase: " + str))
//                .collect(Collectors.toList());
        System.out.println(output);
    }
}