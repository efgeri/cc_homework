import { useState, useEffect } from "react";

import './App.css';

import SightingsForm from "./SightingsForm";
import SightingsGrid from "./SightingsGrid";
import { getSightings } from "./SightingService";

function App() {

  const [birdSightings, setBirdSightings] = useState([]);
  const [currentBirdSightings, setCurrentBirdSightings] = useState({});

  useEffect(() => {
    getSightings().then((allSightings) => {
      setBirdSightings(allSightings);
    })
  }, []);

  const addSighting = (sighting) => {
    setBirdSightings([...birdSightings, sighting]);
  }

  const removeSighting = (id) => {
    const sightingsToKeep = birdSightings.filter(sighting => sighting._id !== id)
    setBirdSightings(sightingsToKeep);
  }

  const modifySighting = (id) => {
    const sightingToChange = birdSightings.filter(sighting => sighting._id === id)
    console.log(sightingToChange)  
    setCurrentBirdSightings(sightingToChange[0])
  }
  console.log(currentBirdSightings)

  return (
    <>
      <SightingsForm addSighting={addSighting} selectedBird={currentBirdSightings}/>
      <SightingsGrid sightings={birdSightings} removeSighting={removeSighting} modifySighting={modifySighting} />
    </>
  );
}

export default App;
