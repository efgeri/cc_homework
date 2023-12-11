console.log("hello world")

var myName = "Mickey"
myName = "minnie"
// myName = 1
console.log(myName)
console.log(typeof myName)
console.log(myName.toUpperCase())
console.log(myName.length)
console.log(3 + 3)
console.log(3 ** 3)
console.log(5 % 3)

console.log(Number("1"))
console.log(String("1"))

console.log(myName + " " + myName)
console.log(`Hello ${myName}`)

var isRaining = false
if (1 < 0){
    console.log("That condition was true")
} else if (1==0) {
    console.log("I will never show")
} else {
    console.log("In all other cases do this")
}