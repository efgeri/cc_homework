import React from 'react';

const SongItem = ({song}) => {
//  const handleClick = function() {
//   console.log(`Clicked on ${country.name.common}`)
//   // onCountryClicked(country)
//  }
  console.log(song)
  return <li>Author: {song["im:artist"]["label"]} --- <strong>Album: {song["im:name"]["label"]}</strong> </li>
}

export default SongItem;