import { useParams } from "react-router-dom";

const Choice = () => {
    const {choice} = useParams()

    return ( 
        <>
            <h1>Choice</h1>
            <p>You've chosen {choice}</p>
        </>
     );
}
 
export default Choice;