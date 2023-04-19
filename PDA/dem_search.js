const searchList = (list, query) => {
    let result = "It's not in the array"
    list.forEach((listItem, index) => {
        if (listItem === query) {
            result = `It's in the array, it's index is ${index}`
        }
    })
    return result
}

const heroes = ["Superman", "Batman", "Flash", "Green Lantern", "Wonder Woman"]

console.log(searchList(heroes, "Flash"))
console.log(searchList(heroes, "Wolverine"))
