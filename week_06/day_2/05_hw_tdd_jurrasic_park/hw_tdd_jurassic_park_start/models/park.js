const Park = function(name, ticketPrice, dinosaurs = []){
    this.name = name
    this.ticketPrice = ticketPrice
    this.dinosaurs = dinosaurs
}

Park.prototype.addDino = function(dino){
    this.dinosaurs.push(dino)
}

Park.prototype.removeDino = function(dino){
    const indexOfDino = this.dinosaurs.indexOf(dino);
    this.dinosaurs.splice(indexOfDino, 1);
}
Park.prototype.mostPopular = function(){
    let popularity = 0
    let selectedDino
    for (dino of this.dinosaurs){
        if (dino.guestsAttractedPerDay > popularity){
            popularity = dino.guestsAttractedPerDay
            selectedDino = dino
        }
    }
    return selectedDino
}

Park.prototype.sameSpecies = function(species){
    let dinoList = []
    for (dino of this.dinosaurs){
        if (dino.species === species){
            dinoList.push(dino)
        }
    }
    return dinoList
}

Park.prototype.visitorsPerDay = function(){
    let total = 0
    for (dino of this.dinosaurs){
        total += dino.guestsAttractedPerDay
    }
    return total
}

Park.prototype.visitorsPerYear = function(){
    const perDay = this.visitorsPerDay()
    return perDay * 365
}

Park.prototype.revenuePerYear = function(){
    const perYear = this.visitorsPerYear()
    return perYear * this.ticketPrice
}

Park.prototype.removeSpecies = function(species){
    const toRemove = this.sameSpecies(species)
    for (dino of toRemove){
        this.removeDino(dino)
    }
}

Park.prototype.specificDiet = function(diet){
    let count = 0
    for (dino of this.dinosaurs){
        if (dino.diet === diet){
            count++
        }
    }
    return count
}

Park.prototype.countDiets = function(){
    let carnivores = this.specificDiet("carnivore")
    let herbivores = this.specificDiet("herbivore")
    let omnivores = this.specificDiet("omnivore")
    const dietDict =  { 'carnivore': carnivores, 'herbivore': herbivores, 'omnivore': omnivores }
    return dietDict
}


module.exports = Park