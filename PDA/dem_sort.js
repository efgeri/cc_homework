const sortList = (list) => {
    list.sort()
    return list
}

const heroes = ["Superman", "Batman", "Flash", "Green Lantern", "Wonder Woman"]

console.log(`Unsorted list: ${heroes}`)
console.log(`Sorted list: ${sortList(heroes)}`)
