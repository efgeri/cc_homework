document.addEventListener('DOMContentLoaded', () => {
  console.log('JavaScript loaded');

  const form = document.querySelector('#new-item-form')
  form.addEventListener("submit", handleFormSubmit)

})

const handleFormSubmit = function(event) {
  event.preventDefault()
  console.log("form event caught")
  console.log(event)
  console.log(event.target.title.value)
  console.log(event.target.author.value)
  console.log(event.target.category.value)

  const newListItem = document.createElement('li')
  newListItem.textContent = `${event.target.title.value} ${event.target.author.value} ${event.target.category.value} `
  newListItem.classList.add('book-details')
  const list = document.querySelector('ul')
  list.appendChild(newListItem)
  document.getElementById('new-item-form').reset()
}