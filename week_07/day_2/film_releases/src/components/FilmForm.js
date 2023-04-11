import React, { useState } from 'react';

const FilmForm = ({onFilmSubmit}) => {
    const [name, setName] = useState('')
    const [url, setUrl] = useState('')

    const handleNameChange = e => setName(e.target.value)

    const handleUrlChange = e => setUrl(e.target.value)

    const handleSubmit = e => {
        e.preventDefault()
        const nameValue = name.trim()
        const urlValue = url.trim()
        if (!nameValue || !urlValue) return

        onFilmSubmit({
            name: nameValue,
            url: urlValue
        })

        setName('')
        setUrl('')
    }

    return ( 
        <form onSubmit={handleSubmit} >
            <input type="text" placeholder="Film title" value={name} onChange={handleNameChange}/>
            <input type="text" placeholder="web address" value={url} onChange={handleUrlChange} />
            <button>Submit</button>
        </form>
     );
}
 
export default FilmForm;