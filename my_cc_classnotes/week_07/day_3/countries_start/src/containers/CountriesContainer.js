import React, { useState, useEffect } from 'react';
import CountryList from '../components/CountryList';
import './CountriesContainer.css';
import CountryDetail from '../components/CountryDetail';
import CountrySelect from '../components/CountrySelect';

const CountryContainer = () => {
    const [countries, setCountries] = useState([]);
    const [selectedCountry, setSelectedCountry] = useState(null);

    useEffect(() => {
      getCountries();
    }, [])

    const getCountries = function(){
        fetch('https://restcountries.com/v3.1/all')
        .then(res => res.json())
        .then(countries => {
            setCountries(countries)})
    }

    // const onCountryClicked = function(country) {
    //     setSelectedCountry(country)
    // }
    const onCountrySelected = function(index) {
        setSelectedCountry(countries[index])
        console.log(countries[index])
    }



    return (
        <div className="main-container">
            {/* {selectedCountry ? <h1>{selectedCountry.name.common}</h1> : ""} */}
            {/* <CountryList countries={countries} onCountryClicked={onCountryClicked} /> */}

            <CountrySelect countries={countries} onCountrySelected={onCountrySelected} />
            {selectedCountry ? <CountryDetail country={selectedCountry}/> : null}

        </div>
    )
        }

export default CountryContainer;
