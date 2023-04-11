const Upcoming = ({upcoming}) => {
    return ( 
        <>
        <a href={upcoming[0].url}><h3 className="upcoming">{upcoming[0].text}</h3></a>
        </>
     );
}
 
export default Upcoming;