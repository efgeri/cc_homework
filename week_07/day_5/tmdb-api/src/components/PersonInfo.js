import React from "react";

const PersonInfo = ({ person, personInfo }) => {
    console.log(personInfo.name)
    console.log(personInfo.credits)
//   const getPersonFilmList = personInfo.credits.crew.map((film) => {
//     return <li>{film.original_title}</li>;
//   });

  return (
    <div>
      <h4>Person Info</h4>
      <p>{person.id}</p>
      <p>{personInfo.name}</p>
      {/* <p>{getPersonFilmList}</p> */}
    </div>
  );
};

export default PersonInfo;
