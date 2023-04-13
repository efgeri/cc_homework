import React from 'react';
import SongItem from './SongItem';

const SongList = ({songs}) => {

    const songsItems = songs.map((song, index) => {
      return <SongItem song={song} key={index} />
    })

  return (
    <div>
    <ul>
      {songsItems}
    </ul>
  </div>
  )
}

export default SongList;