console.log("hello world")

document.addEventListener('DOMContentLoaded', () => {
    const title = document.querySelector('h1')
    title.textContent = "Javascript says hello world"
    const welcome = document.querySelector('#welcome-paragraph')
    welcome.textContent = "You are a wizard Harry!"

    
    const allListItems = document.querySelectorAll('li')
    console.dir(allListItems)
        
    const redListItem = document.querySelector('li.red');
    redListItem.classList.add('bold')
    console.dir(redListItem);

    const newListItem = document.createElement('li')
    newListItem.textContent = "Purple"
    newListItem.classList.add('purple')
    const list = document.querySelector('ul')
    list.appendChild(newListItem)

})