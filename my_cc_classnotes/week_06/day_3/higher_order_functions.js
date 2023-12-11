const myNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

// for (const number of myNumbers){
//     console.log(`This is number ${number}`);
// };

// myNumbers.forEach((number, index) => {
//     console.log(`This is number ${number} at ${index}`);
// })

const multiplyByTwo = function (numbers) {
    const result = [];
    numbers.forEach((number) => {
        const multiplied = number * 2;
        result.push(multiplied)
    })

    return result
}

console.log(multiplyByTwo(myNumbers))

const getEvens = function (numbers) {
    const result = [];
    numbers.forEach((number) => {
        if (number % 2 === 0){
            result.push(number)
        } 
    })
    return result
}
console.log(getEvens(myNumbers))

const multiplyByTwoMap = function (numbers) {
    const result = numbers.map((number) => {
        return number * 2
    });
    return result
}

console.log(multiplyByTwoMap(myNumbers))


const getEvensFilter = function (numbers){
    const result = numbers.filter((number) => {
        return number % 2 === 0;
    })
    return result
}

console.log(getEvensFilter(myNumbers))

const sumElements = function (numbers) {
    let total = 0;
  
    numbers.forEach((number) => {
      total += number;
    })
  
    return total;
  }
  
  console.log(sumElements(myNumbers));

  const sumElementsReduce = function (numbers) {
    const total = numbers.reduce((runningTotal, number) => {
        return runningTotal + number;
    }, 0);
    return total;
  }
  console.log(sumElementsReduce(myNumbers));