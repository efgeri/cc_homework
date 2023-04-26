import SightingCard from "./SightingCard";
const SightingsGrid = ({sightings, removeSighting, modifySighting}) => {
    const sightingsList = sightings.map((sighting) =>{
        return <SightingCard sighting={sighting} key={sighting._id} removeSighting={removeSighting} modifySighting={modifySighting} />
    });
    
    return (
        <>
            {sightingsList}
        </>
    );

}

export default SightingsGrid;