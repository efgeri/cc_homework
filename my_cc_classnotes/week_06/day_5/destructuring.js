const names = ["Fred", "Kate", "Cindy", "Ricky", "Keith"];
console.log(names);

// const [fred, kate] = names;
// console.log(kate);

const [, , , ricky] = names;      // CHANGED
console.log(ricky); 

const [fred, kate, ...remainingNames] = names;       // CHANGED
console.log(remainingNames);  