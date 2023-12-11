const Person = function(name, age, pet) {
    this.name = name
    this.age = age
    this.pet = pet
}

Person.prototype.greet = function(){
    console.log("Hiya I am " + this.name)
}

Person.prototype.feedPet = function(food){
    console.log(`${this.name} fed ${this.pet.name} a ${food}`)
    this.pet.eat(food)
}

module.exports = Person