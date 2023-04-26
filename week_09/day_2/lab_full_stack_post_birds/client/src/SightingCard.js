import { deleteSighting, updateSighting } from "./SightingService"

const SightingCard = ({sighting, removeSighting, modifySighting}) => {
    
    const handleDelete = () => {
        deleteSighting(sighting._id).then(()=>{
            removeSighting(sighting._id);
        })
    }

    const handleUpdate = () => {
        modifySighting(sighting._id)
        // updateSighting(sighting._id, ).then(()=>{
        //     removeSighting(sighting._id);
        // })
    }
    return (
        <>
            <h1>{sighting.species}</h1>
            <p>Location: {sighting.location}</p>
            <p>Date: {sighting.date}</p>
            <button onClick={handleDelete}> 🗑 </button>
            <button onClick={handleUpdate}> Update </button>
            <hr></hr>
        </>
    )
}

export default SightingCard;