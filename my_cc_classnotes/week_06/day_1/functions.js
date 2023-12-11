function sayHello(name = "World") {
    return `Hello ${name}`
}

console.log(sayHello("Geri"))

var add = function(firstNumber, secondNumber) {
    return firstNumber + secondNumber
}

console.log(add(1, 3))
numbers = [5, 10, 19]

var addList = function(numberArray) {
    var sum = 0
    for (number of numberArray){
        sum += number
    }
    return sum
}

console.log(addList(numbers))

var multiply = (firstNumber, secondNumber) => {
    return firstNumber * secondNumber
}

// This above can be written like this
// var multiply = (firstNumber, secondNumber) => firstNumber * secondNumber

console.log(multiply(2, 3))