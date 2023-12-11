document.addEventListener('DOMContentLoaded', () => {
  console.log('JavaScript has loaded');

  const button = document.querySelector('#button')
  button.addEventListener('click', handleButtonClick)

  const input = document.querySelector('#input')
  input.addEventListener("input", handleInput)

  const select = document.querySelector('#select')
  select.addEventListener("change", handleSelectChange)

  const form = document.querySelector('#form')
  form.addEventListener("submit", handleFormSubmit)

});

const handleButtonClick = function() {
  // console.log("Yo the button was clicked man")
  const resultParagraph = document.querySelector('#button-result')
  resultParagraph.textContent = "That button has been totally clicked YO!"
}

const handleInput = function(event) {
  console.log(event.target.value)
  const inputResultParagraph = document.querySelector('#input-result')
  inputResultParagraph.textContent = `You have typed in: ${event.target.value}`
}

const handleSelectChange = function(event) {
  console.log("event caught")
  console.log(event.target.value)
  const selectResultParagraph = document.querySelector('#select-result')
  selectResultParagraph.textContent = `You went with: ${event.target.value}`
}

const handleFormSubmit = function(event) {
  event.preventDefault()
  console.log("form event caught")
  console.log(event)
  console.log(event.target.first_name.value)
  console.log(event.target.last_name.value)
  const formResultParagraph = document.querySelector('#form-result')
  formResultParagraph.textContent = `It's going to be: ${event.target.first_name.value}  ${event.target.last_name.value}`
  const formResultButton = document.querySelector('#submit_name')
  formResultButton.textContent = "Going WIIILLD"
}