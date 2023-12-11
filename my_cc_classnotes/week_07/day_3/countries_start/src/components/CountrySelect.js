import React from "react";
import ListItem from "./ListItem";

const CountrySelect = ({ countries, onCountrySelected }) => {
  const countryItems = countries.map((country, index) => {
    return (
      <option value={index}>{country.name.common}
        {/* <ListItem country={country} key={index} /> */}
      </option>
    );
  });

  return (
    <div>
      <label for="countries">Choose a country:</label>

      <select onChange={(index) => onCountrySelected(index)} name="countries" id="countries">
        {countryItems}
      </select>
    </div>
  );
};

export default CountrySelect;
