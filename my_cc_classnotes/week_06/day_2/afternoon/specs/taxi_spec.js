const assert = require('assert')
const Taxi = require('../taxi.js')

describe('Taxi', function(){
    let taxi
    beforeEach(function(){
        taxi = new Taxi("Toyota", "Prius", "Johnny Bravo");
    })

    it('should have a manufacturer', function(){
        const actual = taxi.manufacturer;
        assert.strictEqual(actual, 'Toyota');
    });
    it('should have a model', function(){
        const actual = taxi.model;
        assert.strictEqual(actual, 'Prius');
    });
    it('should have a driver', function(){
        const actual = taxi.driver;
        assert.strictEqual(actual, 'Johnny Bravo');
    });

    describe('passengers', function(){
        beforeEach(function(){
        })
        it('should start with no passengers', function(){
            const actual = taxi.passengers;
            assert.deepStrictEqual(actual, [])
        });
        it('should be able to count passengers', function(){
            const actual = taxi.numberOfPassengers();
            assert.deepStrictEqual(actual, 0)
        });
        it('should be able to add passengers', function(){
            taxi.addPassenger("John");
            const actual = taxi.numberOfPassengers();
            assert.deepStrictEqual(actual, 1)
        });
        it('should be able to remove passengers by name', function(){
            taxi.addPassenger("Luke");
            taxi.addPassenger("Kate");
            taxi.removePassengerByName("Kate")
            const actual = taxi.numberOfPassengers();
            assert.deepStrictEqual(actual, 1)
        });
        it('should be able to remove all passengers', function(){
            taxi.addPassenger("Luke");
            taxi.addPassenger("Kate");
            taxi.removeAllPassengers()
            const actual = taxi.numberOfPassengers();
            assert.deepStrictEqual(actual, 0)
        });


    })

});