const Pet = require('./pet.js')
const Person = require('./person.js')


const scooby = new Pet('Scooby Doo', 'Dog');
scooby.eat('Scooby Snack')

const shaggy = new Person("Shaggy Rogers", 32, scooby)
shaggy.greet()
shaggy.feedPet('Scooby Snackity Snack')