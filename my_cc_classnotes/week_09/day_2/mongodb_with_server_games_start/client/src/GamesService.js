const baseURL = 'http://localhost:9000/api/games/'

export const getGames = () =>{
    return fetch(baseURL)
    .then(res => res.json())
}

export const postGame = (payload) => {
    return fetch(baseURL, {
        method: 'POST',
        body: JSON.stringify(payload),
        headers: { 'Content-Type': 'application/json'}
    })
    .then(res => res.json())
    .then(data => {
        return {
            ...data,
            ...payload
        }
    })
}

export const deleteGame = (id) =>{
    return fetch(baseURL + id, {
        method: 'DELETE'
    })
}

