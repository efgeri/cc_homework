const PangramFinder = function (phrase) {
  this.alphabet = 'qwertyuiopasdfghjklzxcvbnm'.split('');
  this.phrase = phrase
}

PangramFinder.prototype.isPangram = function () {
  let lower_phrase = this.phrase.toLowerCase()
  lower_phrase = lower_phrase.split('')
  const result = this.alphabet.every((letter) => {
    return lower_phrase.includes(letter)
  })
  return result
} 

// const pangramFinder = new PangramFinder('the quick brown fox jumps over the lazy dog');
// console.log(pangramFinder.isPangram())
module.exports = PangramFinder;
