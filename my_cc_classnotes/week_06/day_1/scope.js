var person = "Jill"

var secretsFunction = function() {
    var pinCode = [0, 0, 0, 0]
    console.log("pinCode inside secretsFunction", pinCode)
    console.log("person inside secretsFunction", person)
}

secretsFunction()
// console.log("pinCode inside secretsFunction", pinCode)
// since the variable is local to the function, this won't work