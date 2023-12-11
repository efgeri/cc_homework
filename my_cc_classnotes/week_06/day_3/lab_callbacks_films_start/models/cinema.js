const Cinema = function (films) {
  this.films = films;
};

Cinema.prototype.listOfFilmTitles = function(){
  const result = this.films.map((film) => {
    return film.title
  })
  return result
}
Cinema.prototype.filterByTitle = function(filmName){
  const result = this.films.filter((film) => {
    return film.title === filmName
  })
  return result
}

Cinema.prototype.filterByGenre = function(filmGenre){
  const result = this.films.filter((film) => {
    return film.genre === filmGenre
  })
  return result
}

Cinema.prototype.filterByYear = function(filmYear){
  const result = this.films.filter((film) => {
    return film.year === filmYear
  })
  return result
}

Cinema.prototype.someYear = function(filmYear){
  const result = this.films.some((film) => {
    return film.year === filmYear
  })
  return result
}

Cinema.prototype.overMinimumLength = function(filmLength){
  const result = this.films.every((film) => {
    return film.length > filmLength
  })
  return result
}

Cinema.prototype.listOfFilmLengths = function(){
  const result = this.films.map((film) => {
    return film.length
  })
  return result
}

Cinema.prototype.totalRunningLengthAllFilms = function(){
  const lengthArray = this.listOfFilmLengths()
  const total = lengthArray.reduce((runningTotal, length) => {
    return runningTotal + length;
  })
  return total
}

Cinema.prototype.searchByProperty = function(nameOfProperty, value){
  const result = this.films.filter((film) => {
    return film[nameOfProperty] === value
  })
  return result
}



module.exports = Cinema;



