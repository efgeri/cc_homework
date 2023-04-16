import React from "react";
import { useState, useEffect } from "react";
import PeopleList from "../components/PeopleList";

const DataContainer = () => {
    const apikey = process.env.REACT_APP_KEY
    const [ninetiesList, setNinetiesList] = useState([]);
    const [filmCrewData, setFilmCrewData] = useState([]);

    useEffect(() => {
        loadNineties()
        loadFilmCrewData()
    }, [])
    
    const loadNineties = function(){
        fetch(`https://api.themoviedb.org/3/discover/movie?api_key=${apikey}&language=en-US&sort_by=vote_average.desc&include_adult=false&include_video=false&page=1&primary_release_date.gte=1990-01-01&primary_release_date.lte=1999-12-31&vote_count.gte=3000&with_watch_monetization_types=flatrate`)
        .then (res => res.json())
        .then(filmList => {
            setNinetiesList(filmList.results)
        })
    }
    
    const getFilmUrls = ninetiesList.map((film) => {
      return (`https://api.themoviedb.org/3/movie/${film.id}/credits?api_key=${apikey}&language=en-US`)
      // this works, correct elements
    })

    const loadFilmCrewData = function(){
        const crewValues = getFilmUrls.map((url) =>{
            fetch(url)
            .then(res => res.json())
            .then (crewList => {
                setFilmCrewData(crewList.crew)
            })
        })
      }

      const ninetiesListItems = ninetiesList.map((film) => {
        return <li>{film.title}</li>
      })



    return (
        <div>
            <h2>Data Container</h2>

            <ul>
                {ninetiesListItems}
            </ul>
            <PeopleList />
        </div>
    )
}



export default DataContainer