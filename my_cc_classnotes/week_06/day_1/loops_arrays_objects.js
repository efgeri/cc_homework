var sports = ["football", "tennis", "rugby", "curling", "snooker"]

sports.push("darts")

console.log(sports)
console.log(sports[1])
console.log(sports.length)

// you can catch the popped element, because the method returns it
var removedElement = sports.pop()
console.log(sports)
console.log(removedElement)

sports.unshift("basketball")
console.log(sports)

// shift also returns the removed element
sports.shift()
console.log(sports)

// var splicedThing = sports.splice(3, 2, "banana", "apple")
console.log(sports)
// console.log(splicedThing)

for (var sport of sports) {
    console.log(sport.toUpperCase())
}

console.log(sports)

for (var i = 0; i < sports.length; i++) {
    var currentSport = sports[i]
    console.log(currentSport.toUpperCase())
}

var movie = {
    title: "It's a wonderful Life",
    year: 1946,
    language: "Spanish"
}
console.log(movie.title)

movie.cast = ['James Stewart', "Donna Reid"]
movie.language = "English"
movie['language'] = "Italian"
movie.subtitleLanguage = "German"

// delete movie.year

movie.ratings = {
    critic: 94,
    audience: 95
}

console.log(movie)
console.log(movie.ratings.audience)

for (var key in movie) {
    console.log(key)
    var value = movie[key]
    console.log(key + " is " + value)
}

var keys = Object.keys(movie)
console.log(keys)