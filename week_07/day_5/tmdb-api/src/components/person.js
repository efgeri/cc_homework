import React from "react";

const Person = ({items}) => {
    const getCostumePerson = items.map((person) => {
        if (person.job==="Costume Design") {
            console.log(person.name)
            return <li><button>{person.name}</button></li>
        }
    })
    


    return (
        <div>
        {getCostumePerson}
        </div>
        )
}

export default Person;