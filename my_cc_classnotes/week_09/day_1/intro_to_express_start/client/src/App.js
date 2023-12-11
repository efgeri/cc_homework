import './App.css';
import {useState, useEffect} from 'react'

function App() {

  const [message, setMessage] = useState("")

  useEffect(() => {
    fetchMessage()
  }, [])

  const fetchMessage = async () => {
    const messageData = await fetch("http://localhost:9000")
    const message = await messageData.json()
    setMessage(message)

  }
  return (
    <>
    <h1>Intro to Express</h1>
    <p>{message.greeting} in year {message.year}</p>
    </>

  );
}

export default App;