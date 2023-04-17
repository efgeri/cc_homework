import React from "react";
import Person from "./Person";

const PeopleList = ({ filmCrewData }) => {
  console.log(filmCrewData)
  const peopleListItems = filmCrewData.map((items) => {
    return <Person items={items} />
  })

  return (
    <>
      <h3>PeopleList </h3>
      <ul>{peopleListItems}</ul>
    </>
  );
};

export default PeopleList;