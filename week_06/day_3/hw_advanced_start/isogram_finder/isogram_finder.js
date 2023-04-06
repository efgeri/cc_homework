const IsogramFinder = function (word) {
    this.word = word.split('')

}

IsogramFinder.prototype.isIsogram = function () {
    const result = this.word.every((letter, index) => {
        return this.word.indexOf(letter) === index
    })
    return result
}

// let isIsogram = (str) => str.split("").every((c, i) => str.indexOf(c) == i);


module.exports = IsogramFinder;
