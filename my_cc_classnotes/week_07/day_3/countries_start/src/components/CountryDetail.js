// CountryDetail.js

const CountryDetail = ({country}) => {

    return (
      <div className="country-detail">
        <h2>The capital of {country.name.common} is {country.capital} and the flag is {country.flag}</h2>
        <h3><a href={country.maps.googleMaps} target="_blank" >You can check it out on Google Maps</a></h3>
      </div>
    )
  }
  
  export default CountryDetail;