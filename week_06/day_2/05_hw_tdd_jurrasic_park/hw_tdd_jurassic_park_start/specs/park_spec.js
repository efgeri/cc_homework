const assert = require('assert');
const Park = require('../models/park.js');
const Dinosaur = require('../models/dinosaur.js');

describe('Park', function() {
  let park
  let trex
  let trex2
  let raptor
  let stego
  beforeEach(function () {
    trex = new Dinosaur("T-Rex", "carnivore", 100)
    trex2 = new Dinosaur("T-Rex", "carnivore", 99)
    raptor = new Dinosaur("Velociraptor", "carnivore", 150)
    stego = new Dinosaur("Stegosaurus", "herbivore", 2)
    park = new Park ("Jurassic Park", 25, [trex, raptor])
  })

  it('should have a name', function(){
    const actual = park.name
    assert.strictEqual(actual, "Jurassic Park")
  });

  it('should have a ticket price', function(){
    const actual = park.ticketPrice
    assert.strictEqual(actual, 25)
  });

  it('should have a collection of dinosaurs', function(){
    const actual = park.dinosaurs.length
    assert.strictEqual(actual, 2)
  });

  it('should be able to add a dinosaur to its collection', function(){
    park.addDino(stego)
    const actual = park.dinosaurs.length
    assert.strictEqual(actual, 3)
  });

  it('should be able to remove a dinosaur from its collection', function(){
    park.addDino(stego)
    park.removeDino(raptor)
    const actual = park.dinosaurs.length
    assert.strictEqual(actual, 2)
  });

  it('should be able to find the dinosaur that attracts the most visitors', function(){
    const actual = park.mostPopular()
    assert.deepStrictEqual(actual, raptor)
  });

  it('should be able to find all dinosaurs of a particular species', function(){
    park.addDino(trex2)
    const actual = park.sameSpecies("T-Rex")
    const expected = [trex, trex2]
    assert.deepStrictEqual(actual, expected)
  });

  it('should be able to calculate the total number of visitors per day', function(){
    const actual = park.visitorsPerDay()
    assert.deepStrictEqual(actual, 250)
  });
  
  it('should be able to calculate the total number of visitors per year', function(){
    const actual = park.visitorsPerYear()
    assert.deepStrictEqual(actual, 91250)
  });

  it('should be able to calculate total revenue for one year', function(){
    const actual = park.revenuePerYear()
    assert.deepStrictEqual(actual, 2281250)
  });

  it('should be able to remove all dinosaurs of a particular species', function(){
    park.addDino(trex2)
    park.addDino(stego)
    park.removeSpecies("T-Rex")
    const actual = park.dinosaurs.length
    assert.deepStrictEqual(actual, 2)
  });
  
  it('should be able to provide an object containing each of the diet types and the number of dinosaurs in the park of that diet type', function(){
    park.addDino(stego)
    const expected = { 'carnivore': 2, 'herbivore': 1 }
    const actual = park.countDiets()
    assert.deepStrictEqual(actual, expected)
  });

});
